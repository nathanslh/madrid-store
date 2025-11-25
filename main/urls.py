from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user, edit_product, delete_product, create_product_ajax
from main.views import edit_product_ajax, delete_product_ajax, proxy_image, create_product_flutter
from main.views import show_products_flutter, show_my_products_flutter, logout_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<str:id>/', edit_product, name='edit_product'),
    path('delete-product/<str:id>/', delete_product, name='delete_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<str:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('products-flutter/', show_products_flutter, name='show_products_flutter'),
    path('my-products-flutter/', show_my_products_flutter, name='show_my_products_flutter'),
    path('logout-flutter/', logout_flutter, name='logout_flutter'),
]