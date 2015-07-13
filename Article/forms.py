#coding=utf-8

from django import forms
from Article.models import Article

class editArticleForm(forms.ModelForm):
    '''编辑文章表单'''
    class Meta:
        model = Article
        fields = ('title', 'group', 'content', 'tags', 'author')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'group' : forms.TextInput(attrs={'class':'form-control'}),
            #'instime' : forms.DateTimeInput(attrs={'class':'form-control'}),
            #'uptime' : forms.DateTimeInput(attrs={'class':'form-control'}),
            'content' : forms.TextInput(attrs={'class':'list-inline'}),
            'tags' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super(editArticleForm,self).__init__(*args,**kwargs)
        self.fields['title'].label=u'标 题'
        self.fields['content'].label=u'正 文'
        self.fields['content'].error_messages={'required':u'请输入文章正文'}
        # self.fields['group'].error_messages={'required':u'请输入分组'}
        #self.fields['instime'].label=u'插入时间'
        # self.fields['email'].label=u'邮 箱'
        # self.fields['email'].error_messages={'required':u'请输入邮箱','invalid':u'请输入有效邮箱'}
        # self.fields['nickname'].label=u'姓 名'
        # self.fields['nickname'].error_messages={'required':u'请输入姓名'}
        # self.fields['sex'].label=u'性 别'
        # self.fields['sex'].error_messages={'required':u'请选择性别'}
        # self.fields['role'].label=u'角 色'
        # self.fields['is_active'].label=u'状 态'
