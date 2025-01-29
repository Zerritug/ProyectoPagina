
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HomePage/', include('HomePage.urls')),
    
    path("__reload__/", include("django_browser_reload.urls")), #esto no lo vaya a tocar, aqui se cargan las cosas de django para refrescar dentro del buscador y eso todo bien :3
    
]
