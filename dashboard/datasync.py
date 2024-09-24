from api.models import Warehouse, Organization, Client, Order, CustomUser, OrderDetail
from authentic.integrations import client


def Werehouse_sync():
    c_warehouses = client.service.GetWarehouses()
    warehouse_list = []
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
    for i in c_organizations:
        if not Organization.objects.filter(code=i['Code']).exists():
            organization = Organization(code=i['Code'], name=i['Name'])
            organizations_list.append(organization)
    Organization.objects.bulk_create(organizations_list)


def Clients_sync(code):
    c_clients = client.service.GetClients(code)
    client_list = []

    for i in c_clients:
        if not Client.objects.filter(code=i['Code']).exists():
            i_client = Client(code=i['Code'], name=i['Name'], signboard=i['Signboard'], inn=i['INN'],
                              adressDelivery=i['AdressDelivery'])
            client_list.append(i_client)
    Client.objects.bulk_create(client_list)


def Orders_sync(code):
    c_orders = client.service.GetOrderList(code)

    order_list = []

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

    for i in order:
        print(i.dateOrder)
        o_time = str(i.dateOrder).replace("-", "").replace("+00:00", "").replace(" ", '').replace(':', '')
        print(o_time)
        print(order_detail_list)
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
    OrderDetail.objects.bulk_create(order_detail_list)
