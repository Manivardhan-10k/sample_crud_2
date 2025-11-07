from django.urls  import path 
from . import  views


urlpatterns=[
    path("welcome/",view=views.welcome),
    path("reg_user/",view=views.reg_user),
    path("user_list/",view=views.users),
    path("remove/<int:uid>",view=views.delete_user),
    path("update/<int:uid>",view=views.update_user)
]