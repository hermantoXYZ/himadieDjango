from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    ArticleListView, ArticleDetailView,
    PageListView, PageDetailView,
    IndexView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

    # Article URLs
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),

    # Page URLs
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
] 