
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from .models import Wheel, Recommend, ClothesType, Jacket, Pants, Shoes, Others, User, Cart, Address, \
    OrderInfo, OrderGoods
from django.core.paginator import Paginator
import random
import time
import re
from django.conf import settings
import os
# Create your views here.
def index(request):
    pass

def main(request):
    wheelList = Wheel.objects.all()
    recommendList = Recommend.objects.all()
    clothesTypeList = ClothesType.objects.all()
    jacketList = Jacket.objects.all()
    pantsList = Pants.objects.all()
    shoesList = Shoes.objects.all()
    othersList = Others.objects.all()
    #上衣子类型划分为列表*****************0
    childnames0 = clothesTypeList[0].childTypeNames
    childList0 = []
    # #进口水果:103534#国产水果:103533
    arr1 = childnames0.split("#")
    for str in arr1:
        # 全部分类:0
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList0.append(obj)
    #*****************1
    childnames1 = clothesTypeList[1].childTypeNames
    childList1 = []
    arr1 = childnames1.split("#")
    for str in arr1:
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList1.append(obj)
    # *****************2
    childnames2 = clothesTypeList[2].childTypeNames
    childList2 = []
    arr1 = childnames2.split("#")
    for str in arr1:
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList2.append(obj)
    # *****************3
    childnames3 = clothesTypeList[3].childTypeNames
    childList3 = []
    arr1 = childnames3.split("#")
    for str in arr1:
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList3.append(obj)

    #base 页面内容更新
    # 登录之后，将用户名更改
    username = request.session.get("account", "亲，请登录")
    cartList = []
    total_count = 0
    token = request.session.get("token")
    # token值用于判断登没登录，登陆之后才能取值
    if token != None:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects1.filter(userAccount=user.userAccount)
        for i in cartList:
            total_count += i.goodsNum

    return render(request, 'jiajiale/main.html',{"wheelList":wheelList,"recommendList":recommendList,
                            "jacketList":jacketList,"pantsList":pantsList,"shoesList":shoesList,
                            "othersList": othersList,"clothesTypeList":clothesTypeList,"childList0":childList0,
                            "childList1":childList1,"childList2":childList2,"childList3": childList3,
                            "username":username, 'total_count': total_count})


def detail(request, flag, track_id):
    if flag == "0":
        try:
            childName = '上衣'
            goods = Jacket.objects.get(trackId=track_id)
        except Jacket.DoesNotExit:
            # 所查商品不存在，返回一个页面
            return redirect('/main/')
    elif flag == "1":
        try:
            childName = '下装'
            goods = Pants.objects.get(trackId=track_id)
        except Pants.DoesNotExit:
            return redirect('/main/')
    elif flag == "2":
        try:
            childName = '鞋'
            goods = Shoes.objects.get(trackId=track_id)
        except Shoes.DoesNotExit:
            return redirect('/main/')
    else:
        try:
            childName = '其它'
            goods = Others.objects.get(trackId=track_id)
        except Others.DoesNotExit:
            return redirect('/main/')

    # base 页面内容更新
    # 登录之后，将用户名更改
    username = request.session.get("account", "亲，请登录")
    cartList = []
    total_count = 0
    token = request.session.get("token")
    # token值用于判断登没登录，登陆之后才能取值
    if token != None:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects1.filter(userAccount=user.userAccount)
        for i in cartList:
            total_count += i.goodsNum

    return render(request, 'jiajiale/detail.html', {'username':username, 'goods': goods, 'childName':childName,
                                "flag":flag,"total_count":total_count})


def cart(request):
    # base 页面内容更新
    # 登录之后，将用户名更改
    username = request.session.get("account", "亲，请登录")
    cartList = []
    token = request.session.get("token")
    total_price = 0
    total_count = 0
    total_num = 0
    # token值用于判断登没登录，登陆之后才能取值
    if token != None:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects1.filter(userAccount=user.userAccount)
        for c in cartList:
            c.thePrice = c.goodsPrice / c.goodsNum  #给商品增加thePrice属性，html直接调用即可
        for c in cartList:
            total_count += c.goodsNum
            if c.isChose:
                total_num += c.goodsNum
                total_price += c.goodsPrice

    return render(request, 'jiajiale/cart.html', {"username":username, "cartList": cartList,"total_count":total_count,
                                    "total_price": total_price,"total_num":total_num})


