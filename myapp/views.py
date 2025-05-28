#from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products # Import your specific model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import viewsets, permissions
from .models import Products # Import your model(s)
from .serializers import ProductsSerializer # Import your serializer(s)


class ProductListView(LoginRequiredMixin, ListView):
         model = Products
         template_name = 'myapp/product_list.html' # Optional: Defaults to myapp/yourmodel_list.html
         context_object_name = 'products' # Optional: Defaults to object_list

class ProductDetailView(LoginRequiredMixin, DetailView):
         model = Products
         template_name = 'myapp/product_detail.html' # Optional: Defaults to myapp/yourmodel_detail.html
         # context_object_name defaults to 'object' or 'yourmodel'

class ProductCreateView(LoginRequiredMixin, CreateView):
         model = Products
         template_name = 'myapp/product_form.html' # Optional: Defaults to myapp/yourmodel_form.html
         fields = ['product_name', 'category', 'price'] # Specify fields to include in the form OR use form_class
         success_url = reverse_lazy('myapp:product_list')

def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def get_success_url(self):
        return reverse_lazy('myapp:product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
         model = Products
         template_name = 'myapp/product_form.html' # Can reuse the create form template
         fields = ['category', 'price'] # Specify fields
         success_url = reverse_lazy('myapp:product_list') # Redirect after successful update

         def test_func(self):
                return self.request.user.is_staff

class ProductDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
         model = Products
         template_name = 'myapp/product_confirm_delete.html' # Optional: Defaults to myapp/yourmodel_confirm_delete.html
         success_url = reverse_lazy('myapp:product_list') # Redirect after successful deletion

         def test_func(self):
                return self.request.user.is_staff
         
class ProductsViewSet(viewsets.ModelViewSet):
         """
         API endpoint that allows YourModel objects to be viewed or edited.
         Provides list, create, retrieve, update, partial_update, destroy actions.
         """
         queryset = Products.objects.all().order_by('-id') # Or appropriate ordering
         serializer_class = ProductsSerializer