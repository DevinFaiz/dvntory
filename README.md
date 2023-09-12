# **DVNTORY**

Devin Faiz Faturahman 2206830593 PBP E

Tautan untuk mengakses web di adaptable, [klik tautan ini](https://dvntory.adaptable.app)

## Membuat sebuah proyek Django baru
1. Mulai dengan membuat direktori baru sesuai keinginan. Membuat direktori bernama `dvntory` dan buka terminal shell di dalam direktori tersebut.
2. Selanjutnya, buat virtual environment dengan perintah `python3 -m venv env` untuk mengisolasi proyek Python. Aktifkan virtual environment dengan menjalankan perintah `source env/bin/activate` (pengguna Mac).
3. Buat file `requirements.txt` di dalam direktori proyek dan isi dependencies yang diperlukan untuk proyek.
4. Install semua dependencies dengan menjalankan perintah `pip install -r requirements.txt`. Selanjutnya, buat proyek Django dengan perintah `django-admin startproject dvntory`.
5. Buka file `settings.py`. Cari variabel "ALLOWED_HOSTS" dan ubah isinya menjadi ["*"].
6. Buka terminal lalu jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek.
7. Proyek Django yang baru telah berhasil dibuat, buka proyeknya dalam link ini http://localhost:8000. Jika tidak error dan muncul gambar roket, maka proyek Django berhasil.
8. Hentikan server dengan menekan `Ctrl+C` di terminal. Menonaktifkan virtual environment dengan perintah `deactivate`.

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Buka terminal di direktori utama dan aktifkan virtual environment dengan perintah `source env/bin/activate`.
2. Jalankan perintah `python3 manage.py startapp main` untuk membuat folder baru bernama main.
3. Buka file settings.py di direktori proyek dan tambahkan 'main' pada variabel INSTALLED_APPS.

## Membuat model pada aplikasi main
1. Ubah file models.py yang terdapat di dalam direktori aplikasi main untuk mendefinisikan model baru dengan nama Item dan memiliki atribut wajib di bawah ini.
- `name` sebagai nama item dengan tipe CharField.
- `amount` sebagai jumlah item dengan tipe IntegerField.
- `description` sebagai deskripsi item dengan tipe TextField.
Diperbolehkan untuk menambah atribut jika diinginkan.
2. Isi file models.py dengan kode berikut.
```py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    amount = models.IntegerField()
```

3. Lakukan migrasi model dengan menjalankan perintah `python3 manage.py makemigrations` lalu jalankan perintah `python3 manage.py migrate`.

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
1. Buat direktori baru dengan nama `templates` di dalam direktori aplikasi `main`, lalu buat file `main.html` di dalamnya.
2. Buka file `views.py` yang ada di direktori `main` lalu tambahkan baris kode di paling atas `from django.shortcuts import render`.
3. Buat fungsi `show_item` dengan menggunakan 1 parameter, dan isi seperti contoh di bawah ini.
```py
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
```
4. Buka file `main.html`, ubah kode yang tadinya statis menjadi kode Django yang sesuai.

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Jika belum ada, buat file urls.py pada direktori main dan buka file tersebut. Import path dari django.urls dan import views dari views.py. Seperti contoh di bawah ini.
```py
from django.urls import path
from main.views import show_item

app_name = 'main'

urlpatterns = [
    path('', show_item, name='show_item'),
]
```

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Buka file urls.py pada direktori proyek dvntory dan import modul include dari django.urls.
2. Tambahkan path yang akan mengarahkan ke aplikasi 'main' di dalam variabel urlpatterns. Seperti contoh di bawah ini.
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', include('main.urls')),
]
```

## Cara deployment aplikasi ke Adaptable
1. Setelah berhasil login, pilih opsi `New App` dan kemudian pilih `Connect an Existing Repository`.
2. Sambungkan Adaptable.io dengan akun GitHub.
3. Pilih repositori proyek aplikasi dan branch yang akan digunakan untuk proses deployment.
4. Pilih template deployment `Python App Template` dan pilih `PostgreSQL`.
5. Sesuaikan versi Python dengan menggunakan perintah `python3 --version` di terminal.
6. Di bagian `Start Command,` masukkan `python3 manage.py migrate && gunicorn dvntory.wsgi`.
7. Beri nama aplikasi dan nama domain situs web.
8. Aktifkan opsi `HTTP Listener on PORT` dan klik `Deploy App` untuk proses deployment.

## Buat bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![Gambar Bagan Django](image/BaganDjango.png)
Saat request client masuk, request tersebut akan diproses oleh `urls.py` terlebih dahulu. Hal ini dikarenakan url routingnya ada di dalam `urls.py`. Kemudian, `urls.py` akan mengecek path yang diminta pada request lalu akan diforward request tersebut kepada `views.py` yang sesuai. Jika fungsi pada `views.py` membutuhkan read/write data dari database, maka `views.py` akan menghubungi atau mengambil data dari `models.py` sebagai perantara ke database. Kemudian, untuk menampilkan data tersebut, `views.py` akan mengakses template tampilan yang sesuai pada berkas html. Output akhirnya berupa halaman html yang utuh dan sesuai sebagai response untuk client. Kaitan antara `urls.py, views.py, models.py, dan berkas html` adalah semuanya berperan dan saling terhubung satu sama lain dalam memproses response suatu request client.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment merupakan sebuah environment yang terisolasi dari dependencies utama. Dengan begitu, setiap environment bisa memiliki dependecies yang sesuai dengan kriterianya masing-masing tanpa harus tercampur dengan dependecies dari environment lainnya. Penggunaan virtual environment bersifat tak terbatas sehingga kita dapat membuat membuat banyak venv untuk project yang berbeda-beda. Tools ini juga banyak digunakan di Python yaitu di Django, untuk mengeksekusi suatu aplikasi yang telah dibuat.

Saat kita menginstall suatu library tanpa menggunakan virtual env, maka secara default library tersebut akan terinstall secara global pada python dan semua aplikasi dapat mengaksesnya. Namun, biasanya antar aplikasi membutuhkan serta cocok dengan library atau versi library yang berbeda-beda. Jika diinstall secara global, ketika library tersebut diupgrade ke versi terbaru, lalu terdapat aplikasi A yang kita buat tidak kompatibel dengan versi terbaru library tersebut. Tentunya aplikasi A menjadi tidak bisa berjalan dengan semestinya. Sementara itu, terdapat aplikasi B yang membutuhkan library versi terbaru tersebut untuk berjalan. Oleh karena itu, penggunaan virtual env sangat penting untuk mencegah hal-hal semacam itu terjadi sehingga setiap aplikasi tetap bisa berjalan dengan librarynya masing-masing yang sudah terisolasi. Kita tetap dapat membuat sebuah aplikasi web tanpa menggunakan virtual environment, tetapi sebaiknya tetap memakai virtual environment agar dependenciesnya bisa terklasifikasi dengan baik.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya
MVC, MVT, dan MVVM adalah tiga pendekatan arsitektur perangkat lunak yang digunakan untuk mengorganisasi dan memisahkan komponen dalam sebuah aplikasi. 
### Pengertian MVC, MVT, dan MVVM
- **MVC (Model-View-Controller):**
    - Model: Model adalah bagian yang mengatur logika bisnis dan manipulasi data. Model bertanggung jawab untuk mengakses database atau sumber data lainnya, memproses informasi, dan mengirimkan hasilnya kepada Controller.
    - View: View adalah tampilan yang ditampilkan kepada pengguna. Ini bertanggung jawab untuk menampilkan data dari Model dan menerima masukan dari pengguna.
    - Controller: Controller adalah bagian yang mengatur interaksi antara Model dan View. Ini menangani permintaan dari pengguna, memprosesnya, dan memutuskan bagaimana Model dan View harus berinteraksi.

- **MVT (Model-View-Template):**
    - Model: Seperti dalam MVC, Model merupakan komponen yang mengatur logika bisnis dan manipulasi data.
    - View: View dalam MVT adalah tampilan yang ditampilkan kepada pengguna. Ini juga memiliki komponen Template yang mengatur cara data dari Model ditampilkan dalam View.
    - Template: Template adalah komponen tambahan dalam MVT yang menentukan cara data dari Model akan dirender ke dalam View.

- **MVVM (Model-View-ViewModel):**
    - Model: Seperti dalam MVC dan MVT, Model adalah komponen yang mengatur logika bisnis dan manipulasi data.
    - View: View dalam MVVM adalah tampilan yang ditampilkan kepada pengguna, mirip dengan View dalam MVC dan MVT.
    - ViewModel: ViewModel adalah komponen kunci dalam MVVM. Ini bertanggung jawab untuk menyediakan data yang akan ditampilkan dalam View dan berperan sebagai perantara antara Model dan View.

### Perbedaan MVC, MVT, dan MVVM
- MVC biasanya digunakan dalam pengembangan aplikasi desktop dan web tradisional. Kontrol aliran logika terletak di Controller, yang menghubungkan Model dan View.
- MVT adalah pendekatan yang umum digunakan dalam kerangka kerja web Django, yang banyak digunakan dalam pengembangan web berbasis Python.
Template yang terpisah dari View memungkinkan pemisahan antara logika presentasi dan logika tampilan.
- MVVM adalah pendekatan yang umum digunakan dalam pengembangan aplikasi berbasis data yang canggih dan interaktif, terutama di lingkungan pengembangan aplikasi seluler dan desktop. ViewModel memungkinkan pemisahan yang lebih baik antara logika presentasi dan logika bisnis, dan ini dapat sangat berguna dalam pengembangan antarmuka pengguna yang kompleks.