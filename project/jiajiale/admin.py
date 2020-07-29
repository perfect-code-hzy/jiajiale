from django.contrib import admin


# Register your models here.
from .models import Wheel,Recommend,ClothesType,Jacket,Pants,Shoes,Others,User,Cart,Address,OrderInfo,OrderGoods

@admin.register(Wheel)
class WheelAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'name',
	list_filter = 'rankId',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','redirectUrl','rankId',isDelete]
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'name',
	list_filter = 'trackId',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','goodsPrice','stockNum','redirectUrl','trackId',isDelete]
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(ClothesType)
class ClothesTypeAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'typeName',
	list_filter = 'typeId',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ['typeName','typeId',"childTypeNames",isDelete]
	list_per_page = 5
	fieldsets = [
		(None,{'fields': ['typeName','typeId']}),
		('详细信息', {'fields': ['childTypeNames','isDelete']}),
	]


@admin.register(Jacket)
class JacketAdmin(admin.ModelAdmin):
	def sellStatus(self):
		if self.sellStatus:
			return "出售中"
		else:
			return "暂停销售"
	sellStatus.short_description = "出售状态"
	search_fields = 'name','goodsLabel','briefIntro',
	list_filter = 'childName','address',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','goodsPrice','praiseNum','briefIntro','address','stockNum',
					'goodsLabel','sellStatus','childName','childId','trackId']
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(Pants)
class PantsAdmin(admin.ModelAdmin):
	def sellStatus(self):
		if self.sellStatus:
			return "出售中"
		else:
			return "暂停销售"
	sellStatus.short_description = "出售状态"
	search_fields = 'name','goodsLabel','briefIntro',
	list_filter = 'childName','address',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','goodsPrice','praiseNum','briefIntro','address','stockNum',
					'goodsLabel','sellStatus','childName','childId','trackId']
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
	def sellStatus(self):
		if self.sellStatus:
			return "出售中"
		else:
			return "暂停销售"
	sellStatus.short_description = "出售状态"
	search_fields = 'name','goodsLabel','briefIntro',
	list_filter = 'childName','address',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','goodsPrice','praiseNum','briefIntro','address','stockNum',
					'goodsLabel','sellStatus','childName','childId','trackId']
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(Others)
class OthersAdmin(admin.ModelAdmin):
	def sellStatus(self):
		if self.sellStatus:
			return "出售中"
		else:
			return "暂停销售"
	sellStatus.short_description = "出售状态"
	search_fields = 'name','goodsLabel','briefIntro',
	list_filter = 'childName','address',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','goodsPrice','praiseNum','briefIntro','address','stockNum',
					'goodsLabel','sellStatus','childName','childId','trackId']
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["userAccount",'userPassword','userMail','userToken']
	list_per_page = 5


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	def isChose(self):
		if self.isChose:
			return "是"
		else:
			return "否"
	isChose.short_description = "是否选中"
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'name',
	list_filter = 'goodsPrice',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ["name",'image_data','trackId','goodsNum','goodsPrice',isChose,'orderId',
					isDelete,'userAccount']
	list_per_page = 5
	readonly_fields = ('image_data',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'address',
	list_filter = 'user',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ['receiver','user',"address",'zipCode','phone',isDelete]
	list_per_page = 5


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'address',
	list_filter = 'user',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ['orderId','user',"address",'pay_method','total_count','total_price','transit_price','order_status',
					'trade_no','create_time','update_time',isDelete]
	list_per_page = 5


@admin.register(OrderGoods)
class OrderGoodsAdmin(admin.ModelAdmin):
	def isDelete(self):
		if self.isDelete:
			return "√"
		else:
			return "×"
	isDelete.short_description = "是否删除"
	search_fields = 'order',
	list_filter = 'name',
	# 执行动作位置
	actions_on_bottom = True
	actions_on_top = False
	list_display = ['order','name','image_data',"count",'price',isDelete]
	list_per_page = 5
	readonly_fields = ('image_data',)