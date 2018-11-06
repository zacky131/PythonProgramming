# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Pada bagian 2 ini, kita akan belajar mengenai berbagai macam tipe data dalam programming Python. 
Selain itu, kita juga akan belajar bagaimana menyimpan data pada variable serta menggunakannya pada program yang kita buat.
Apa sebenarnya yang terjadi ketika menjalankan program “Lesson_2_variable.py”
Ketika menjalankan program tersebut kita akan melihat : “Aku bisa programming Python dengan mudah!!!”.
"""
print ("Aku bisa programming Python dengan mudah")

"""
Ketika kita menjalankan “Lesson_2_variable.py”, file tersebut berakhiran .py, 
yang artinya Python extension file. 
Python editor kemudian menjalankan program tersebut melalui “Python interpreter”, 
yang membaca program dan menentukan apa arti dari setiap kata di dalam program tersebut. 
Sebagai contoh, ketika interpreter melihat kata “print”, 
maka dia akan menulis pada layar apapun di dalam tanda kurung. 
"""
#Variable

"""
Mari kita coba menggunakan variable di dalam file “Lesson_2_variable.py”. 
Pertama-tama kita coba untuk menentukan variable seperti ini:
"""    
tulisan = 'Saya menyukai progamming Python!!!'
print(tulisan)

"""
Ketika kita klik run, maka akan terpampang tulisan “Saya suka progamming Python!!!”.
Kita baru saja menambahkan variable "tulisan". 
Setiap variable memiliki nilai tertentu,yang merupakan informasi berkaitan dengan variable tersebut. 
Dengan penambahan variable, maka akan memperberat sedikit kerjaan untuk Python interpreter, 
karena mengeksekusi 2 perintah, yang pertama untuk menentukan variable dan yang kedua untuk mencetak tulisan tersebut. 

Beberapa aturan dalam menentukan variable:
    1. variable hanya meliputi huruf angka dan underscore
    2. Spasi tidak dibolehkan "contohnya "tulisan saya"
    3. Variable harus simple dan deskriptif
    4. Hati hati talam menggunakan huruf 'o' dan 'l' karena akan membingunkan dengan angka "1" dan "0"

menghindari salah tulis ketika hendak menggunakan variable
"""
#tulisan = 'Saya menyukai progamming Python!!!'
#print(tulisn)
"""
maka akan ada waring 'NameError' di IPython console
"""

#String
"""
Dalam programming, ada beberapa tipe data yang berbeda. Yang pertama akan kita bahas adalah string
String adalah urutan karakter yang berada di dalam tanda petik (satu atau dua tanda petik), contohnya
"""
'Ini adalah string'
"Ini pun string"
"""
contoh lainnya adalah:
"""
'saya mengatakan kepada rekan saya. Bahwa:"Python sangatlah mudah untuk di pelajari"'
"bahasa pemrograman 'Python' bukan diambil dari nama ular python"
"Juara 1 bisa kita katakan sebagai 'pemenang' dalam kompetisi"

"""
String memiliki beberapa fitur
""" 
judul = 'ada apa dengan cinta'
print(judul.title())
"""
dapat di lihat bahwa di setiap awalan kata akan memiliki huruf kapital.
Hal ini karena kita memakai method "title()". Method dapat melakukan suatu perintah tertentu pada suatu data.
tanda titik(.) setelah kata "judul" mengintruksikan Python untuk menggunakan method "title(). Contoh lainnya adalah:
"""
print(judul.upper())
print(judul.lower())

#Menggabungkan string
nama_depan = 'Lionel'
nama_belakang = 'Ronaldo'
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)
"""
metode menggabungkan string dinamakan concatenation. Kita dapat menggunakan metode ini untuk menulis kalimat komplit
seperti contoh dibawah ini:
"""
print("Hai, " + nama_lengkap.title() + "!")
"""
kita pun dapat melengkapi kalimat dengan menyimpan seluruh kalimatnya menggunakan variable
"""
kalimat = "Hai, " + nama_lengkap.title() + "!"
print(kalimat)

#Menambah spasi kosong di depan (tab)
print('Python')
print('\tPython')
"""
hasilnya seperti kita menekan tombol tab satu kali
"""
#Menambah line baru di bawahnya
print('Bahasa: \nIndonesia\nInggris\nPerancis\nSpanyol\nArab')

#Menghilangkan spasi kosong
"""
tulis di Ipython console
bahasa = '    Indonesia     '
bahasa
bahasa.rstrip() bagian kanan
bahasa.lstrip() bagian kiri
bahasa.strip() dua sisi
"""
#NUMBERS
"""
tulis di IPython console
Integers:
1+1
5-4
2*8
5/2
pangkat
3**2
2**3
10**6
prioritas
1+2*4
(1+2)*4
Floats:
0.5 + 0.7
0.1 + 0.3
2 * 0.4
"""
#Menghindari kesalahan dengan menggabungkan string
"""tulis di I console saja"""
umur = 17
#kalimat_salah = 'Selamat ulang tahun yang ke' + umur  #ini akan menghasilkan error karena string dan nomor di gabungkan
kalimat_benar = 'Selamat ulang tahun yang ke-' + str(umur)

"""
Sekian untuk sesi kali ini, jangan lupa untuk subscribe channel ini untuk mendapatkan notifikasi
setiap ada update. Dan saya akan selalu mengupload video terbaru minimal 1 dalam 1 minggu. Terimakasih


















