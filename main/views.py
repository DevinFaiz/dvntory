from django.shortcuts import render

def show_main(request):
    context = {
        'item_inventory' : [
            {
                'name': 'Gitar Akustik',
                'amount': '5',
                'description': 'Alat musik berdawai yang umumnya digunakan untuk memainkan berbagai genre musik, termasuk akustik, pop, dan folk.',
                'price': '1000000'  
            },
            {
                'name': 'Drum Set',
                'amount': '3',
                'description': 'Set perkusi yang terdiri dari berbagai jenis drum, seperti snare drum, tom-tom, dan bass drum, serta simbal dan hardware pendukung.',
                'price': '5000000'  
            },
            {
                'name': 'Piano Digital',
                'amount': '2',
                'description': 'Alat musik yang memiliki tuts dan suara yang mirip dengan piano akustik, tetapi dalam bentuk digital yang lebih ringkas.',
                'price': '1000000'  
            },
            {
                'name': 'Saxophone',
                'amount': '6',
                'description': 'Alat musik tiup logam dengan berbagai jenis, seperti alto, tenor, dan soprano. Biasanya digunakan dalam jazz dan musik klasik.',
                'price': '4000000'  
            },
            {
                'name': 'Biola',
                'amount': '8',
                'description': 'Instrumen dawai yang dimainkan dengan menggunakan busur. Biasanya digunakan dalam musik klasik.',
                'price': '1000000'  
            },
        ],
    }

    return render(request, "main.html", context)