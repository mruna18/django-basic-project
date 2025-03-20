from django.contrib import admin
from base.models import ArticleData,NewsData,EventsData

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display=['title','desc']  

  list_display_links=['title']
  ordering=['id']
 

admin.site.register(ArticleData,ArticleAdmin)


class NewsAdmin(admin.ModelAdmin):
  list_display=['title','author','date','content']  
  ordering=['id']
admin.site.register(NewsData,NewsAdmin)


class EventsAdmin(admin.ModelAdmin):
  list_display=['name','date','location','type']
  ordering=['id']
admin.site.register(EventsData,EventsAdmin)
