from django.urls import path
from .import views
from blog.views import RSSFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('archives/',views.archives,name='archives'),
    path('aboutme/',views.about_me,name="about_me"),
    path('^tag(?P<tag>\w+)/$',views.search_tag,name="search_tag"),
    path('search/',views.blog_search,name='search'),
    path('feed/',RSSFeed(),name="RSS"),
]

