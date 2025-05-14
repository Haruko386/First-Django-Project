from django.contrib import admin

from app01.models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title',)


admin.site.register(Article, ArticleAdmin)
