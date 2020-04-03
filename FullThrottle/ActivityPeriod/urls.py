from django.urls import path
from ActivityPeriod import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('getName/', views.getName, name = 'name'),
    path('Users/', views.Users, name = 'Users'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
