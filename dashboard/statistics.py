from datetime import datetime
from django.db.models import Sum
from api.models import Order, OrderProductRows
from django.db.models.functions import TruncMonth


def daily_order_statistics(user):
    today = datetime.today()
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    orders = Order.objects.filter(agent=user, dateOrder__gte=start_of_day, dateOrder__lte=today)
    total_sales = orders.aggregate(total_sum=Sum('total'))['total_sum'] or 0
    return {
        "daily_orders_count": orders.count(),
        "daily_total_sales": total_sales,
    }


def most_sold_products_monthly_by_user(user):
    today = datetime.today()
    month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Filter products by user's orders and date within the current month
    products = (
        OrderProductRows.objects.filter(order__agent=user, order__dateOrder__gte=month_start)
        .values('NameProduct')
        .annotate(total_sold=Sum('Amount'))
        .order_by('-total_sold')
    )
    return products[:5]  # Top 5 most sold products


def product_sales_statistics_by_user(user):
    # Filter products by user's orders
    products = (
        OrderProductRows.objects.filter(order__agent=user)
        .values('NameProduct')
        .annotate(total_sold=Sum('Amount'))
        .order_by('-total_sold')
    )
    return products


def yearly_sales_statistics_by_user(user):
    year_start = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    # Filter orders by user's data and group by month
    sales = (
        Order.objects.filter(agent=user, dateOrder__gte=year_start)
        .annotate(month=TruncMonth('dateOrder'))
        .values('month')
        .annotate(total_sales=Sum('total'))
        .order_by('month')
    )
    return sales
