from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, ImageProduct, Category, Branding, Tags
from django.db.models import Q
from taggit.models import Tag
from cart.forms import CartAddProductForm
from django.views.generic.edit import FormMixin


class ShopListView(ListView):
    model = Product
    paginate_by= 12
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super(ShopListView, self).get_queryset()
        queryset = queryset.all()
        f = self.kwargs.get('slug')
        if f:
            queryset = queryset.filter(Q(category__slug=f) | Q(branding__slug = f))           
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['branding'] = Branding.objects.all()
        context['tags'] = Tag.objects.all()
        return context
    

class ShopDetailView(FormMixin,DetailView):
    model = Product
    context_object_name = 'product'
    form_class = CartAddProductForm

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        context['img'] = ImageProduct.objects.filter(product=self.get_object())
        context['tags'] = Tag.objects.filter(tags__product=self.get_object())
        context['related'] = Product.objects.filter(category=self.get_object().category)
        return context
