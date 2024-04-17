from django.contrib import admin
from .models import contact_form
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(contact_form)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('reason', 'email', 'subject', 'submission_date', 'message')
