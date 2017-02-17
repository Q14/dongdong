"""dongdong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from article.views import AboutView
from article.views import ArchiveView
from article.views import BlogsWithCategoryView
from article.views import BlogListView
from article.views import LatestPosts
from article.views import TagsView
from article.views import CategoriesView
from article.views import BlogsWithTagView
from dongdong.sitemaps import BlogSitemap, IndexSitemap

admin.autodiscover()

sitemaps = {
    'index': IndexSitemap,
    'blog': BlogSitemap,

}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BlogListView.as_view(), name="home"),
    url(r'^blog/', include('article.urls', namespace='article')),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^404', TemplateView.as_view(template_name="404.html")),


    url(r"^tag/(?P<tag_name>[\w,-]+)$", BlogsWithTagView.as_view(), name="tag"),
    url(r"^category/(?P<pk>\d+)/(?P<cat_name>\w+)$", BlogsWithCategoryView.as_view()),
    url(r"^tags$", TagsView.as_view(), name="tag_list"),
    url(r"^categories$", CategoriesView.as_view(), name="category_list"),
    url(r"^archives", ArchiveView.as_view(), name="archives"),

    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^humans.txt$', TemplateView.as_view(template_name="humans.txt", content_type="text/plain")),
    url(r'^rss/', LatestPosts(), name='feeds'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
