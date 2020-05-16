from django.contrib import admin
from .models import UserDetails

# Register your models here.

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','mobile_num','level','course','date_posted')
    
    
admin.site.register(UserDetails,UserDetailsAdmin)
