from django.shortcuts import render

# Create your views here.
def show_main(request):
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

    context = {
        'my_list': my_list ,
        'my_name': my_name , 
        'my_class': my_class ,
        'my_npm' : my_npm
    }
        
    return render(request, "main.html", context)