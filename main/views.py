from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    product = Product.objects.all()
    my_list = [
        {
            'name': 'Pulang',
            'amount': 5,
            'description': 'Mengangkat kisah pergulatan hidup sosok pria kecil dari pelosok daratan Bukit Tinggi yang kemudian dibawa ke kota untuk ditempa menjadi seorang tukang jagal dunia.',
            'category': 'Fiksi'
        },

        {
            'name': 'Atomic Habits',
            'amount': 7,
            'description': 'Merupakan buku motivasi yang berisikan cara mengubah hidup melalui kebiasaan-kebiasaan kecil.',
            'category': 'Non-Fiksi'
        },

        {
            'name': 'Laut Bercerita',
            'amount': 10,
            'description': 'Merupakan kisah nyata dari pengalaman seorang aktivis yang menghilang pada tahun 1998, diculik, kemudian dikembalikan 9 orang dan dinyatakan 13 orang hilang.',
            'category': 'Fiksi'
        }
    ]

    my_name = "Ammara Pranahiza"
    my_class = "PBP B"
    my_npm = "2206083022"
    my_products = list(product) + my_list

    context = {
        'my_list': my_list ,
        'my_name': my_name , 
        'my_class': my_class ,
        'my_npm' : my_npm,
        'my_products' : my_products
    }
        
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
