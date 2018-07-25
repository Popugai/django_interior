from django.shortcuts import render

from django.http import response

from .models import Product_Category, Product


# Create your views here.

# def main(request):
#     return render(request,'')


# def main(request):
#     return render(request, 'interiorapp/index.html', content_main)


def main(request):
    title = 'главная'
    products = Product.objects.all()
    content_main = {'main_menu': main_menu, 'title': title, 'products': products}
    return render(request, 'interiorapp/index.html', content_main)


def product(request):
    title = 'список продуктов'
    products = Product.objects.all()
    content_product = {'main_menu': main_menu, 'title': title, 'products': products}
    return render(request, 'interiorapp/interior_product.html', content_product)


def product_details(request):
    title = 'описанте продукта'
    products = Product.objects.all()[:3]
    content_product_details = {'main_menu': main_menu, 'title': title, 'products': products}
    return render(request, 'interiorapp/interior_product_details.html', content_product_details)


def contact(request):
    return render(request, 'interiorapp/interior_contact.html', content)


main_menu = [
    {'href': 'main', 'name': 'HOME'},
    {'href': 'product', 'name': 'PRODUCTS'},
    {'href': 'contact', 'name': 'CONTACT'},
]

content = {
    'main_menu': main_menu
}

# content_main = {
#     'main_menu': main_menu,
#     'items_list': [1, 2, 3, 4, 5, 6]
# }

content_product = {
    'main_menu': main_menu,
    'items_list': [1, 2, 3, 4, 5, 6, 7, 8, 9]
}
