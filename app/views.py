from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Category, Article, Page, TeamMember

# Category Views
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})

class CategoryDetailView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        latest_articles = Article.objects.filter(status='published').order_by('-published_date')[:6]
        articles = category.articles.filter(status='published')
        categories = Category.objects.all().order_by('name')
        return render(request, 'category_detail.html', {'category': category, 'categories': categories, 'articles': articles, 'latest_articles': latest_articles})

# Article Views
class ArticleListView(View):
    def get(self, request):
        articles = Article.objects.filter(status='published')
        latest_articles = Article.objects.filter(status='published').order_by('-published_date')[:6]
        categories = Category.objects.all().order_by('name')
        return render(request, 'article_list.html', {
            'articles': articles,
            'latest_articles': latest_articles,
            'categories': categories,
        })

class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug, status='published')
        article.views_count = (article.views_count or 0) + 1
        article.save(update_fields=['views_count'])
        latest_articles = Article.objects.filter(status='published').exclude(pk=article.pk).order_by('-published_date')[:5]
        from .models import Category
        categories = Category.objects.all().order_by('name')
        return render(request, 'article_detail.html', {
            'article': article,
            'latest_articles': latest_articles,
            'categories': categories,
        })

# Page Views
class PageListView(View):
    def get(self, request):
        pages = Page.objects.filter(status='published').order_by('order', 'title')
        return render(request, 'page_list.html', {'pages': pages})

class PageDetailView(View):
    def get(self, request, slug):
        page = get_object_or_404(Page, slug=slug, status='published')
        from .models import Article, Category
        latest_articles = Article.objects.filter(status='published').order_by('-published_date')[:6]
        categories = Category.objects.all().order_by('name')
        return render(request, 'page_detail.html', {
            'page': page,
            'latest_articles': latest_articles,
            'categories': categories,
        })

class IndexView(View):
    def get(self, request):
        latest_articles = Article.objects.filter(status='published').order_by('-published_date', '-created_at')[:5]
        team_members = TeamMember.objects.all().order_by('jabatan', 'angkatan', 'nama')

        context = {
            'latest_articles': latest_articles,
            'team_members': team_members,
        }

        return render(request, 'index.html', context)
