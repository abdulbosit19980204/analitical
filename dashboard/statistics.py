from datetime import datetime
from django.db.models import Sum, Count
from api.models import Order, OrderProductRows
from product.models import Product
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
    month_start = today.replace(year=2020, day=1, hour=0, minute=0, second=0, microsecond=0)

    # Filter products by user's orders and date within the current month
    products = (
        OrderProductRows.objects.filter(order__agent=user, order__dateOrder__gte=month_start)
        .values('NameProduct')
        .annotate(total_sold=Sum('Amount'))
        .order_by('-total_sold')
    )
    return products[:6]  # Top 5 most sold products


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
    year_start = datetime.today().replace(year=2020, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    # Filter orders by user's data and group by month
    sales = (
        Order.objects.filter(agent=user, dateOrder__gte=year_start)
        .annotate(month=TruncMonth('dateOrder'))
        .values('month')
        .annotate(total_sales=Sum('total'))
        .order_by('month')
    )
    return sales


def most_purchased_product_by_user_clients(user):
    # Filter product rows by user's orders and group by client and product
    client_products = (
        OrderProductRows.objects.filter(order__agent=user)
        .values('order__client__name', 'NameProduct')
        .annotate(total_bought=Sum('Amount'))
        .order_by('-total_bought')
    )
    return client_products


def clients_monthly_trade_by_user(user):
    year_start = datetime.today().replace(year=2020, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

    # Filter orders by user's data and group by month and client
    trades = (
        Order.objects.filter(agent=user, dateOrder__gte=year_start)
        .annotate(month=TruncMonth('dateOrder'))
        .values('month', 'client__name')
        .annotate(total_trade=Sum('total'))
        .order_by('month', 'client__name')
    )
    return trades[:10]


def popular_categories_monthly_by_user(user):
    # Filter OrderProductRows by user's orders
    order_product_rows = (
        OrderProductRows.objects.filter(order__agent=user)
        .select_related('order', 'order__client')  # Optimize queries
        .values('CodeProduct', 'order__dateOrder')  # Group by product codes
        .annotate(total_trade=Sum('Total'))  # Total trade for each product
    )
    print(order_product_rows[:5])
    # Fetch products and their categories using the article field
    product_data = {
        product.article: product.product_category.name if product.product_category else "Unknown"
        for product in Product.objects.filter(article__in=[row['CodeProduct'] for row in order_product_rows])
    }

    # Organize trade by category and month
    category_monthly_trade = {}
    for row in order_product_rows:
        product_code = row['CodeProduct']
        category = product_data.get(product_code, "Unknown")  # Default to "Unknown" if category missing
        month = row['order__dateOrder'].strftime('%Y-%m')  # Format as 'YYYY-MM'

        if category not in category_monthly_trade:
            category_monthly_trade[category] = {}

        category_monthly_trade[category][month] = (
                category_monthly_trade[category].get(month, 0) + row['total_trade']
        )

    # Format results
    formatted_results = []
    for category, monthly_data in category_monthly_trade.items():
        formatted_results.append({
            "category": category,
            "monthly_trade": [{"month": month, "total_trade": total_trade} for month, total_trade in
                              monthly_data.items()]
        })

    return formatted_results
