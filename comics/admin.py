from engineered.comics.models import Strip
from django.contrib import admin

class StripAdmin(admin.ModelAdmin):
    fields = ['sub_date', 'title', 'alt_text', 'strip']
    list_filter = ['sub_date']
    search_fields = ['title']
    date_hierarchy = 'sub_date'

    list_display = ('__unicode__', 'sub_date', 'title')

admin.site.register(Strip, StripAdmin)
