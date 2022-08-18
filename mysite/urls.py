"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
 
from News.views import welcome ,signup,detail,addfav,deletefav,myfavorit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='index'),
    path('', welcome, name='home'),
    path('myfavorit', myfavorit, name='myfavorit'), 
    path('article', welcome, name='home'),
    path('<int:id>', detail, name='detail'),
    path('article/<int:id>', detail, name='detail'),
    path('addfav/<int:id>', addfav, name='addfav'),
    path('deletefav/<int:id>', deletefav, name='deletefav'),
     
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup', signup, name='signup'),
   # path('accounts/',name='login'),# include('django.contrib.auth.urls')),
   # path('accounts/',auth.urls),# include('django.contrib.auth.urls')),
    
]
#The urls provided by this are
#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']