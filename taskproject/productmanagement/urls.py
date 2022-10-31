from django.urls import path
from productmanagement import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category-api', views.ProductCategoryViewset, basename='category_api')
router.register(r'product-api', views.ProductViewset, basename='product_api')


app_name = 'productmanagement'

urlpatterns = [
    path('product-management/', views.ProductList.as_view(), name='product_list'),
    # path('add-category/', views.AddCategory.as_view(), name='add_category'),
    path('all-category/', views.CategoryList.as_view(), name='category_list'),
    path('sub-category/<str:current_id>/', views.SubCategoryList.as_view(), name='sub_category_list'),
    path('categories/', views.Categories.as_view(), name='categories'),

] + router.urls
