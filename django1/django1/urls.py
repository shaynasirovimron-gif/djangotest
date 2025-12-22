
from django.contrib import admin
from django.urls import path
from core.views import test, test2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test), 
    path('custom/', test2)
]