def cartAdd(request):
    # 判断用户是否登录
    global goods, total_count
    token = request.session.get("token")
    if token == None:
        # 没登录
        return JsonResponse({'res': 0, 'errmsg': '请先登录'})

    # 接收数据，用post方法因此不在定义函数中以形参出现
    track_id = request.POST.get('track_id')
    flag = request.POST.get('flag')
    count = request.POST.get('count')
    user = User.objects.get(userToken=token)

    # 校验数据合法性
    if not all([track_id, count]):
        return JsonResponse({'res': 1, 'errmsg': '数据不完整'})
    # 校验商品数量合法性
    try:
        count = int(count)
    except Exception:
        return JsonResponse({'res': 2, 'errmsg': '数目出错'})

    if flag == '0':
        # 校验商品是否存在
        try:
            goods = Jacket.objects.get(trackId=track_id)
        except Jacket.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})
    if flag == '1':
        try:
            goods = Pants.objects.get(trackId=track_id)
        except Pants.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})
    if flag == '2':
        try:
            goods = Shoes.objects.get(trackId=track_id)
        except Shoes.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})
    if flag == '3':
        try:
            goods = Others.objects.get(trackId=track_id)
        except Others.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

    # 校验库存值，设置对应值
    if count > goods.stockNum:
        return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})

    cartList = Cart.objects1.filter(userAccount=user.userAccount)
    goodsPrice = goods.goodsPrice * count
    c = None
    if cartList.count() == 0:
        # 直接增加一条订单
        c = Cart.createcart(user.userAccount, goods.name, goods.img, goods.trackId, count, goodsPrice,
                            True, False, "0")
        c.save()
    else:
        try:
            c = cartList.get(trackId=track_id)  # 购物车中该商品情况
            # 修改数量和价格
            c.goodsNum = c.goodsNum + count
            c.goodsPrice = goods.goodsPrice * c.goodsNum

            c.save()
        except Cart.DoesNotExist as e:
            # 直接增加一条订单
            c = Cart.createcart(user.userAccount, goods.name, goods.img, goods.trackId, count, goodsPrice,
                                True, False, "0")
            c.save()
    goods.stockNum -= count
    goods.save()

    return JsonResponse({'res': 5, 'errmsg': '添加成功'})


