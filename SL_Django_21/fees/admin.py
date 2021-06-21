from django.contrib import admin
from fees.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display=('name','mail')
 
admin.site.register(Student,StudentAdmin) 