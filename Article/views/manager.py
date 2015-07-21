#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.core.urlresolvers import reverse
from website.common.CommonPaginator import SelfPaginator

from Article.models import Article
from Article.forms import editArticleForm
import logging


logger = logging.getLogger(__name__)

def adminArticleList(request):
    '''管理后台 文章列表'''
    logger.info('show article list ...')
    articles = Article.objects.all()
    #分页功能
    lst = SelfPaginator(request, articles, 5)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('Article/admin.article.list.html', kwvars, RequestContext(request))

def editArticle(request):
    '''edit'''
    if request.method == "POST":
        form = editArticleForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(form.cleaned_data)
            return HttpResponseRedirect(reverse('adminartlisturl'))

    else:
        form = editArticleForm()

    kwvars = {
        'form' : form,
        'request' : request,
    }

    return render_to_response('Article/admin.edit.article.html', kwvars, RequestContext(request))

def delArticle(request, artid):
	'''del article'''
	article = Article.objects.get(pk=int(artid))
	if article:
		article.delete()

	return HttpResponseRedirect(reverse('adminartlisturl'))

