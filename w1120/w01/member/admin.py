from django.contrib import admin
from member.models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']

admin.site.register(Member)