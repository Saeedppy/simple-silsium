from django.contrib import admin
from .models import Article,Category,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','slug','parent','status',)
    list_filter=(['status'])
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}
    

# Register your models here.
admin.site.register(Category,CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','slug','publish','status','category_to_str')
    list_filter=('publish','status')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering=['-status','publish']

    def category_to_str(self,obj):
        return " , ".join([category.title for category in obj.category_published()])


# Register your models here.
admin.site.register(Article,ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','body','article','created','active')
    list_filter=('created',)
    list_editable=('active',)
admin.site.register(Comment,CommentAdmin)



