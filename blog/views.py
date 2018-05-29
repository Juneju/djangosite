from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Article
from django.http import Http404
from django.test.utils import tag
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger  #分页功能
from django.core.paginator import Page

#首页
def index(request):
    posts=Article.objects.all()
    paginator=Paginator(posts,2)  #分页，每页显示两片文章
    page=request.GET.get('page')
    try:
        post_list=paginator.page(page)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'index.html',{'post_list':post_list})

def detail(request,id):
#     response="You're looking at the results of question %s."
#     return HttpResponse(response %id)
    try:
        post=Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

#归档功能
def archives(request):
    try:
        post_list=Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,'error':False})

#关于我
def about_me(request):
    return render(request,'aboutme.html')



def search_tag(request):
    try:
        post_list=Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})


#搜索功能
def blog_search(request):
    if 's' in request.GET:
        s=request.GET['s'];
        if not s:
            return render(request,'index.html');
        else:
            post_list=Article.objects.filter(title__icontains=s)
            if len(post_list)==0:
                return render(request,'archives.html',{'post_list':post_list,'error':True})
            
            else:
                return render(request,'archives.html',{'post_list':post_list,'error':False})
    
    return redirect('/')


#RSS功能
class RSSFeed(Feed):
    title="RSS feed - article"
    link="feeds/posts/"
    description="RSS feed -blog posts"
    
    def items(self):
        return Article.objects.order_by('-date_time')
    
    def item_title(self,item):
        return item.title
    
    def item_pubdate(self,item):
        return item.date_time
    
    def item_description(self,item):
        return item.content
    









