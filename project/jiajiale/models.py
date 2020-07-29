from django.db import models
from django.utils.html import format_html
# from django.conf import settings


class Wheel(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\wheel",verbose_name='图片')
    redirectUrl = models.CharField(max_length=100,verbose_name='跳转url')
    rankId = models.CharField(max_length=20,verbose_name='等级')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name


class Recommend(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\\recommend",verbose_name='图片')
    redirectUrl = models.CharField(max_length=100,verbose_name='跳转url')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    stockNum = models.IntegerField(verbose_name='库存数量')
    trackId = models.CharField(max_length=20,verbose_name='标记id')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '推荐新品'
        verbose_name_plural = verbose_name


class ClothesType(models.Model):
    typeName = models.CharField(max_length=20, verbose_name='类型名')
    typeId = models.CharField(max_length=20, verbose_name='类型id')
    childTypeNames = models.CharField(max_length=100, verbose_name='子类名')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.typeId
    class Meta:
        verbose_name = '衣服分类'
        verbose_name_plural = verbose_name


class Jacket(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\goods",verbose_name='图片')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    praiseNum = models.IntegerField(verbose_name='好评数')
    briefIntro = models.TextField(max_length=100,verbose_name='简介')
    address = models.CharField(max_length=20,verbose_name='所在地')
    stockNum = models.IntegerField(verbose_name='库存')
    goodsLabel = models.CharField(max_length=20,verbose_name='商品标签')
    sellStatus = models.BooleanField(default=True,verbose_name='出售状态')
    childName = models.CharField(max_length=20, verbose_name='子类名')
    childId = models.CharField(max_length=20, verbose_name='子类id')
    trackId = models.CharField(max_length=20,verbose_name='标记id')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '上衣'
        verbose_name_plural = verbose_name


class Pants(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\goods",verbose_name='图片')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    praiseNum = models.IntegerField(verbose_name='好评数')
    briefIntro = models.TextField(max_length=100,verbose_name='简介')
    address = models.CharField(max_length=20,verbose_name='所在地')
    stockNum = models.IntegerField(verbose_name='库存')
    goodsLabel = models.CharField(max_length=20,verbose_name='商品标签')
    sellStatus = models.BooleanField(default=True,verbose_name='出售状态')
    childName = models.CharField(max_length=20, verbose_name='子类名')
    childId = models.CharField(max_length=20, verbose_name='子类id')
    trackId = models.CharField(max_length=20,verbose_name='标记id')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '下装'
        verbose_name_plural = verbose_name


class Shoes(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\goods",verbose_name='图片')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    praiseNum = models.IntegerField(verbose_name='好评数')
    briefIntro = models.TextField(max_length=100,verbose_name='简介')
    address = models.CharField(max_length=20,verbose_name='所在地')
    stockNum = models.IntegerField(verbose_name='库存')
    goodsLabel = models.CharField(max_length=20,verbose_name='商品标签')
    sellStatus = models.BooleanField(default=True,verbose_name='出售状态')
    childName = models.CharField(max_length=20, verbose_name='子类名')
    childId = models.CharField(max_length=20, verbose_name='子类id')
    trackId = models.CharField(max_length=20,verbose_name='标记id')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '鞋子'
        verbose_name_plural = verbose_name


class Others(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    img = models.ImageField(upload_to="static\images\goods",verbose_name='图片')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    praiseNum = models.IntegerField(verbose_name='好评数')
    briefIntro = models.TextField(max_length=100,verbose_name='简介')
    address = models.CharField(max_length=20,verbose_name='所在地')
    stockNum = models.IntegerField(verbose_name='库存')
    goodsLabel = models.CharField(max_length=20,verbose_name='商品标签')
    sellStatus = models.BooleanField(default=True,verbose_name='出售状态')
    # categoryId = models.ForeignKey("ClothesType",on_delete=models.CASCADE,verbose_name='类型id')  # 关联外键
    childName = models.CharField(max_length=20, verbose_name='子类名')
    childId = models.CharField(max_length=20, verbose_name='子类id')
    trackId = models.CharField(max_length=20,verbose_name='标记id')

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'
    class Meta:
        verbose_name = '其它'
        verbose_name_plural = verbose_name


# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20, unique=True, verbose_name='账号')
    # 密码
    userPassword = models.CharField(max_length=20, verbose_name='密码')
    # 昵称
    userMail = models.EmailField(max_length=50, verbose_name='邮箱')
    # touken验证值，每次登陆之后都会更新
    userToken = models.CharField(max_length=50, verbose_name='token值')
    @classmethod
    def createuser(cls,account,password,mail,token):
        u = cls(userAccount = account,userPassword = password,userMail=mail,userToken=token)
        return u
    class Meta:
        verbose_name = '会员'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.userAccount


class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class Cart(models.Model):
    userAccount = models.CharField(max_length=20, verbose_name='账号')
    trackId = models.CharField(max_length=20, verbose_name='标记id')
    goodsNum = models.IntegerField(verbose_name='商品数量')
    goodsPrice = models.IntegerField(verbose_name='商品价格')
    isChose = models.BooleanField(default=True, verbose_name='是否选择')
    img = models.ImageField(upload_to="static\images\cart", verbose_name='图片')
    name = models.CharField(max_length=20, verbose_name='名称')
    orderId = models.CharField(max_length=20,default="0",verbose_name='订单id')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')
    objects1 = CartManager1()
    objects2 = CartManager2()#用于查看订单的
    @classmethod
    def createcart(cls,userAccount,name,img,trackId,goodsNum,goodsPrice,isChose,isDelete,orderId):
        c = cls(userAccount = userAccount,name = name,img=img,trackId=trackId,goodsNum=goodsNum,goodsPrice=goodsPrice,
                isChose=isChose,isDelete=isDelete,orderId=orderId)
        return c

    def __str__(self):
        return self.name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


class Address(models.Model):
    '''用户收件地址模型类，注意区分字段与Meta中verbose_name不同'''
    user = models.CharField(max_length=20, verbose_name='账号')
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    address = models.CharField(max_length=256, verbose_name='收件地址')
    zipCode = models.CharField(max_length=6,  null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class OrderInfo(models.Model):
    '''订单模型类'''
    PAY_METHOD = {
        1: '货到付款',
        2: '微信支付',
        3: '支付宝',
        4: '银联支付',
    }

    ORDER_STATUS = {
        1: '待支付',
        2: '待发货',
        3: '待收货',
        4: '待评价',
        5: '已完成',
    }

    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付')
    )

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )

    orderId = models.CharField(max_length=128, primary_key=True, verbose_name='订单id') # 订单编号与表主键id不同
    user = models.ForeignKey('User', verbose_name='用户', on_delete=models.CASCADE)
    address = models.CharField(max_length=128, verbose_name='地址')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='订单运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, default='', verbose_name='支付编号') # 支付编号为支付宝等提供
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orderId


class OrderGoods(models.Model):
    '''订单商品模型类'''
    order = models.ForeignKey('OrderInfo', verbose_name='订单', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='名称')
    img = models.ImageField(upload_to="static\images\orderGoods", verbose_name='图片')
    count = models.IntegerField(default=1, verbose_name='商品数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    isDelete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def image_data(self):
        return format_html('<img src="/{}" alt="图片加载失败" width="100px"/>',self.img.url,)
    image_data.short_description = u'图片'

    def __str__(self):
        order = str(self.order)
        return order