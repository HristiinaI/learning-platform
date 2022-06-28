from django.urls import path
from . import views
from mysite import settings 
from django.conf.urls.static import static
#from django.conf import settings

app_name = "main"

urlpatterns = [
    path('', views.homepage, name = "homepage"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)