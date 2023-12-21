from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about,name="about"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.user_logout,name="logout"),
    path('signup/',views.user_signup,name="signup"),
    path('login/',views.user_login,name="login"),
    path('addblog/',views.add_blog,name='addblog'),
    path('updateblog/<int:id>/',views.update_blog,name="updateblog"),
    path('deleteblog/<int:id>/',views.delete_blog,name="deleteblog"),
]
