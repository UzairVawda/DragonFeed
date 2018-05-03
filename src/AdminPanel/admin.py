from django.contrib import admin
from models import Article

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["Title", "Start", "End"]
    list_display_links = None
    list_filter = ["Tag"]
    search_fields = ["Tag"]
    
    class Meta:
        model = Article

admin.site.register(Article, ArticleModelAdmin)

