from numbers import Number
import json
from collections import defaultdict
# from api.models import Warehouse

from zeep import Settings, Client
from zeep.plugins import HistoryPlugin
from zeep.transports import Transport

settings = Settings(strict=False, xml_huge_tree=True)
history = HistoryPlugin()
transport = Transport(timeout=10)
# reasionReturn = 'http://192.168.1.241:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
# reasionReturn = 'http://kit.gloriya.uz:5443/EVYAPTEST/EVYAPTEST.1cws?wsdl'
reasionReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
# reasionReturn = ''
client = Client(wsdl=reasionReturn, transport=transport, plugins=[history], settings=settings)


def user():
    user = client.service.GetUserByTelegramID(6410170725)
    # print(user)


# user()


def customers(login, password):
    customers = client.service.GetUser(login, password)
    print(customers)


# customers('ТП-12', '1424')


def priceList(userCode):
    priceList = client.service.GetPriceList(userCode)
    return priceList


pls = priceList('000000327')


def price_types(userCode):
    priceTypes = client.service.GetPriceTypes(userCode)
    return priceTypes


pts = price_types('000000327')

for pl in pls:
    for pt in pts:
        if pl['CodeTypePrice'] == pt['Code']:
            pl['CodeTypePrice'] = pt['Name']
            # print(pl)


def kpis(userCode):
    kpis = client.service.GetKPI(userCode)
    print(kpis)


# kpis('000000327')


def getTradePointTypeList(userCode):
    tps = client.service.GetTradePointTypeList(userCode)
    return tps


# getTradePointTypeList('000000327')


def typeOfContract():
    typeOfContract = client.service.GetTypeOfContract()
    print(typeOfContract)


# typeOfContract()


def GetDailyReport(userCode):
    dyr = client.service.GetDailyReport(userCode)
    print(dyr)


# GetDailyReport('000000327')


def GetWarehouses():
    wherehouse = client.service.GetWarehouses()
    # print(wherehouse)

    return wherehouse


# GetWarehouses()


def getKPI(CodeUser):
    Kpi = client.service.GetKPI('000000327')
    print(Kpi)


# getKPI('000000327')


def getOrderList(CodeAgent):
    orderList = client.service.GetOrderList(CodeAgent)
    # print(orderList)
    return orderList


# print(getOrderList('000000327'))


def clientList(UserCode):
    clientList = client.service.GetClients(UserCode)
    # print(clientList)
    return clientList


# clientList('000000327')


def getOrderDetail_view(NumberOrder, OrderDate1, OrderDate2):
    orderDetail = client.service.GetOrderDetails(NumberOrder, OrderDate1, OrderDate2)
    # print(orderDetail)
    return orderDetail


# getOrderDetail_view('GL00-165881', 20240613000000, '20241013000000')
# getOrderDetail_view('GL00-166025', 20240613000000, '20241013000000')


def orderListWithSklad(UserCode):
    for order in getOrderList(UserCode):
        orderDetail = getOrderDetail_view(order.NumOrder, 20240613000000, '20241213000000')
        for sklad in GetWarehouses():
            if orderDetail.CodeSklad == sklad.Code:
                orderDetail.Sklad = sklad.Name
                print(orderDetail)


product_sales = defaultdict(int)
product_sales_sum = defaultdict(int)


def productSoldCount(UserCode):
    for order in getOrderList(UserCode):
        orderDetail = getOrderDetail_view(order.NumOrder, 20240613000000, '20241213000000')
        # Loop through each order
        for product_row in orderDetail["ProductRows"]:
            for row in product_row["Rows"]:
                # Update the product count
                product_sales[row["NameProduct"]] += row["Amount"]
                product_sales_sum[row["NameProduct"]] += row["Total"]
    top_sales = []
    for product_c, total_sold in product_sales.items():
        pr = {}
        for product_s, total_sum in product_sales_sum.items():
            if product_c == product_s:
                pr['product'] = product_c
                pr['count'] = total_sold
                pr['total_sum'] = total_sum
                top_sales.append(pr)
    print(top_sales)


# productSoldCount('000000327')
# orderListWithSklad('000000327')


def GetKPIDate(UserCode, Date):
    Kpi = client.service.GetKPIDate(UserCode, Date)
    print(Kpi)


# GetKPIDate('000000184', '20240730000000')

def werehouse():
    werehouses = client.service.GetWarehouses()
    print(werehouses)


# werehouse()

def getShippingList(userCode):
    shippingList = client.service.GetShippingList(userCode)
    print(shippingList)


getShippingList('000000184')


def GetPackage(dateOfPackage, codeUser, codeClient):
    package = client.service.GetPackage(dateOfPackage, codeUser, codeClient)
    print(package)

# GetPackage('20240922000000', '000000327', '')
