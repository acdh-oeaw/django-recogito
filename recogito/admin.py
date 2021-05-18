from django.contrib import admin

from . models import RecogitoAnnotation


@admin.register(RecogitoAnnotation)
class RecogitoAnnotationAdmin(admin.ModelAdmin):
    list_display = (
        "re_text",
        "re_id",
        "re_app",
        "re_model",
        "re_field_name"
    )
    list_filter = (
        "re_app",
        "re_model",
        "re_field_name",
    )
    search_fields = [
        're_text'
    ]
