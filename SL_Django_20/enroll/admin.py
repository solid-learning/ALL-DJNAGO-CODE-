from django.contrib import admin
from enroll.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display=('id','stuid','stuname','stuemail','stucollage','stustate')
 
admin.site.register(Student,StudentAdmin) 