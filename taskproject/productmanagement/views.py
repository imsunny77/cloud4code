from ast import Delete
from gettext import install
from django.views.generic import UpdateView, DeleteView, DetailView, ListView
from productmanagement.forms import ProductCategoryForm, ProductManagementForm
from productmanagement.models import Product, ProductCategory
from django.contrib.auth.mixins import LoginRequiredMixin
from productmanagement.serializers import ProductCategorySerializer, ProductSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
class ProductList(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        productmanagement_list = Product.objects.all() 
        return productmanagement_list   

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['form'] = ProductManagementForm()
        return context

class Categories(LoginRequiredMixin, ListView):
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super(Categories, self).get_context_data(**kwargs)
        context['form'] = ProductCategoryForm()
        return context

# class AddCategory(APIView):
#     def post(self, request, format=None, **kwargs):
#         parent_category = request.POST['parent_category']
#         category = request.POST['category']
#         if parent_category=='':
#             ProductCategory.objects.create(
#                 category=category
#             )
#         else:
#             parent_category_obj = ProductCategory.objects.get(pk=parent_category)
#             ProductCategory.objects.create(
#                 parent_category=parent_category_obj,
#                 category=category
#             )  
#         return JsonResponse({'message':'done'}, status= 200)

class CategoryList(APIView):
    def get(self, request, format=None, **kwargs):
        productcategory_list = [] 
        productcategory_list2 = [] 

        for category in ProductCategory.objects.all():
            if category.productcategory_set.all().exists() and category.parent_category is None:
                productcategory_list.append({'category':category.category,'id':category.id})
            elif not category.productcategory_set.all().exists() and category.parent_category is None:
                productcategory_list2.append({'category':category.category,'id':category.id})

        return JsonResponse({"productcategory_list": productcategory_list,'productcategory_list2':productcategory_list2})
        
class SubCategoryList(APIView):
    def get(self, request, format=None, **kwargs):
        id = kwargs['current_id']
        sub_category_list=[]
        for sub_cat in ProductCategory.objects.filter(parent_category__id=id):
            if sub_cat.productcategory_set.all().exists():
                sub_category_list.append({'category':sub_cat.category,'id':sub_cat.id, 'is_parent':'dropdown-toggle'})  
            else:
                sub_category_list.append({'category':sub_cat.category,'id':sub_cat.id, 'is_parent':''})  

        return JsonResponse({"sub_category_list": sub_category_list})
        
class ProductCategoryViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

    def list(self, request):
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        parent_category = request.POST['parent_category']
        category = request.POST['category']
        if parent_category=='':
            ProductCategory.objects.create(
                category=category
            )
        else:
            parent_category_obj = ProductCategory.objects.get(pk=parent_category)
            ProductCategory.objects.create(
                parent_category=parent_category_obj,
                category=category
            )  
        return JsonResponse({'message':'done'}, status= 200)

    def update(self, request, pk=None):
        parent_category = request.POST['parent_category']
        category = request.POST['category']
        category_obj = ProductCategory.objects.get(pk=pk)
        if parent_category=='':
            category_obj.category=category
            category_obj.save()
        else:
            parent_category_obj = ProductCategory.objects.get(pk=parent_category)
            category_obj.category=category
            category_obj.parent_category=parent_category_obj
            category_obj.save()
        return JsonResponse({'message':'done'}, status= 200)

    def destroy(self, request, pk=None):
        category_obj = ProductCategory.objects.get(pk=pk)
        category_obj.delete()
        return JsonResponse({'message':'done'}, status= 200)

class ProductViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'done'}, status= 200)
    
    def update(self, request, pk=None):
        product_name= request.POST['product_name']
        product_category= request.POST['product_category']
        # feature_image= request.POST['feature_image']
        description= request.POST['description']
        category_obj = ProductCategory.objects.get(pk=product_category)
        product_obj = Product.objects.get(pk=pk)
        product_obj.product_name=product_name
        product_obj.product_category=category_obj
        # product_obj.feature_image=feature_image
        product_obj.description=description
        product_obj.save()
        return JsonResponse({'message':'done'}, status= 200)

    def destroy(self, request, pk=None):
        product_obj = Product.objects.get(pk=pk)
        product_obj.delete()
        return JsonResponse({'message':'done'}, status= 200)