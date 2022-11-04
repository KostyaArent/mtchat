from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__", "name"]
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Room


admin.site.register(Room, RoomAdmin)
