from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User   #设置表单的模型
        fields=('username','email')     #指定表单要显示的字段，指定字段在模板中会渲染成表单控件，密码和确认密码默认控件。