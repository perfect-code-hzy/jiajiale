from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20, min_length=5,required=True,error_messages={"required":'用户账号不能为空',
							   "invalid":'格式错误'}, widget=forms.TextInput(attrs={"class":'c'}))
	pswd = forms.CharField(max_length=20,min_length=6,widget=forms.PasswordInput)