def changeCart(request, label):
    # 判断用户是否登录
    token = request.session.get("token")
    if token == None:
        # 没登录
        return JsonResponse({"data": -1, "status": "error"})
    user = User.objects.get(userToken=token)
    goods_id = request.POST.get("goods_id")

    flag = (int(goods_id) % 100) // 10
    # 通过商品id拿出该商品其他数据
    if flag == 0:
        goods = Jacket.objects.get(trackId=goods_id)
    elif flag == 1:
        goods = Pants.objects.get(trackId=goods_id)
    elif flag == 2:
        goods = Shoes.objects.get(trackId=goods_id)
    else:
        goods = Others.objects.get(trackId=goods_id)
    if label == '0':
        if goods.stockNum == 0:
            return JsonResponse({"data": -2, "status": "error"})  # 库存已满，添加不上了，下面就走不通了
        carts = Cart.objects1.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            # 直接增加一条订单
            c = Cart.createcart(user.userAccount, goods.name, goods.img, goods.trackId, 1, goods.goodsPrice,
                                True, False, "0")
            c.save()
        else:
            try:
                c = carts.get(trackId=goods_id)
                # 修改数量和价格
                c.goodsNum += 1
                c.goodsPrice = (goods.goodsPrice) * c.goodsNum
                c.save()
            except Cart.DoesNotExist as e:
                # 直接增加一条订单
                c = Cart.createcart(user.userAccount, goods.name, goods.img, goods.trackId, 1, goods.goodsPrice,
                                    True, False, "0")
                c.save()
        # 库存减一
        goods.stockNum -= 1
        goods.save()

        num = c.goodsNum
        price = c.goodsPrice  # 保存修改后商品的价格，不然下面遍历carts就会改变
        carts = Cart.objects1.filter(userAccount=user.userAccount)
        total_price = 0
        total_num = 0
        for c in carts:
            if c.isChose:
                total_price += c.goodsPrice
                total_num += c.goodsNum
        return JsonResponse({"data": num, "price": price,"total_price":total_price,'total_num':total_num,
                             "status": "success"})
    elif label == '1':
        carts = Cart.objects1.filter(userAccount=user.userAccount)
        c = None
        if carts.count() == 0:
            return JsonResponse({"data": -2, "status": "error"})
        else:
            try:
                c = carts.get(trackId=goods_id)
                # 修改数量和价格
                c.goodsNum -= 1
                c.goodsPrice = (goods.goodsPrice) * c.goodsNum
                if c.goodsNum == 0:
                    c.delete()
                else:
                    c.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})
        # 库存加一
        goods.stockNum += 1
        goods.save()

        num = c.goodsNum
        price = c.goodsPrice #保存修改后商品的价格，不然下面遍历carts就会改变
        carts = Cart.objects1.filter(userAccount=user.userAccount)
        total_price = 0
        total_num = 0
        for c in carts:
            if c.isChose:
                total_price += c.goodsPrice
                total_num += c.goodsNum
        return JsonResponse({"data": num, "price": price,"total_price":total_price,"total_num":total_num, "status": "success"})
    else:
        carts = Cart.objects1.filter(userAccount=user.userAccount)
        c = carts.get(trackId=goods_id)
        c.isChose = not c.isChose
        c.save()
        str = ""
        if c.isChose:
            str = "√"

        carts = Cart.objects1.filter(userAccount=user.userAccount)
        total_price = 0
        total_num = 0
        for c in carts:
            if c.isChose:
                total_price += c.goodsPrice
                total_num += c.goodsNum
        return JsonResponse({"data": str, "status": "success","total_price":total_price,"total_num":total_num})

    # else:
    #     carts = Cart.objects1.filter(userAccount=user.userAccount)
    #     total_price = 0
    #     total_num = 0
    #     for c in carts:
    #         total_price += c.goodsPrice
    #         total_num += c.goodsNum
    #     allFlag = True
    #     for c in carts:
    #         if not c.isChose:
    #             allFlag = False
    #             c.isChose = not c.isChose
    #             c.save()
    #     carts = Cart.objects1.filter(userAccount=user.userAccount)
    #     if allFlag:
    #         for c in carts:
    #             c.isChose = not c.isChose
    #         total_price = 0
    #         total_num = 0
    #     return JsonResponse({"data": 1, "status": "success", "total_price": total_price, "total_num": total_num})


def userInfo(request):
    global user
    token = request.session.get("token")
    if token == None:
        # 没登录
        return redirect('/login/')
    # base 页面内容更新
    # 登录之后，将用户名更改
    username = request.session.get("account", "亲，请登录")
    cartList = []
    total_count = 0
    token = request.session.get("token")
    # token值用于判断登没登录，登陆之后才能取值
    if token != None:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects1.filter(userAccount=user.userAccount)
        for i in cartList:
            total_count += i.goodsNum
    return render(request, 'jiajiale/userInfo.html', {"username":username, "total_count":total_count,
                            'user':user,'page':'info'})


def userOrder(request,page):
    global total_price
    token = request.session.get("token")
    if token == None:
        # 没登录
        return redirect('/login/')
    # 登录之后，将用户名更改
    username = request.session.get("account", "亲，请登录")
    # base 页面内容更新
    cartList = []
    total_count = 0
    token = request.session.get("token")
    # token值用于判断登没登录，登陆之后才能取值
    if token != None:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects1.filter(userAccount=user.userAccount)
        for i in cartList:
            total_count += i.goodsNum

    orders = OrderInfo.objects.filter(user=user).order_by('-create_time')
    # 遍历获取订单商品的信息
    for order in orders:
        # 根据orderId查询订单商品的信息，并动态增加商品信息属性
        order_goods = OrderGoods.objects.filter(order=order.orderId)
        # 遍历order_goods计算商品的小计，并动态增加小计
        total_price = 0
        for order_good in order_goods:
            amount = order_good.count * order_good.price
            order_good.amount = amount #获取该商品总价
            total_price += amount
        order.order_goods = order_goods
    paginator = Paginator(orders, 2)
    # 获取要求页码的内容
    try:
        page = int(page)
    except Exception as e:
        page = 1
    # 判断页码是否超出
    if page > paginator.num_pages:
        page = 1

    # 获取指定页码的内容
    order_page = paginator.page(page)
    # 至多显示5个页码，显示当前页的前两页和后两页
    # 1.页面小于5页，页面上显示所有页码
    # 2.当前页是前3页，显示1-5页
    # 3.当前页是后3页，显示后5页
    # 4.其余：显示当前页的前两页和后两页
    # 5.添加跳转到第几页和最后一页的按钮，后续实现
    num_pages = paginator.num_pages
    if num_pages <= 5:
        pages = range(1, num_pages + 1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages - 4, num_pages + 1)
    else:
        pages = range(page - 2, page + 3)

    # 组织上下文
    context = {
        "username": username,
        "total_count": total_count,
        "total_price":total_price,
        'order_page': order_page,
        'pages': pages,
        'page': 'order', }
    return render(request, 'jiajiale/userOrder.html', context)


