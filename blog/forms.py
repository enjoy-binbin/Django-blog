from django import forms

from .models import Article, Comment, GuestBook


class ArticleAdminForm(forms.ModelForm):
    """
    admin管理form, 在content基础上添加 pagedown作为md编辑器
    注释掉content了现在在正文里使用 mdeditor作为md编辑器
    """

    # from pagedown.widgets import AdminPagedownWidget
    # content = forms.CharField(widget=AdminPagedownWidget)

    class Meta:
        model = Article
        fields = '__all__'


# Meta中使用fields, 将Model中的字段，对应转化成form字段, 可以在Meta中用 widgets指定 fields里元素对应的 widget
# Form中属性, 补充Model中没有的字段到前端表单, 和 覆盖 Model中的 同名Field的定义
# 在init里用 self.fields[key] 可以最终操作到前端
# ModelForm中 元Meta中的 fields, 和Model 相关联，可以进行save操作写入Model
class CommentForm(forms.ModelForm):
    """ 前端评论框form """
    name = forms.CharField(label='名称', required=True, widget=forms.HiddenInput)
    email = forms.EmailField(label='邮箱', required=True, widget=forms.HiddenInput)
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        # 可以根据model里的field转换成form的field
        fields = ['content']


class GuestBookForm(forms.ModelForm):
    """ 前端留言板form """
    class Meta:
        model = GuestBook
        fields = ['content']
