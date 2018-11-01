#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:24:03 2018

@author: zacky
"""

'''
Halo semua apa kabar, kembali lagi bersama saya untuk melanjutkan tutorial 
Python bagian ketiga .Kali ini saya akan membahas mengenai list di Python.
Apakah itu lists? list adalah kumpulan dari beberapa items yang mengikuti
urutan tertentu. Kita dapat membuat apa saja di dalam list, meliputi huruf, angka
dan sebagainya. Dalam Python, tanda braket kotak ([]) mengindikasinkan list.
Setiap element di dalam list dipisahkan oleh tanda kommma.
Untuk lebih jelas mari kita lihat contoh di bawah ini
'''
kendaraan = ['mobil', 'motor', 'becak', 'kereta', 'bus', 'pesawat terbang', 'perahu'] 
#print(kendaraan)
'''
Jika kita memerintahkan Python untuk print list, maka hasilnya akan kembali ke pada list
tersebut termasuk tanda kurung kotak nya. Oleh karena itu, mari kita mencoba hal lain, 
misalnya untuk mengakses element di dalam list tersebut.
'''
#Mengakses element di dalam list
'''
List adalah koleksi element yang terurut, sehingga kita dapat memerintahkan Python
posisi ataupun index dari item yang diinginkan. Untuk mengaksesnya, kita dapat menulis
nama dari list tersebut, diikuti oleh index di dalam tanda kurung kotak ([])
'''
print(kendaraan[0]) #beri contoh untuk yang lain dan jelaskan

'''
Index posisi dimulai dari angka 0 hingga element list terakhir, jika melebihinya
akan ada peringatan error
'''
print(kendaraan[-1])
'''
untuk mengakses list, dapat pula dari arah berlawanan atau dari list terakhir
dengan memberi tanda negative pada index yang di inginkan
'''
# Menggunakan nilai individual dari dalam list
kalimat = "Kendaraan yang sering saya gunakan adalah " + kendaraan[1].title() + "."
print(kalimat)

# Mengubah, menambah dan menghapus element di dalam list
mobil = ['Toyota', 'Honda', 'Volkswagen', 'BMW', 'Mercedes']
print (mobil)
'''
Item pertama adalah Toyota, bagaimana kita mengubahnya?
'''
# Mengubah element di dalam list
mobil[0] = 'Esemka'
print(mobil)

# Menambah element di dalam list
mobil.append('Suzuki')
print(mobil)
'''
Metode append() memudahkan kitu untuk membuat list secara dinamik
'''
motor = []
motor.append('honda')
motor.append('yamaha')
motor.append('vespa')
print(motor)

## Menyisipi element kedalam list
#motor.insert(0, 'ducati')
#print(motor)

## Menghapus element dalam list
#del motor[1]
#print (motor)

## Menghapus element dengan metode lain pop()
#'''
#metode pop() akan menghapus element yang paling akhir
#'''
#popped_motor = motor.pop()
#print (motor)

## Menghapus dengan pop() di posisi manapun
#motor_pertama = motor.pop(0)

# Menghapus element berdasarkan nilai
motor = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motor)
motor.remove('yamaha')
print(motor)

# Mengorganisasikan list
mobil = ['ford', 'audi', 'chevrolet', 'subaru']
mobil.sort() # berdasarkan alfabet
print(mobil)
mobil.sort(reverse=True)
print(mobil)


# Mengetahui panjangnya list
print(len(mobil))








