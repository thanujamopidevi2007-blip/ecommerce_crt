from django.urls import path
from .views import add_product, view_all_product, delete_by_id, add_to_cart,delete_from_cart

urlpatterns=[
    path("add",add_product),
    path("view",view_all_product),
    path("delete_by_id/<int:id>",delete_by_id,name="delete_by_id"),
    path("add_to_cart/<int:id>",add_to_cart),
    path("delete_from_cart/<int:id>",delete_from_cart),

]