from django.contrib import admin
from django.urls import path
from website.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
    path('addProduct/', addProduct,name='addProduct'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
