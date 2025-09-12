Link PWS: https://natan-harum-madridstore.pbp.cs.ui.ac.id/

TUGAS 2

Soal jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat dan mengaktifkan Virtual Environment baru.
    2. Membuat file requirements.txt dan menambahkan dependencies.
    3. Meng-install dependencies.
    4. Setup environment variables di .env dan env.prod
    5. Menambahkan ALLOWED_HOSTS di settings.py
    6. Migrate database.
    7. Menjalanakan server (di step ini proyek Django sudah berhasil dibuat).
    8. Setelah di tes bisa berjalan, lalu membuat aplikasi main (python manage.py startapp main).
    9. Menambahkan main sebagai installed apps di settings.py
    10. Mengubah isi models.py pada direktori aplikasi main dan mengisi dengan Product dan atribut-atribut yang diperlukan yang dicatumkan dalam soal.
    11. Membuat dan menerapkan migrasi model terhadap perubahan model yang terjadi.
    12. Mengubah views.py di direktori aplikasi main dan mengisinya dengan fungsi yang sesuai yang menerima parameter request.
    13. Membuat direktori templates di dalam direkori main dan menambahkan file html di dalam direktori templates.
    14. Membuat tampilan di file html yang menerima data dari views.py tadi.
    15. Mengonfigurasi Routing URL Aplikasi main.
    16. Mengonfigurasi Routing URL Proyek.

Soal buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Link Bagan: https://drive.google.com/file/d/1TjZXIQXXRJoj5t-vvd-H1w7R2E0YFnPt/view?usp=sharing
    Penjelasan Bagan:
    1. User akses website dari web browser akan mengirimkan HTTP request
    2. urls.py akan memeriksa link tersebut dan diarahkan ke fungsi di views.py yang sesuai, tetapi kalau tidak ada akan menampilkan eror 404
    3. views.py  menerima request, lalu mengolah data yang diambil dari models.py atau bisa langsung kasih response sederhana.
    4. models.py berisi definisi struktur data (ORM). Dipakai oleh views untuk query database.
    5. html merupakan tampilan dari request yang dilakukan atau hasil akhir yang akan di kirimkan ke user setelah diberi data dari view lalu dikirimkan ke user lagi sebagai http response

Soal Jelaskan peran settings.py dalam proyek Django!
    file settings.py adalah pusat konfigurasi Django, jadi semua hal teknis seperti database, keamanan, apps, static file, debug mode itu diataur disini

Soal Bagaimana cara kerja migrasi database di Django?
    Setiap ada perubahan di models.py pada aplikasi harus dibuat migrasi baru dengan cara python manage.py makemigrations lalu menerapkannya dengan cara python manage.py migrate
    dengan begini data proyek kita akan sinkron dengan SQL yang dihandle oleh Django.

Soal Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Menurut saya karena Django itu Python based dimana Python itu merupakan bahasa yang cukup mudah diguanakan dan dipelajari. Kemudian, dari segi keamanan Django juga cukup baik karena 
    sudah ada built in keamanan seperti SQL injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF). Begitu juga dengan komunitas Django sangatlah luas di internet 
    jadi lebih mudah jika mengahadapi masalah atau jika ada suatu pertanyaan bisa di cari dengan lebih mudah.





TUGAS 3

 Soal jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
     Data delivery sangatlah penting karena dengan data delivery kita bisa mengirimkan suatu informasi atau data dari suatu tempat ke tujuannya dalam hal ini adalah baik ke pengguna,          aplikasi, atau sistem lain.  Ini memastikan bahwa data yang dibutuhkan tersedia di tempat yang tepat dan waktu yang tepat, memungkinkan integrasi yang lancar dan operasional yang
     efisien. 

Soal menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya pribadi json lebih baik karena lebih mudah dibaca dan dipahami karena format penulisannya lebih ringkas dan rapih. Kemudian kenapa JSON lebih populer dibanding xml selain
    alasan saya tersebut adalah karena JSON memiliki ukuran data yang lebih kecil dan parsing yang lebih cepat, karena itulah JSON meningkatkan efisiensi dan kinerja aplikasi, terutama
    di lingkungan web.

Soal jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    method is_valid berfungsi sebagai memeriksa apakah data yang dimasukan oleh user ke form sudah sesuai dengan aturan validasi yang ditentukan, seperti ipe data yang benar, panjang
    karakter, atau pola tertentu. Method ini mengembalikan nilai True atau False, jika return True data akan diproses lebih lanjut atau masuk ke database, tetapi jika False form akan
    mengandung pesan kesalahan yang menjelaskan mengapa data tidak valid.

Soal mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token melindungi form Django dari CSRF. Django menempelkan kode unik di setiap form halaman asli situs, lalu server mengecek kode itu saat form dikirim.
    Tanpa token, penyerang bisa memanfaatkan cookie login korban dengan membuat halaman yang diam-diam mengirim request ke situs kita, sehingga aksi berbahaya bisa terjadi tanpa
    sepengetahuan korban.
    
Soal jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Menambahkan UUID pada models.py di main dan merubah atribut nama menjadi name.
    2. Migrasi data karena ada perubahan pada model.
    3. Membuat file form.py di direktori main dan membuat fields formnya sepert name, price, dll.
    4. Membuat function create_product guna endpoint untuk membuat data produk baru dengan alur yang aman. di views.py pada direktori main. 
    5. Membuat function show_product guna endpoint detail produk sekaligus menambah view counter tiap kali dibuka di views.py pada direktori main.
    6. membuat direktori templates di root projek dan membuat dile base.html di dalamnya untuk sebagai template dasar untuk halaman lain pada projek ini.
    7. Membuat file html untuk tampilan detail produk dan create produk di direktori main/templates.
    8. Membuat function untuk endpoint json dan xml di views.py dan juga menambahkan endpoint by id.  
