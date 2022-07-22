import pandas as pd
import csv

name = ''
surname = ''
student_number = ''
letter_grade = ''
midterm_note = ''
final_note = ''
situation = ''

while True:
    print("""******************************** MENU ********************************
            1. Öğrenci Bilgilerini Gir
            2. Öğrenci Bilgilerini Görüntüle
            3. Öğrenci Bilgilerini Excel Tablosuna Dönüştür
            4. Çıkış
**********************************************************************""")
    print("--> Lütfen 0-5 arasında tam sayı değeri giriniz...")
    action = input("İşlem seçiniz: ")
    print('\n')

    if action == '1':
        name = input("Adınızı giriniz: ")
        name = name.capitalize()
        surname = input("Soyadınızı giriniz: ")
        surname = surname.capitalize()
        student_number = input("Okul numaranızı giriniz: ")

        midterm_note = int(input("Vize notunuzu giriniz: "))

        while midterm_note > 100 or midterm_note < 0:
            print("--> Lütfen 0 ile 101 arasında tam sayı değeri giriniz...")
            midterm_note = int(input("Vize notunuzu giriniz: "))

        final_note = int(input("Final notunuzu giriniz: "))

        while final_note > 100 or final_note < 0:
            print("--> Lütfen 0 ile 101 arasında tam sayı değeri giriniz...")
            final_note = int(input("Final notunuzu giriniz: "))

        average_point = (midterm_note * 0.4 + final_note * 0.6)

        if 100 >= average_point >= 85:
            letter_grade = 'AA'
            situation = 'Geçti'
        elif average_point >= 80:
            letter_grade = 'BA'
            situation = 'Geçti'
        elif average_point >= 75:
            letter_grade = 'BB'
            situation = 'Geçti'
        elif average_point >= 70:
            letter_grade = 'CB'
            situation = 'Geçti'
        elif average_point >= 65:
            letter_grade = 'CC'
            situation = 'Geçti'
        elif average_point >= 60:
            letter_grade = 'DC'
            situation = 'Geçti'
        elif average_point >= 55:
            letter_grade = 'DD'
            situation = 'Geçti'
        elif 55 > average_point >= 0:
            letter_grade = 'FF'
            situation = 'Kaldı'

        with open('student_information.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, surname, student_number, average_point, letter_grade, situation])
            file.close()

        print('\n')
    if action == '2':
        try:
            csv_file = pd.read_csv("student_information.csv", names=["Ad", "Soyad", "Ögrenci Numarası",
                                                                     "Başarı Puanı", "Harf Notu", "Durum"])
            print(csv_file)

        except FileNotFoundError:
            print("--> Öğrenci Bilgileri Bulunmamaktadır...")

        print('\n')
    if action == '3':
        try:
            csv_file = pd.read_csv("student_information.csv", names=["Ad", "Soyad", "Öğrenci Numarası",
                                                                     "Başarı Puanı", "Harf Notu", "Durum"])
            data = pd.DataFrame(csv_file)
            data.to_excel('student_result.xlsx', index=False)
            print("Bilgiler excel dosyasına dönüştürüldü.")
            print("Dosya dizinini kontrol ediniz...")

        except FileNotFoundError:
            print("--> Öğrenci Bilgileri Oluşturulmamıştır...")

        print('\n')
    if action == '4':
        print("Çıkış Yapıldı...")
        break
