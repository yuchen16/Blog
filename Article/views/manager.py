#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext

from Article.models import Article
from Article.forms import editArticleForm



def adminArticleList(request):
    '''管理后台 文章列表'''
    articles = Article.objects.all()

    return render_to_response('Article/admin.article.list.html', locals(), RequestContext(request))

def editArticle(request):
    '''edit'''
    if request.method == "POST":
        forms = editArticleForm(request.POST)
        if forms.is_valid():
            froms.save()
            return HttpResponseRedirect(reverse('adminartlisturl'))

    else:
        forms = editArticleForm()

    kwvars = {
        'forms' = forms,
        'request' = request,
    }

    return render_to_response('Article/admin.edit.article.html', kwargs, RequestContext(request))