"""UnicornAttractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import homepage
from issue_tracker import urls as urls_tracker
from user_authentication import urls as urls_user
from user_profile import urls as urls_profile
from checkout import urls as urls_checkout
from dashboard import urls as urls_dashboard
from games import urls as urls_games

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='index'),
    ## url(r'^about/$', aboutpage, name='about'),
    url(r'^tracker/', include(urls_tracker)),
    url(r'^accounts/', include(urls_user)),
    url(r'^profile/', include(urls_profile)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^dashboard/', include(urls_dashboard)),
    url(r'^games/', include(urls_games)),
]
