333333333322Link PWS: https://natan-harum-madridstore.pbp.cs.ui.ac.id/

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
     Data delivery sangatlah penting karena dengan data delivery kita bisa mengirimkan suatu informasi atau data dari suatu tempat ke tujuannya dalam hal ini adalah baik ke pengguna, aplikasi, atau sistem lain.
     Ini memastikan bahwa data yang dibutuhkan tersedia di tempat yang tepat dan waktu yang tepat, memungkinkan integrasi yang lancar dan operasional yang efisien. 

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
    4. Membuat function create_product guna endpoint untuk membuat data produk baru dengan alur yang aman di views.py pada direktori main. 
    5. Membuat function show_product guna endpoint detail produk sekaligus menambah view counter tiap kali dibuka di views.py pada direktori main.
    6. membuat direktori templates di root projek dan membuat dile base.html di dalamnya untuk sebagai template dasar untuk halaman lain pada projek ini.
    7. Membuat file html untuk tampilan detail produk dan create produk di direktori main/templates.
    8. Membuat function untuk endpoint json dan xml di views.py dan juga menambahkan endpoint by id. 

Link SS Postman: https://drive.google.com/drive/folders/1nxhPpR8AE7spca-FRAleu-4LTP9R6xJy?usp=sharing





TUGAS 4

Soal apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    Django AuthenticationForm adalah form bawaan dari Django yang dipakai untuk login user. Form ini nantinya akan berisi field username dan password yang nantinya akan diisi oleh user, kemudian Saat disubmit,
    Django akan memvalidasi apakah kombinasi username & password tersebut cocok dengan data di database. Jika valid, user dianggap terautentikasi dan bisa login menggunakan login() function.
    
        Kelebihan:
            1. Built-in & praktis karena sudah bawaan dari Django.
            2. Validasi otomatis oleh Django.
            3. Keamanan terjamin karena di Django Sudah mendukung hashing password & perlindungan CSRF token pada form
            
        Kekurangan:
            1. Kurang fleksibel karena tidak bisa kostumisasi filed contohnya login dengan email.
            2. UI sangat dasar biasanya butuh custom template/CSS.
            3. Tidak ada fitur tambahan seperti captcha, 2FA, atau "remember me" checkbox secara bawaan.

Soal apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    1. Autentikasi adalah proses verifikasi identitas pengguna. Contohnya user login dengan username & password artinya memastikan user yang login adalah benar pemilik akun/identitas tersebut.
    2. Otorisasi adalah proses pemberian izin / hak akses kepada pengguna setelah terautentikasi.Contohnya jika user yang sudah di Auntentikasi tadi adalah admin maka user tersebut diberikan hak sebagai admin.
    Django menyediakan Authentication system bawaan yaitu django.contrib.auth contohnya AuthenticationForm untuk autentikasi login dan UserCreationForm untuk register user. Untuk otorisasi Django menggunakan
    sistem Permissions dan Groups, yaitu Permission adalah hak akses spesifik (add_user, delete_product, dsb) dan Group adalah kumpulan permission, bisa diberikan ke banyak user. Contohnya request.user punya
    method seperti user.is_authenticated untuk cek sudah login atau belum dan user.is_staff, user.is_superuser untuk hak akses khusus.

Soal apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

    Kelebihan Cookies:
        1. Sederhana dan praktis karena udah digunakan, cukup simpan data di browser.
        2. Stateless server artinya server tidak perlu menyimpan data state karena data sudah dibawa oleh client.
        3. Bisa dipakai lintas server misalnya untuk tracking login atau preferensi user di beberapa domain/subdomain.
        
    Kelebihan Session:
        1. Lebih aman karena data sensitif tidak dikirim ke client, hanya session ID.
        2. Bisamenyimpan data besar karena disimpan di server, bisa menyimpan object atau informasi user lebih banyak.
        3. Kontrol penuh di server jadi erver bisa menghapus atau memperbarui session kapan saja.

    Kekurangan Cookies:
        1. Ukuran Terbatas karena iasanya max 4KB per cookie.
        2. Kurang aman karena tersimpan di client, bisa diubah/dibaca oleh user.
        3. Beban request karena cookies dikirim otomatis di setiap request.

    Kekurangan Session:
        1. Membebani Sserver kemua data harus disimpan dan dikelola di server.
        2. Butuh manajemen session perlu diatur masa berlakunya (expiry), penyimpanan, dan pembersihan (session cleanup).

Soal apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Cookies tidak aman secara default karena bisa dicuri cookie dari browser korban atau kalau developer simpan data penting langsung di cookie (tanpa enkripsi), bisa diubah user. Django menangani hal ini dengan
    Secure Flag seperti Secure=True yaitu cookie hanya dikirim lewat HTTPS, bukan HTTP biasa, SameSite membatasi pengiriman cookie lintas domain, django.core.signing yaitu membuat cookie terenkripsi, sehingga
    kalau diubah user, akan invalid, dan Django default tidak simpan data user di cookie jadi browser hanya menyimpan session ID.

Soal jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat Fungsi login dan register di views.py.
    2. Membuat HTML login dan register di main/templates.
    3. Memetakan urls untuk login dan dan register di urls.py direktori main.
    4. Membuat fungsi logut di views.py dan membuat button dan anchor link nya di main.html            direktori main dan membuat urls nya juga di urls.py di direktori main.
    5. Modifikasi fungsi show main dan show product di views.py dengan menambahkan Decorators          agar hanya bisa diakses saat login.
    6. Menggunakan cookies untuk menampilkan last login di main.html.
