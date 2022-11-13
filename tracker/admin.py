from django.contrib import admin

# Register your models here.

from .models import ChoreEvent, Family, Dog

# admin.site.register(ChoreEvent)
admin.site.register(Family)
admin.site.register(Dog)

@admin.register(ChoreEvent)
class ChoreEventAdmin(admin.ModelAdmin):
    """Administration object for ChoreEvent models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('type', 'dog', 'care_giver', 'timestamp')