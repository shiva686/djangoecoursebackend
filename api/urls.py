
from django.urls import path
from . import views;

urlpatterns = [
   path('api/adminlogin',views.adminlogin.as_view()),
   path('api/admin/changepassword',views.Adminchangepassword.as_view()),
   path('api/admin/websitedetails',views.Adminwebsitedetails.as_view()),
   path('api/admin/addcourses',views.Adminaddcourses.as_view()),
   path('api/admin/courses',views.courses.as_view()),
   path('api/admin/homecourses',views.limitcourses.as_view()),
   path('api/admin/deletecourse',views.delcourse.as_view()),
   path('api/admin/logout',views.logout.as_view()),
   path('api/admin/authlogin',views.auth.as_view()),
   path('api/usersignin',views.userSignin.as_view()),
   path('api/usersignup',views.userSignup.as_view()),
   path('api/userchangepassword',views.userchangepassword.as_view()),
   path('api/profile',views.userprofile.as_view()),
   path('api/user/authentication',views.userAuth.as_view()),
   path('api/deleteuser',views.deleteuser.as_view()),
   path('api/mycourse',views.mycourses.as_view()),
   path('api/buycourse',views.selectedcourse.as_view()),
   path('api/websitedetails',views.websitedetails.as_view()),
   path('api/admin_students_list',views.admin_students_list.as_view()),
]