def userAddress(request):
    global user
    if request.method == "POST":
        '''地址的添加'''
        receiver = request.POST.get('receiver')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        if not all([receiver, address, phone,zipcode]):
            return render(request, 'jiajiale/userAddress.html', {'errmsg': '数据不完整，请重新输入'})
        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'jiajiale/userAddress.html', {'errmsg': '手机号不合法，请重新输入'})

        # 获取登录用户对应的User实例对象
        token = request.session.get("token")
        user = User.objects.get(userToken=token)
        # 添加收货地址
        Address.objects.create(user=user.userAccount,receiver=receiver,address=address,zipCode=zipcode, phone=phone)
        # 返回应答，刷新地址页面，以get方式再访问当前页面
        return redirect('/userAddress/')
        # 可以添加让用户在多个收货地址中选择默认收货地址的功能，需要在模板中显示用户的所有收货地址
    else:
        # base 页面内容更新
        # 登录之后，将用户名更改
        username = request.session.get("account")
        cartList = []
        total_count = 0
        token = request.session.get("token")
        # token值用于判断登没登录，登陆之后才能取值
        if token != None:
            user = User.objects.get(userToken=token)
            cartList = Cart.objects1.filter(userAccount=user.userAccount)
            for i in cartList:
                total_count += i.goodsNum

        addressList = Address.objects.filter(user=username)
        return render(request, 'jiajiale/userAddress.html', {"username":username, "total_count":total_count,
                                'addressList':addressList,'page':'address'})


def saveOrder(request):
    if request.method == "POST":
        user = request.session.get("account")
        # 如果购物车里的商品没有被选择
        carts = Cart.objects1.filter(userAccount=user,isChose=True)
        if carts.count() == 0:
            return redirect("/cart/")
        address = '河南省信阳市商城县李集乡  hzy  (收)  18866668888'
        total_goods_count = 0
        total_pay = 0
        cart_track_ids = []
        for c in carts:
            c.thePrice = c.goodsPrice / c.goodsNum
            total_goods_count += c.goodsNum
            total_pay += c.goodsPrice
            cart_track_ids.append(c.trackId)
        cart_track_ids = ','.join(cart_track_ids)


        # base 页面内容更新
        # 登录之后，将用户名更改
        username = request.session.get("account")
        cartList = []
        total_count = 0
        token = request.session.get("token")
        # token值用于判断登没登录，登陆之后才能取值
        if token != None:
            user = User.objects.get(userToken=token)
            cartList = Cart.objects1.filter(userAccount=user.userAccount)
            for i in cartList:
                total_count += i.goodsNum

        context = {
            "username": username,
            "total_count": total_count,
            "address": address,
            "carts": carts,
            "total_goods_count":total_goods_count,
            "total_pay":total_pay,
            "cart_track_ids":cart_track_ids
        }
        return render(request, 'jiajiale/saveOrder.html', context)


