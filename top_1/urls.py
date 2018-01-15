"""top_1 URL Configuration

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
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from app import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'top_1'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('app.urls')),
    url(r'^login/$', login, {'template_name': 'app/login.html'}),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^update/$', views.update, name='update'),
    url(r'^change-password/$', views.cp, name='cp'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^dashboard',views.dashboard,name='dashboard'),
    url(r'^problems',views.problems,name='problems'),
    url(r'^contest', views.contest, name='contest'),
    url(r'^leaderboard', views.leaderboard, name='leaderboard'),
    url(r'^contribute', views.contribute, name='contribute'),
    url(r'^statistics', views.statistics, name='statistics'),
    url(r'^discuss', views.discuss, name='discuss'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

