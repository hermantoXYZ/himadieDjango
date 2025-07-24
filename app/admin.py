from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldAdmin
from .models import Page, Article, Category, TeamMember
from django import forms
from tinymce.widgets import TinyMCE


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

class PageAdminForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

@admin.register(Category)
class CategoryAdmin(UnfoldAdmin):
    list_display = ('name', 'slug', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'slug', 'description')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)

@admin.register(TeamMember)
class TeamMemberAdmin(UnfoldAdmin):
    list_display = ('nama', 'angkatan', 'jabatan', 'image')
    search_fields = ('nama', 'angkatan', 'jabatan')
    ordering = ('angkatan', 'jabatan')

@admin.register(Article)
class ArticleAdmin(UnfoldAdmin):
    form = ArticleAdminForm
    list_display = ('title', 'author', 'category', 'status', 'views_count')
    search_fields = ('title', 'slug', 'author__username', 'category__name', 'content', 'excerpt')
    list_filter = ('status', 'category', 'author', 'published_date')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date', '-created_at')

@admin.register(Page)
class PageAdmin(UnfoldAdmin):
    form = PageAdminForm
    list_display = ('title', 'author', 'status', 'order', 'created_at')
    search_fields = ('title', 'slug', 'author__username', 'content')
    list_filter = ('status', 'author')
    prepopulated_fields = {"slug": ("title",)}
    ordering = ('order', 'title')