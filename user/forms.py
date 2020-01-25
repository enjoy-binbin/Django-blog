from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import widgets


def email_unique_validate(email):
    """ 验证邮箱是否已被注册 """
    user = get_user_model().objects.filter(email=email).first()
    if user:
        # raise ValidationError('该邮箱已注册')
        pass


# Meta中使用fields, 将Model中的字段，对应转化成form字段, 可以在Meta中用 widgets指定 fields里元素对应的 widget
# Form中属性, 补充Model中没有的字段到前端表单, 和 覆盖 Model中的 同名Field的定义
# 在init里用 self.fields[key] 可以最终操作到前端
# ModelForm中 元Meta中的 fields, 和Model 相关联，可以进行save操作写入Model

class RegisterForm(UserCreationForm):
    """ 注册form 继承UserCreationForm"""

    # 在init里指定widget, 这样 ModelForm就可以根据 Model, 生成对应的field，会自动根据model，设置 max_length， required等
    # username = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'placeholder': 'Username',
    #         'class': 'form-control'
    #     }))
    email = forms.EmailField(required=True, validators=(email_unique_validate,))

    # email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 只修改widget
        self.fields['username'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'style': 'margin-bottom: 10px'
            })
        self.fields['email'].widget = widgets.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            })
        self.fields['password1'].widget = widgets.PasswordInput(
            attrs={
                'placeholder': 'New password',
                'class': 'form-control'
            })
        self.fields['password2'].widget = widgets.PasswordInput(
            attrs={
                'placeholder': 'Repeat password',
                'class': 'form-control'
            })

    def clean_email(self):
        """
        判断邮箱是否已经注册, 如果和validators一起用了
        会先执行validators, 通过后才会到这里, 如果上面先抛出异常, 这里就不会执行了
        """
        email = self.cleaned_data.get('email')
        user = get_user_model().objects.filter(email=email).first()
        if user:
            raise ValidationError('该邮箱已注册.')
        else:
            return email

    class Meta:
        model = get_user_model()  # UserProfile
        # 使用了 model里的 username 和 email, UserCreationForm里继承有 password1,password2
        fields = ("username", "email")


class LoginForm(AuthenticationForm):
    """ 登陆form，继承AuthenticationForm """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'style': 'margin-bottom: 10px',
                'autofocus': True
            })
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
