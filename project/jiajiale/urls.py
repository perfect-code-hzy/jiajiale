from django.conf.urls import url
app_name='[jiajiale]'
from . import views

urlpatterns = [
	# url(r'^', views.index, name='index'),
	url(r'^main/$', views.main, name='main'),
	url(r'^detail/(\d+)/(\d+)/$', views.detail, name='detail'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^cartAdd/$', views.cartAdd, name='cartAdd'),
	url(r'^changeCart/(\d+)/$', views.changeCart, name='changeCart'),
	url(r'^userInfo/$', views.userInfo, name='userInfo'),
	url(r'^userOrder/(\d+)/$', views.userOrder, name='userOrder'),
	url(r'^userAddress/$', views.userAddress, name='userAddress'),

	url(r'^saveOrder/$', views.saveOrder, name='saveOrder'),
	url(r'^orderCommit/$', views.orderCommit, name='orderCommit'),

	url(r'^login/$', views.login, name="login"),
	url(r'^register/$', views.register, name='register'),
	url(r'^quit/$', views.quit, name='quit'),


	url(r'^jsPractice/$', views.jsPractice, name='jsPractice'),
]