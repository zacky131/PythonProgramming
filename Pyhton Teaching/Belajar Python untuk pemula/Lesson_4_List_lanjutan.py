#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:56:25 2018

@author: zacky
"""

"""
Halo semua, bertemu dengan saya kembali di seri belajar Python untuk pemula.
Pada bagian ini akan melanjutkan materi mengenai list untuk pengembangan implementasinya
"""
# Looping menggunakan list
'''
kali ini kita akan belajar bagaimana process looping pada suatu list, tidak berpengaruh
seberapa panjang list tersebut
Dalam programming, kita akan selalu menjalankan semua masukan yang terdapat di dalam list
melakukan sesuatu yang sama untuk setiap item. Sebagai contoh, kita memiliki list yang berupa angka
dimana kita ingin melakukan fungsi operasi statistik pada setiap elementnya.
Ketika ingin melakukan perintah yang sama, dalam Python menggunakan "for" loop
sebagai contoh
'''
klub_bola = ['Barcelona', 'Real Madrid', 'Juventus', 'Liverpool']
for klub in klub_bola:
    print(klub)
'''
Contoh barusan 