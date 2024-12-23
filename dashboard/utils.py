from datetime import timedelta, datetime
from django.db.models import Count, Q, Avg

from authentic.integrations import client
from api.models import Client, Order


# 1. Business regionlarni olish
def get_business_regions(code):
    return client.service.GetBusinessRegions(code)


# 2. Faol mijozlarni aniqlash
def calculate_active_clients(user, date_limit):
    today = datetime.today()

    # Oxirgi 3 oyda har bir oy faol bo'lgan mijozlar
    active_clients = Client.objects.filter(
        order__agent=user,
        order__dateOrder__gte=date_limit
    ).annotate(
        this_month=Count('order', filter=Q(order__dateOrder__month=today.month)),
        last_month=Count('order', filter=Q(order__dateOrder__month=(today.month - 1) % 12 or 12)),
        two_months_ago=Count('order', filter=Q(order__dateOrder__month=(today.month - 2) % 12 or 12))
    ).filter(this_month__gt=0, last_month__gt=0, two_months_ago__gt=0)

    return active_clients


# 3. Passiv mijozlarni aniqlash
def calculate_passive_clients(user, one_month_ago, active_clients, region_codes):
    """
    Passiv mijozlarni aniqlash:
    Oxirgi 1 oy davomida faol bo'lmagan yoki buyurtma qilmagan, lekin mas'ul regionga tegishli mijozlar.
    """
    passive_clients = Client.objects.filter(
        Q(order__dateOrder__lt=one_month_ago) |  # Oxirgi oydan oldin buyurtma qilgan mijozlar
        Q(order__isnull=True),  # Hech qanday buyurtma qilmagan mijozlar
        codeRegion__in=region_codes  # Faqat mas'ul region(lar)ga tegishli mijozlar
    ).exclude(
        id__in=active_clients.values_list('id', flat=True)  # Faol mijozlar ro'yxatini chiqarib tashlash
    ).distinct()

    return passive_clients


# 4. Mijozlarni buyurtmalar bo'yicha guruhlash
def group_clients_by_orders(user):
    client_order_counts = Order.objects.filter(agent=user).values('clientCode').annotate(
        order_count=Count('id')
    )
    avg_orders = client_order_counts.aggregate(avg_orders=Avg('order_count'))['avg_orders'] or 0
    top_clients = client_order_counts.filter(order_count__gt=avg_orders)
    few_clients = client_order_counts.filter(order_count__lte=avg_orders)

    return {
        'average_orders': avg_orders,
        'top_clients': list(top_clients),
        'few_clients': list(few_clients),
    }
