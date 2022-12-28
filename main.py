import streamlit as st
import math

from streamlit_option_menu import option_menu

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Mau Hitung Apa?',
    ['Hitung Luas dan Volume Kubus',
    'Hitung Luas Persegi',
    'Hitung Luas dan Keliling Lingkaran',
    'Hitung Luas Segitiga',
    'Author'],
    default_index=0)

# halaman hitung luas permukaan dan volume kubus
if (selected == 'Hitung Luas dan Volume Kubus') :
    st.title('Hitung Luas dan Volume Kubus')

    sisi = st.number_input ("Masukan sisi kubus (cm):")
    hitung = st.button ("Hitung luas dan volume kubus")

    if hitung :
        luas_permukaan = 6 * sisi**2
        luas_volume = sisi**3

        st.success (f"Luas kubus adalah = {luas_permukaan} cm^2")
        st.success (f"Volume kubus adalah = {luas_volume} cm^2")

# halaman hitung luas persegi
if (selected == 'Hitung Luas Persegi') :
    st.title('Hitung Luas Persegi')

    sisi = st.number_input ("Masukan sisi persegi (cm):")
    hitung = st.button ("Hitung luas persegi")

    if hitung :
        luas_persegi = sisi * sisi
        st.success (f"Luas persegi adalah = {luas_persegi} cm^2")

# halaman hitung luas dan keliling lingkaran
if (selected == 'Hitung Luas dan Keliling Lingkaran') :
    st.title('Hitung Luas dan keliling Lingkaran')

    jari_jari = st.number_input ("Masukan jari-jari:")
    hitung = st.button ("Hitung luas dan keliling lingkaran")

    if hitung :
        luas = math.pi * jari_jari **2
        keliling = 2 * math.pi * jari_jari

        st.success (f"Luas lingkarang adalah {luas:.2f} cm")

        st.success (f"Keliling lingkarang adalah {keliling:.2f} cm")

        st.write (f"Catatan: Nilai 1 π adalah {math.pi:.2f} untuk mendapatkan hasil π maka, hasil di bagi 3.14.")

# halaman hitung luas segitiga
if (selected == 'Hitung Luas Segitiga') :
    st.title('Hitung Luas Segitiga')

    alas = st.number_input ("Masukan alas segitiga (cm):")
    tinggi = st.number_input ("Masukan tinggi segitiga (cm):")
    hitung = st.button ("Hitung luas segitiga")

    if hitung :
        luas = 0.5 * alas * tinggi
        st.success (f"Luas segitiga adalah = {luas} cm")

# author
if (selected == 'Author') :
    st.title('Terimakasih sudah menggunakan aplikasi ini.')
    st.title('Salam.')
    st.title('Cond Rock')
