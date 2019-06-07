from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls))
    url(r'^', include('products.urls')),
]
