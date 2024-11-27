from itertools import product

from api.models import Warehouse, Organization, Client, Order, CustomUser, OrderDetail, OrderProductRows, \
    OrderCreditDetailsList
from product.models import ProductBrand, ProductSeria, ProductRemainder, Product
from authentic.integrations import client
from datetime import datetime


def Werehouse_sync():
    c_warehouses = client.service.GetWarehouses()
    warehouse_list = []
    if c_warehouses:
        for i in c_warehouses:
            # Get the Organization object based on i['Organization']
            organization = Organization.objects.filter(code=i['Organization']).first()
            # Check if the warehouse already exists based on unique fields (e.g., name and organization)
            if not Warehouse.objects.filter(name=i['Name'], organization=organization).exists():
                # Create the Warehouse object
                warehouse = Warehouse(
                    name=i['Name'],
                    code=i['Code'],  # Replace with correct field from i
                    organization=organization  # Assign the foreign key here
                )
                warehouse_list.append(warehouse)

        # Bulk create new warehouses
        Warehouse.objects.bulk_create(warehouse_list)


def Organizations_sync():
    c_organizations = client.service.GetOrganizations()
    organizations_list = []
    if c_organizations:
        for i in c_organizations:
            if not Organization.objects.filter(code=i['Code']).exists():
                organization = Organization(code=i['Code'], name=i['Name'])
                organizations_list.append(organization)
        Organization.objects.bulk_create(organizations_list)


def Clients_sync(code):
    c_clients = client.service.GetClients(code)
    client_list = []
    if c_clients:
        for i in c_clients:
            if not Client.objects.filter(code=i['Code']).exists():
                i_client = Client(code=i['Code'], name=i['Name'], signboard=i['Signboard'], inn=i['INN'],
                                  adressDelivery=i['AdressDelivery'], referencePoint=i['ReferencePoint'],
                                  longitude=i['Longitude'], latitude=i['Latitude'], contactPerson=i['ContactPerson'],
                                  contactPersonPhone=i['ContactPersonPhone'], responsiblePerson=i['ResponsiblePerson'],
                                  responsiblePersonPhone=i['ResponsiblePersonPhone'],
                                  tradePointType=i['TradePointType'], theNumberOfOrders=i['TheNumberOfOrders'],
                                  creditLimit=i['CreditLimit'],
                                  accumulatedCredit=i['AccumulatedCredit'], codeRegion=i['CodeRegion'],
                                  director=i['Director'], mfo=i['MFO'], bankAccount=i['BankAccount'])
                client_list.append(i_client)
        Client.objects.bulk_create(client_list)


def Orders_sync(code):
    c_orders = client.service.GetOrderList(code, '20200101000000', '20241231000000')
    print(c_orders)
    order_list = []
    if c_orders:
        for i in c_orders:
            if not Order.objects.filter(numOrder=i['NumOrder'], clientCode=i['ClientCode']).exists():
                i_order = Order(numOrder=i['NumOrder'], clientCode=i['ClientCode'], dateOrder=i['DateOrder'],
                                captionOrder=i['CaptionOrder'], typePrice=i['TypePrice'], status=i['Status'],
                                commentSupervisor=i['CommentSupervisor'], commentForwarder=i['CommentForwarder'],
                                total=i['Total'], clientName=i['ClientName'], codeOrg=i['CodeOrg'],
                                client=Client.objects.filter(code=i['ClientCode']).first(),
                                agent=CustomUser.objects.filter(code=code).first(),
                                )
                order_list.append(i_order)
        Order.objects.bulk_create(order_list)


def OrderDetails_sync(code):
    order = Order.objects.filter(agent__code=code)
    order_detail_list = []
    order_product_rows_list = []
    credit_details_list = []
    if order:
        for i in order:
            o_time = str(i.dateOrder).replace("-", "").replace("+00:00", "").replace(" ", '').replace(':', '')
            c_order_detail = client.service.GetOrderDetails(i.numOrder, o_time, o_time)
            if not OrderDetail.objects.filter(numOrder=i.numOrder,
                                              CodeSklad=c_order_detail['CodeSklad']).exists():
                i_order_detail = OrderDetail(
                    numOrder=i.numOrder,
                    CodeSklad=c_order_detail['CodeSklad'],
                    DateOrder=c_order_detail['DateOrder'],
                    Credit=c_order_detail['Credit'],
                    CodePrice=c_order_detail['CodePrice'],
                    OrderType=c_order_detail['OrderType'],
                    CodeOrg=c_order_detail['CodeOrg'],
                    ShippingDate=c_order_detail['ShippingDate'],
                    order=Order.objects.filter(numOrder=i.numOrder).first(),
                )
                order_detail_list.append(i_order_detail)
                for j in c_order_detail['ProductRows'][0]['Rows']:
                    order_product_row = OrderProductRows(
                        order=i,
                        CodeProduct=j['CodeProduct'],
                        NameProduct=j['NameProduct'],
                        Amount=j['Amount'],
                        Price=j['Price'],
                        Total=j['Total'],
                        DiscountRate=j['DiscountRate'],
                        Weight=j['Weight'],
                        Capacity=j['Capacity']
                    )
                    order_product_rows_list.append(order_product_row)
                credit = c_order_detail['CreditDetailsList']
                if credit is not None:
                    for k in credit.Rows:
                        # Convert the string "20240930000000" to a proper datetime object
                        date_of_payment_str = k['DateOfPayment']
                        try:
                            date_of_payment = datetime.strptime(date_of_payment_str, '%Y%m%d%H%M%S')
                        except ValueError:
                            date_of_payment = None
                        credit_detail = OrderCreditDetailsList(
                            order=i,
                            Total=k['Total'],
                            DateOfPayment=date_of_payment,
                        )
                        credit_details_list.append(credit_detail)
                    print(credit_details_list)
        OrderDetail.objects.bulk_create(order_detail_list)
        OrderProductRows.objects.bulk_create(order_product_rows_list)
        OrderCreditDetailsList.objects.bulk_create(credit_details_list)


def GetProductsBlance_sync(code_project='00000000004', code_sklad='00000000201'):
    products = client.service.GetProductBalance(code_project, code_sklad)
    brands = []
    series = []
    reminders = []
    for i in products:
        for j in i.Rows:
            for k in j.Rows:
                for r in k.Rows:
                    for t in r.Rows:
                        print(t)
                        d = ProductRemainder(
                            product=Product.objects.filter(id=1).first(),
                            warehouse=Warehouse.objects.filter(code=t['CodeSklad']).first(),
                            CodeProduct=t['CodeProduct'],
                            NameProduct=t['NameProduct'],
                            Have=t['Have'],
                            Reserved=t['Reserved'],
                            Aviable=t['Aviable'],
                            CodeProject=t['CodeProject'],

                        )
                        reminders.append(d)
                pseries = ProductSeria.objects.filter(name=k.ProductSeries)
                if pseries.exists():
                    continue
                else:
                    seria = ProductSeria(name=k.ProductSeries)
                    series.append(seria)

        pbrand = ProductBrand.objects.filter(name=i['ProductBrand'])
        if pbrand.exists():
            continue
        else:
            brand = ProductBrand(
                name=i.ProductBrand,
            )
            brands.append(brand)
    ProductBrand.objects.bulk_create(brands)
    ProductSeria.objects.bulk_create(series)
    ProductRemainder.objects.bulk_create(reminders)
    return products