def orderCommit(request):
    if request.method == "POST":
        token = request.session.get("token")
        if token == None:
            # 没登录
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        user = User.objects.get(userToken=token)
        # username = request.session.get("account")
        address = request.POST.get('address')
        pay_method = request.POST.get('pay_method')
        cart_track_ids = request.POST.get('cart_track_ids')

        #获取参数
        cart_track_ids = cart_track_ids.split(',')
        # 校验参数
        if not all([address, pay_method, cart_track_ids]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})
        # 校验支付方式
        pay_method = int(pay_method)
        if pay_method not in OrderInfo.PAY_METHOD.keys():
            return JsonResponse({'res': 2, 'errmsg': '非法的支付方式'})
        # 校验地址
        # try:
        #     address = Address.objects.get(id=address_id)
        # except Address.DoesNotExist:
        #     return JsonResponse({'res': 3, 'errmsg': '地址不存在'})
        orderId = time.time() + random.randrange(1, 10000)
        orderId = "%d" % orderId  # 取了这个数的整数部分
        transit_price = 0
        # 总数目和总金额,添加记录，先使用默认值，后续修改
        total_count = 0
        total_price = 0
        # 向订单信息表中添加记录
        order = OrderInfo.objects.create(orderId=orderId,
                                         user=user,
                                         address=address,
                                         pay_method=pay_method,
                                         transit_price=transit_price,
                                         total_price=total_price,
                                         total_count=total_count)
        cartList = Cart.objects1.filter(userAccount=user.userAccount, isChose=True)
        for goods_id in cart_track_ids:
            try:
                flag = (int(goods_id) % 100) // 10
                # 通过商品id拿出该商品其他数据
                if flag == 0:
                    goods = Jacket.objects.get(trackId=goods_id)
                elif flag == 1:
                    goods = Pants.objects.get(trackId=goods_id)
                elif flag == 2:
                    goods = Shoes.objects.get(trackId=goods_id)
                else:
                    goods = Others.objects.get(trackId=goods_id)
            except Cart.DoesNotExist:
                return JsonResponse({'res': 4, 'errmsg': '商品不存在'})

            c = cartList.get(trackId=goods_id)
            OrderGoods.objects.create(order=order,
                                      name=goods.name,
                                      img=goods.img,
                                      count=c.goodsNum,
                                      price=goods.goodsPrice)

            # 计算订单商品的总数量和总价格
            amount = goods.goodsPrice * c.goodsNum
            total_count += c.goodsNum
            total_price += amount
        # 更新订单详情表中的总数量和总价格
        order.total_count = total_count
        order.total_price = total_price
        order.save()
        # 清除用户购物车中的记录
        carts = Cart.objects1.filter(userAccount=user.userAccount, isChose=True)
        for c in carts:
            c.delete()
        return JsonResponse({'res': 6, 'message': '订单创建成功'})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        remember = request.POST.get('remember')

        if not all([username, password]):
            return render(request, 'jiajiale/login.html', {'errmsg': '信息填写不完整'})

        # 校验用户是否确认登录
        if remember != 'on':
            return render(request, 'jiajiale/login.html', {'errmsg': '请勾选确认登录'})

        try:
            user = User.objects.get(userAccount=username)
            if user.userPassword != password:
                return render(request, 'jiajiale/login.html', {'errmsg': '密码错误'})
        except User.DoesNotExist as e:
            # return redirect('/login/')
            return render(request, 'jiajiale/login.html', {'errmsg': '用户名不存在'})

        # 登陆成功
        token_int = time.time() + random.randrange(1, 100000)
        user.userToken = str(token_int)
        user.save()

        request.session["account"] = user.userAccount
        request.session["token"] = user.userToken
        return redirect('/main/')
    return render(request, 'jiajiale/login.html')


def register(request):
    # 一旦有POST提交数据，就将其账号数据存到数据库user中
    if request.method == "POST":
        account = request.POST.get("userAccount")
        password = request.POST.get("userPassword")
        mail = request.POST.get("userMail")
        allow = request.POST.get('allow')

        # 判断接受的参数是否都存在
        if not all([account, password, mail]):
            return render(request, 'jiajiale/register.html', {'errmsg': '信息填写不完整'})

        # 校验邮箱格式
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', mail):
            return render(request, 'jiajiale/register.html', {'errmsg': '邮箱格式不正确'})
        # 校验用户是否同意协议
        if allow != 'on':
            return render(request, 'jiajiale/register.html', {'errmsg': '请同意用户协议'})
        try:
            user = User.objects.get(userAccount=account)
        except User.DoesNotExist:
            # 用户名不存在，可以进行注册
            user = None
        if user:
            return render(request, 'jiajiale/register.html', {'errmsg': '用户名已存在，请重试'})

        token_int = time.time() + random.randrange(1, 100000)
        token = str(token_int)
        user = User.createuser(account, password, mail, token)
        user.save()

        request.session["account"] = account
        request.session["token"] = token

        return redirect('/main/')
    else:
        return render(request, 'jiajiale/register.html', {"title": "免费注册"})


#退出登录
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('/main/')


def jsPractice(request):
    return render(request, 'jiajiale/jsPractice.html')