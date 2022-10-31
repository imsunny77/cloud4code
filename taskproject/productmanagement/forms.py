from urllib import request
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Div


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['parent_category','category',]
        widgets = {
            'category': forms.TextInput(attrs={'style':"text-transform: capitalize;"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<h4>Add Product category</h4>"),
            Row(
                Column('parent_category', css_class='form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        )

class ProductManagementForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'price','feature_image','description',]

        widgets = {
            'product_name': forms.TextInput(attrs={'style':"text-transform: capitalize;"}),
            'description': forms.Textarea(attrs={'rows': '3'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<h4>Add Product</h4>"),
            HTML('<hr>'),

            Row(Column('product_name', css_class='form-group col-md-6 mb-0 make_caps'),
                Column('product_category', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),
            
            Row(Column('feature_image', css_class='form-group col-md-6 mb-0 make_caps'),
                Column('price', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'),

            Row(Column('description', css_class='form-group col-md-12 mb-0 make_caps'),
                css_class='form-row'),
            )

