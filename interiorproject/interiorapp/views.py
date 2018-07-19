from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'interiorapp/index.html')

# def main(request):
#     return render(request,'')

def product(request):
    return render(request,'interiorapp/interior_product.html')

def product_details(request):
    return render(request,'interiorapp/interior_product_details.html')

def contact(request):
    return render(request,'interiorapp/interior_contact.html')