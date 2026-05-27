from django.shortcuts import render, get_object_or_404
from .models import ProductModel,Cart
from django.http import HttpResponse

# Create your views here.

def add_product(request):
    if request.method=="POST":
        name=request.POST.get("name")
        price=request.POST.get("price")
        quantity=request.POST.get("quantity")
        data=ProductModel.objects.create(name=name,price=price,quantity=quantity)

        return render(request,"success.html",{"message":"product added successfully"})

    return render(request,"product_form.html")

def view_all_product(request):
    """
    thsi function wil return all the products
    :param request: no param
    :return: list of products
    """
    data=ProductModel.objects.all().values()
    return render(request,"product_list.html",{"product_data":list(data)})

def delete_by_id(request,id):
    """
    this function takes id as params and delete the respective product
    :param request:
    :param id:
    :return:
    """
    if request.method=="POST":
        data=ProductModel.objects.get(id=id)
        data.delete()
        return render(request,"success.html",{"message":"product deleted successfully"})
    return render(request,"product_list.html")
def add_to_cart(request, id):

    product = get_object_or_404(ProductModel, id=id)

    Cart.objects.create(
        product_id=product.id,
        p_price=product.price
    )

    return render(request, "success.html", {
        "message": "Product Added To Cart Successfully"
    })
def delete_from_cart(request, id):
    product = get_object_or_404(ProductModel, id=id)
    Cart.objects.filter(product_id=product.id).delete()
    return render(request, "success.html", {
        "message": "Product Deleted Successfully"

    })