from django.contrib import admin
from .models import StudentDetails
# Register your models here.



@admin.register(StudentDetails)
class AdminStudentDetails(admin.ModelAdmin):
    list_display = ('name' , 'email')