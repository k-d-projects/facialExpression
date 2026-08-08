from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views 
from myapp import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [

    path("",views.index,name="myapp"),
    path("index",views.index,name="index"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("contactus",views.contactus,name="contactus"),
    path("signup",views.handlesignup,name="handlesignup"),
    path("login",views.handlelogin,name="handlelogin"),
    
    path("changepassword",views.changepass,name="changepass"),
    path("logout",views.handlelogout,name="handlelogout"),
    path('opencamero',views.opencamero,name="script"),
    path('photoviewes',views.svimg,name="photoviewes"),
    path('viewimg',views.viewimg,name="viewimg"),
    path('delete/<int:id>', views.destroy,name="delete"),
    path('export_users_csv/', views.export_users_csv),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
