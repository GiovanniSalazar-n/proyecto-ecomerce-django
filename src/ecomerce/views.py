from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render , get_object_or_404
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect

from .forms import ProductModelForm
from .models import ProductModel
# Create your views here.
def product_model_create_view(request):
    form= ProductModelForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Producto crerado con exito")
        return HttpResponseRedirect("/ecomerce/{product_id}".format(product_id=instance.id))
    context={
        "form":form
    }
    template="ecomerce/create-view.html"
    return render(request,template,context)

def product_model_detail_view(request,product_id):
    instance = get_object_or_404(ProductModel,id=product_id)
    context={
        "product":instance
    }
    template ="ecomerce/detail-view.html"
    return render(request,template,context)

def product_model_delete_view(request,product_id):
    instance = get_object_or_404(ProductModel,id=product_id)
    if request.method == "POST":
        instance.delete()
        HttpResponseRedirect("/ecomerce/")
        messages.success(request,"producto eliminado")
        return HttpResponseRedirect("/ecomerce/")
    context={
        "product":instance
    }
    template ="ecomerce/delete-view.html"
    return render(request,template,context)

def product_model_update_view(request,product_id=None):
    instance = get_object_or_404(ProductModel,id=product_id)
    form=ProductModelForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Producto actualizado con exito")
        return HttpResponseRedirect("/ecomerce/{product_id}".format(product_id=instance.id))
    context={
        "form":form
    }
    template="ecomerce/update-view.html"
    return render(request,template,context)



#@login_required aun no se usara 
def product_model_list_view(request):
    print(request.user)
    query= request.GET.get("q",None)
    queryset=ProductModel.objects.all()
    if query is not None:
        queryset=queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query)
        )
    template ="ecomerce/list-view.html"
    
    context = {
        "products":queryset
    }
    
    if request.user.is_authenticated:
        template ="ecomerce/list-view.html"
    else:
        template ="ecomerce/list-view_public.html"

    return render(request,template,context)
@login_required
def login_required_view(request):
    print(request.user)
    query= request.GET.get("q",None)
    queryset=ProductModel.objects.all()
    if query is not None:
        queryset=queryset.filter(
            Q(title__icontains=query) |
            Q(price__icontains=query)
        )
    template ="ecomerce/list-view.html"
    
    context = {
        "products":queryset
    }
    
    if request.user.is_authenticated:
        template ="ecomerce/list-view.html"
    else:
        template ="ecomerce/list-view_public.html"

    return render(request,template,context)