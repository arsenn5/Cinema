from django.urls import path
from .views import (
    IndexView,
    ProductsByTagMaleView,
    ProductsByTagFemaleView,
    ProductsByTagChildrenView,
    ProductsByTagUniversalView,
    CreateOrderView,
)

app_name = 'cloth'

urlpatterns = [
    path('cloth/', IndexView.as_view(), name='index'),
    path('products/by_tag/male', ProductsByTagMaleView.as_view(), name='products_by_tag_male'),
    path('products/by_tag/female', ProductsByTagFemaleView.as_view(), name='products_by_tag_female'),
    path('products/by_tag/children', ProductsByTagChildrenView.as_view(), name='products_by_tag_children'),
    path('products/by_tag/universal', ProductsByTagUniversalView.as_view(), name='products_by_tag_universal'),
    path('create_order', CreateOrderView.as_view(), name='create_order'),
]
