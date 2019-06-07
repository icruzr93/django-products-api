from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/products/(?P<pk>[0-9]+)$',
        views.get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/products/$',
        views.get_post_products,
        name='get_post_products'
    )
]
