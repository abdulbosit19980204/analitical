from datetime import timedelta, datetime
from django.db.models import Count, Q, Avg

from authentic.integrations import client
from api.models import Client, Order


# 1. Business regionlarni olish
def get_business_regions(code):
    """
    Retrieve business regions associated with a given code.

    Args:
        code (str): The unique code representing a business entity or region.

    Returns:
        list: A list of business regions retrieved from the client service.
    """
    return client.service.GetBusinessRegions(code)


# 2. Faol mijozlarni aniqlash
def calculate_active_clients(user, date_limit):
    """
    Identify active clients who placed orders in the last three months.

    Args:
        user (User): The agent whose clients are being considered.
        date_limit (datetime): The date from which to start calculating activity.

    Returns:
        QuerySet: A queryset of clients who were active (placed orders) in each of the last three months.
    """
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
    Identify passive clients who were inactive for the last month but belong to specified regions.

    Args:
        user (User): The agent analyzing clients.
        one_month_ago (datetime): Cutoff date for identifying passive clients.
        active_clients (QuerySet): The list of active clients to exclude.
        region_codes (list): List of region codes to filter clients.

    Returns:
        QuerySet: A queryset of clients who were either inactive for the last month or placed no orders,
                  and who belong to the specified regions, excluding active clients.
    """
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
    """
    Group clients based on their number of orders compared to the average number of orders.

    Args:
        user (User): The agent examining client orders.

    Returns:
        dict: A dictionary containing:
              - `average_orders` (float): The average number of orders per client.
              - `top_clients` (list): Clients whose order count is above average.
              - `few_clients` (list): Clients whose order count is at or below average.
    """
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
