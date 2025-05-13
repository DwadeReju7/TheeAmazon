#from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products # Import your specific model

class ProductListView(ListView):
         model = Products
         template_name = 'myapp/product_list.html' # Optional: Defaults to myapp/yourmodel_list.html
         context_object_name = 'products' # Optional: Defaults to object_list

class ProductDetailView(DetailView):
         model = Products
         template_name = 'myapp/product_detail.html' # Optional: Defaults to myapp/yourmodel_detail.html
         # context_object_name defaults to 'object' or 'yourmodel'

class ProductCreateView(CreateView):
         model = Products
         template_name = 'myapp/product_form.html' # Optional: Defaults to myapp/yourmodel_form.html
         fields = ['product_name', 'category', 'price'] # Specify fields to include in the form OR use form_class
         success_url = reverse_lazy('myapp:product_list')

def get_success_url(self):
        return reverse_lazy('myapp:product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(UpdateView):
         model = Products
         template_name = 'myapp/product_form.html' # Can reuse the create form template
         fields = ['category', 'price'] # Specify fields
         success_url = reverse_lazy('myapp:product_list') # Redirect after successful update

class ProductDeleteView(DeleteView):
         model = Products
         template_name = 'myapp/product_confirm_delete.html' # Optional: Defaults to myapp/yourmodel_confirm_delete.html
         success_url = reverse_lazy('myapp:product_list') # Redirect after successful deletion