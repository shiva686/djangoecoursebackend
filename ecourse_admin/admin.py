from django.contrib import admin

from ecourse_admin.models import adminlogin,websitedetails,addcourse,courses,userlogin,myvid
# Register your models here.

admin.site.register(adminlogin)
admin.site.register(websitedetails)
admin.site.register(addcourse)
admin.site.register(courses)
admin.site.register(userlogin)
admin.site.register(myvid)

