#coding=utf-8

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.core.urlresolvers import reverse
from website.common.CommonPaginator import SelfPaginator

from Article.models import Article
from Article.forms import editArticleForm
import logging


logger = logging.getLogger(__name__)

def articlePreshow(request, artid):
    '''预览文章'''
    article = Article.objects.get(pk=int(artid))
    if article:
        kwvars = {
            'article': article,
            'request': request,
        }
        return render_to_response('Article/article.show.html', kwvars, RequestContext(request))

    return HttpResponseRedirect(reverse('adminartlisturl'))

