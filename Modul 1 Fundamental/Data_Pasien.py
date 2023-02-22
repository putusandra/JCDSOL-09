# Nama : dr. A.A. PUTU SANDRA 
# Data Pasien : Rumah Sakit Digital Ibu dan Anak
# Capstone Modul 1 : Aplikasi Skrining RSD Ibu dan Anak 

#** DOMAIN KNOWLEDGE **
# 1. Klasifikasi Hipertensi (tekanan darah tinggi) menurut JNC 8
    #Bila tekanan darah sistole <=120 dan diastole <=80: Tensi Normal
    #Bila tekanan darah sistole < 90 dan diastole < 60: Tensi Rendah
    #Bila tekanan darah sistole <140 dan diastole <90: Prahipertensi
    #Bila tekanan darah sistole <160 dan diastole <100: Hipertensi tingkat I
    #Bila tekanan darah sistole >160 dan diastole >100: Hipertensi tingkat II

# 2. Tingkat risiko preeklampsia berdasarkan riset Obsgyn UNAIR
    # Preeklampsia --> kondisi hipertensi pada kehamilan trimester I (3 bulan) yang menyebabkan kurangnya aliran darah ke janin
    # Risiko preeklampsia dihitung dengan rumus MAP (Mean Arterial Pressure) = ((TD sistole + 2*TD Diastole)/3)

#Bila MAP <70
def risikoLain():
    print('\nStatus Hasil:\n\nTekanan Darah Rendah\nTanda Gangguan Selain Preeklampsia\nPeriksa BMI dan ambil rujukan spesialis.')
    return bmi_ps()
#Bila MAP >=70
def risikoRendah():
    print('\nStatus Hasil:\n\nTekanan Darah Normal\nRisiko Preeklampsia Rendah\n\nPeriksa faktor risiko lain:\n1. BMI Obesitas (lanjut skrining BMI)\n2. Riwayat preeklampsia atau hipertensi \n3. Hamil di usia <20 dan >35 tahun\n')
    return bmi_ps()
#Bila MAP >90
def risikoSedang():
    print('Risiko Sedang untuk Preeklampsia\n\nLanjut periksa BMI dan ambil rujukan spesialis.')
    return bmi_ps()
#Bila MAP >100
def risikoTinggi():
    print('Risiko Tinggi Preeklampsia\n\nLanjut periksa BMI dan ambil rujukan spesialis.')
    return bmi_ps()

# 3. Klasifikasi BMI (Body Mass Index) berdasarkan World Health Organization
    # BMI < 18.50 : Underweight
    # BMI >= 18.50 or BMI <= 24.90 : Normal
    # BMI >= 25.00 or BMI <= 29.90 : Overweight
    # BMI >= 30.00 or BMI <= 34.90 : Obesity class I
    # BMI >= 35.00 or BMI <= 39.90 : Obesity class II
    # BMI >= 40.00 : Obesity class III 

ibuhamil = [
    {'RM': 330421567, 'Nama' : 'Tania', 'TD Sistole' : 100, 'TD Diastole' : 60, 'BB' : 55, 'TB' : 165},
    {'RM': 330421568, 'Nama' : 'Indira', 'TD Sistole' : 200, 'TD Diastole' : 100, 'BB' : 70, 'TB' : 163},
    {'RM': 330421569, 'Nama' : 'Jayanti', 'TD Sistole' : 160, 'TD Diastole' : 90, 'BB' : 65, 'TB' : 167},
    {'RM': 330421570, 'Nama' : 'Deviani', 'TD Sistole' : 190, 'TD Diastole' : 90, 'BB' : 70, 'TB' : 160},
    {'RM': 330421571, 'Nama' : 'Ratna', 'TD Sistole' : 120, 'TD Diastole' : 80, 'BB' : 60, 'TB' : 167},
    {'RM': 330421572, 'Nama' : 'Sridevi', 'TD Sistole' : 138, 'TD Diastole' : 90, 'BB' : 60, 'TB' : 167}
]

def welcome_menu() :
    menu = '''
    \n\t\t🏥 APLIKASI SKRINING RS IBU DAN ANAK 🏥\n\n
        1. Tampilkan Pasien Hamil Trimester I
        2. Tambahkan Pasien
        3. Ubah Data Pasien
        4. Skrining Hipertensi dan Preeklampsia  
        5. Skrining BMI 
        6. Hapus Data Pasien
        7. Exit\n\n'''
    print(menu)

def banner_atas():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\t\t\tData Ibu Hamil Trimester I RS Digital Ibu dan Anak')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def data_ps():
    for j,i in enumerate(ibuhamil) : 
        print(f"|{j+1}.| RM: {i['RM']} | Nama: {i['Nama']}\t| TD Sistole: {i['TD Sistole']}\t| TD Diastole: {i['TD Diastole']}\t| BB: {i['BB']} kg | TB: {i['TB']} cm |")

def banner_bawah():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def tampilkan_ps():
    print("\n============================== TAMPILKAN DATA PASIEN ==================================\n")
    print('\t1. Tampilkan Seluruh Pasien Hamil Trimester I')
    print('\t2. Tampilkan Data Pasien yang Dipilih')
    print('\t3. Kembali ke Menu Utama')
    choose_menu1 = int(input('\n\tSilakan Pilih Menu [1-3]: '))

    #MASUK SUB MENU 1.1
    #MEMERIKSA KETERSEDIAAN DATA
    if choose_menu1 == 1:
        if len(ibuhamil) != 0:
            print('\n')
            banner_atas()
            data_ps()
            banner_bawah()
            print('\n')
            return tampilkan_ps()
        else:
            print('\n\t🔴 Data Pasien Kosong! 🔴\n')
            return tampilkan_ps()
    
    #MASUK SUB MENU 1.2
    #MENGECEK DATA PASIEN TERPILIH
    elif choose_menu1 == 2:
        if len(ibuhamil) != 0:
            rm_pasien = int(input('\nMasukkkan Nomer Rekam Medis: '))
            print(f'\nPasien dengan RM: {rm_pasien}')
            list_rm = [] 
            for i in range(len(ibuhamil)):
                list_rm.append(ibuhamil[i]['RM'])
            if rm_pasien in list_rm:
                print(f"{list_rm.index(rm_pasien)+1}. RM:{rm_pasien}, Nama: {ibuhamil[list_rm.index(rm_pasien)]['Nama']}, TD Sistole: {ibuhamil[list_rm.index(rm_pasien)]['TD Sistole']}, TD Diastole: {ibuhamil[list_rm.index(rm_pasien)]['TD Diastole']}, BB: {ibuhamil[list_rm.index(rm_pasien)]['BB']}, TB: {ibuhamil[list_rm.index(rm_pasien)]['TB']}")
                return tampilkan_ps()
            else :
                print(f'Data Pasien Dengan RM {rm_pasien} Tidak Tersedia. Mohon tambahkan data pasien.\n')
                return tambah_ps()
    elif choose_menu1 == 3:
        return choose_menu()

    #PERINGATAN
    else :
        print('\n🔴 Periksa kembali angka yang dimasukkan 🔴\n')
        return tampilkan_ps()

def tambah_ps():
    print("\n============================== TAMBAHKAN PASIEN ===============================\n")
    print('\t1. Tambahkan Data Pasien')
    print('\t2. Kembali ke Menu Utama')
    #MENU [Tambahkan Data Pasien]
    #MASUK MENU 2
    while 1:
        choose_menu2 = int(input('\nSilakan Pilih Menu [1-2]: \n'))

        #MASUK SUB MENU 2.1
        if choose_menu2 == 1:
            dict_psbaru = {}
            while 1:
                dict_psbaru['RM']= int(input('Masukkan RM pasien (9 digit angka): '))
                if len(str(dict_psbaru['RM'])) != 9:
                    print('🔴 RM yang anda input tidak 9 digit! 🔴')
                    continue
                else:
                    list_rm = []
                    for i in range(len(ibuhamil)):
                        list_rm.append(ibuhamil[i]['RM'])

                    #Pengecekan data RM duplikat
                    if dict_psbaru['RM'] not in list_rm:
                        dict_psbaru['Nama'] = input('\nMasukkan nama pasien: ').capitalize()
                        if dict_psbaru['Nama'] != ' ' :
                            #Lengkapi data pasien baru
                            dict_psbaru['TD Sistole']= int(input('\nMasukkan nilai tekanan darah sistole: '))
                            dict_psbaru['TD Diastole']= int(input('Masukkan nilai tekanan darah diastole: '))
                            dict_psbaru['BB']= int(input('Masukkan berat badan dalam kg: '))
                            dict_psbaru['TB']= int(input('Masukkan tinggi badan dalam cm: '))

                            #Konfirmasi penambahan data pasien baru
                            while 1:
                                tambah = input('Tekan Y untuk menambah dan N untuk membatalkan: ').capitalize()
                                if tambah == 'Y' :
                                    ibuhamil.append(dict_psbaru)
                                    print('\nPasien Baru Berhasil Ditambahkan ✅\n')
                                    return tambah_ps()
                                elif tambah == 'N':
                                    dict_psbaru.clear()
                                    print('\nData Pasien Dibatalkan ❌\n')
                                    return tambah_ps()
                                else:
                                    print('🔴 Masukkan hanya Y atau N! 🔴\n')
                                    
                    #JIKA DATA SUDAH ADA
                    else:
                        print('\n🔴 Maaf, Nomer Rekam Medik Sudah Terpakai 🔴\n')
                        return tambah_ps()

        #KELUAR DARI SUB MENU 2
        elif choose_menu2 == 2: 
            return choose_menu()
    
        #PERINGATAN
        else:
            print('\n🔴 Anda Hanya Dapat Memilih 1 Atau 2! 🔴\n')
            continue

def ubah_ps():
    print("\n============================== UBAH DATA PASIEN ==================================\n")
    print('\t1. Ubah Data Pasien')
    print('\t2. Kembali ke Menu Utama')
    #MENU 3 [Ubah Data Pasien]
    while 1: 
        choose_menu3 = int(input('\nSilakan Pilih Menu [1-2]: \n'))
        #MASUK SUB-MENU 3.1
        if choose_menu3 == 1:
            if len(ibuhamil) != 0:
                banner_atas()
                data_ps()
                banner_bawah()
                rm_pasien= int(input('\nMasukkan RM Pasien (9 digit): '))
                print(f'Pasien dengan RM: {rm_pasien}')

                list_rm = []
                for i in range(len(ibuhamil)):
                    list_rm.append(ibuhamil[i]['RM'])

                if rm_pasien in list_rm:
                    print(f"{list_rm.index(rm_pasien)+1}. RM:{rm_pasien}, Nama: {ibuhamil[list_rm.index(rm_pasien)]['Nama']}, TD Sistole: {ibuhamil[list_rm.index(rm_pasien)]['TD Sistole']}, TD Diastole: {ibuhamil[list_rm.index(rm_pasien)]['TD Diastole']}, BB: {ibuhamil[list_rm.index(rm_pasien)]['BB']}, TB: {ibuhamil[list_rm.index(rm_pasien)]['TB']}")
                    while 1:
                        ubahdata = input('Tekan Y untuk ubah dan N untuk batal: ').capitalize()
                        if ubahdata == 'Y':
                            list_rm = []
                            for i in range(len(ibuhamil)):
                                list_rm.append(ibuhamil[i]['RM'])
                            print('\n... ... ... Proses Ubah Data Dimulai ... ... ...\n')
                            dataGanti = ibuhamil[list_rm.index(rm_pasien)]
                            while 1:
                                keyGanti = str(input('\nMasukkan Data yang Ingin Diganti (BB/TB/TD SISTOLE/TD DIASTOLE): ')).upper()

                                #MENGUBAH BB
                                if keyGanti == 'BB':
                                    bbBaru = int(input('\nMasukkan BB anda yang terakhir: '))
                                    while 1:
                                        update = input('Tekan Y untuk update dan N untuk batal! ').capitalize()
                                        if update == 'Y':
                                            dataGanti['BB'] = bbBaru
                                            strGanti = f"RM: {dataGanti['RM']}, Nama: {dataGanti['Nama']}, TD Sistole: {dataGanti['TD Sistole']}, TD Diastole: {dataGanti['TD Diastole']}, BB: {dataGanti['BB']}, TB: {dataGanti['TB']}"
                                            print ('\nBerat Badan Berhasil Diganti ✅\nLihat Data Terbaru Pasien :\n')
                                            print(strGanti)
                                            return ubah_ps()
                                        elif update == 'N':
                                            print('\n** Ubah BB Dibatalkan ❌ **\n')
                                            return ubah_ps()
                                        else:
                                            print('\n🔴 Anda Hanya dapat menekan Y atau N 🔴\n')
                                            return ubah_ps()
                                #MENGUBAH TB
                                elif keyGanti == 'TB':
                                    tbBaru = int(input('\nMasukkan TB anda yang terakhir: '))
                                    while 1:
                                        update = input('\nUpdate sekarang (Y/N) ?').capitalize()
                                        if update == 'Y':
                                            dataGanti['TB'] = tbBaru
                                            strGanti = f"RM: {dataGanti['RM']}, Nama: {dataGanti['Nama']}, TD Sistole: {dataGanti['TD Sistole']}, TD Diastole: {dataGanti['TD Diastole']}, BB: {dataGanti['BB']}, TB: {dataGanti['TB']}"
                                            print ('Tinggi Badan Berhasil Diganti ✅\nLihat Data Terbaru Pasien :\n')
                                            print(strGanti)
                                            return ubah_ps()
                                        elif update == 'N':
                                            print('\n** Ubah TB Dibatalkan ❌ **\n')
                                            return ubah_ps()
                                        else:
                                            print('\n🔴 Anda Hanya dapat menekan Y atau N 🔴\n')
                                            return ubah_ps()
                                    
                                #MENGUBAH TD Sistole
                                elif keyGanti == 'TD SISTOLE':
                                    tdsBaru = int(input('\nMasukkan TD Sistole anda yang terakhir: '))
                                    while 1:
                                        update = input('\nUpdate sekarang (Y/N)? ').capitalize()
                                        if update == 'Y':
                                            dataGanti['TD Sistole'] = tdsBaru
                                            strGanti = f"RM: {dataGanti['RM']}, Nama: {dataGanti['Nama']}, TD Sistole: {dataGanti['TD Sistole']}, TD Diastole: {dataGanti['TD Diastole']}, BB: {dataGanti['BB']}, TB: {dataGanti['TB']}"
                                            print ('\nTD Sistole Berhasil Diganti ✅\nLihat Data Terbaru Pasien :\n')
                                            print(strGanti)
                                            return ubah_ps()
                                        elif update == 'N':
                                            print('\n** Ubah TD Sistole Dibatalkan ❌ **')
                                            return ubah_ps()
                                        else:
                                            print('\n🔴 Anda Hanya dapat menekan Y atau N 🔴\n')
                                            return ubah_ps()
                                    
                                #MENGUBAH TD Diastole
                                elif keyGanti == 'TD DIASTOLE':
                                    tddBaru = int(input('\nMasukkan TD Diastole anda yang terakhir: '))
                                    while 1:
                                        update = input('\nUpdate sekarang (Y/N) ?').capitalize()
                                        if update == 'Y':
                                            dataGanti['TD Diastole'] = tddBaru
                                            strGanti = f"RM: {dataGanti['RM']}, Nama: {dataGanti['Nama']}, TD Sistole: {dataGanti['TD Sistole']}, TD Diastole: {dataGanti['TD Diastole']}, BB: {dataGanti['BB']}, TB: {dataGanti['TB']}"
                                            print ('\nTD Diastole Berhasil Diganti ✅\nLihat Data Terbaru Pasien :\n')
                                            print(strGanti)
                                            return ubah_ps()
                                        elif update == 'N':
                                            print('\n** Ubah TD Diastole Dibatalkan ❌ **')
                                            return ubah_ps()
                                        else:
                                            print('\nAnda Hanya dapat menekan Y atau N\n')
                                            return ubah_ps()        
                                else:
                                    print('\n 🔴 Anda hanya dapat mengubah BB, TB, TD Sistole, dan TD Diastole! 🔴\n')
                                    continue

                        #BATAL KE MENU UBAH
                        #KEMBALI KE SUB-MENU 3
                        elif ubah_ps == 'N':
                            print('\nBatal ke Menu Ubah Data\n')
                            return choose_menu()

                        #PERINGATAN SALAH SAAT LOOPING
                        else:
                            print('\n🔴 Anda Hanya Boleh Menekan Y atau N! 🔴\n')
                            return choose_menu()
                #BILA RM BELUM TERSEDIA
                else:
                    print(f'\n\t🔴 Data dengan nomer RM {rm_pasien} tidak tersedia\nTambahkan Pasien Terlebih Dahulu! \n')
                    return tambah_ps()

            #JIKA DATA PASIEN KOSONG
            else:
                print('\n\t🔴 Data Pasien Kosong, Tambahkan Pasien Terlebih Dahulu! 🔴\n')
                return tambah_ps()
        #KELUAR DARI SUB-MENU 3
        elif choose_menu3 == 2:
            return choose_menu()
        else:
            print('\n🔴 Masukkan Hanya 1 Atau 2! 🔴\n')
            continue

def hipertensi_ps():
    print("\n====================== SKRINING HIPERTENSI & PREEKLAMPSIA ========================\n")
    print('\t1. Periksa Risiko Hipertensi dan Preeklampsia')
    print('\t2. Kembali ke Menu Utama')
    #MENU SKRINING TEKANAN DARAH PASIEN
    #MASUK MENU 4
    while 1:
        choose_menu4 = int(input('\nSilakan Pilih Menu [1-2]: '))
        #MASUK SUB-MENU 4.1 --> Periksa Status Hipertensi
        if choose_menu4 == 1:
            if len(ibuhamil) != 0:
                banner_atas()
                data_ps()
                banner_bawah()
                while 1:
                    rmTensi = int(input('\nSilakan Masukkan RM Pasien (9 digit): \n'))
                    list_rm = []
                    for i in range(len(ibuhamil)):
                        list_rm.append(ibuhamil[i]['RM'])
                    
                    if rmTensi in list_rm:
                        print('...Skrining Tekanan Darah Dimulai...')
                        while 1:
                            confirm = input('Tekan Y untuk lanjut dan N untuk batal: ').capitalize()
                            if confirm == 'Y':
                                #Skrining Tekanan Darah Pasien
                                namapasien = ibuhamil[list_rm.index(rmTensi)]['Nama']
                                indexingtensi = ibuhamil[list_rm.index(rmTensi)]
                                tdsistole = indexingtensi['TD Sistole']
                                tddiastole = indexingtensi['TD Diastole']
                                MAP = ((2*tddiastole + tdsistole)/3)
                                #Laporan Hasil Skrining Hipertensi & Preeklampsia
                                print('--------------------------------------------------------------------------')
                                print('\n\t\tHasil Pemeriksaan Skrining Tekanan Darah\n')
                                print('--------------------------------------------------------------------------')
                                print(f'Pasien ibu hamil berikut;\nNama: {namapasien}\nTD Sistole: {tdsistole} mmHg\nTD Diastole: {tddiastole} mmHg')

                                if tdsistole <=120 and tddiastole <=80:
                                    risikoRendah()
                                elif tdsistole < 90 and tddiastole < 60:
                                    risikoLain()
                                elif tdsistole <140  and tddiastole <90:
                                    print('\nStatus Hasil:\nPrahipertensi\n')
                                    if MAP > 90 :
                                        risikoSedang()
                                    else:
                                        risikoTinggi()
                                elif tdsistole <160  and tddiastole <100:
                                    print('\nStatus Hasil:\nHipertensi tingkat I\n')
                                    if MAP > 100 :
                                        risikoTinggi()
                                    else:
                                        risikoSedang()
                                else:
                                    print('\nStatus Hasil:\nHipertensi tingkat II\n')
                                    if MAP > 100 :
                                        risikoTinggi()
                                    else:
                                        risikoSedang()
                            elif confirm == 'N':
                                return hipertensi_ps()
                            else:
                                print('Harap Masukkan Y atau N saja!')
                                continue                 
                    else:
                        print(f'\nData pasien dengan RM {rmTensi} tidak tersedia!\nTambahkan pasien terlebih dahulu.\n')
                        return tambah_ps()
            else:
                print('\n\t🔴 Data Pasien Kosong, Tambahkan Terlebih Dahulu! 🔴\n')
                return tambah_ps()

        #KELUAR DARI SUB-MENU 4
        elif choose_menu4 == 2:
            return choose_menu()

        else:
            print('\n🔴 Anda Hanya Bisa Memasukkan 1 atau 2! 🔴\n')
            continue

def bmi_ps():
    print("\n============================== SKRINING BMI ==================================\n")
    print('\t1. Hitung BMI Pasien')
    print('\t2. Kembali ke Menu Utama')
    #MENU HITUNG BMI PASIEN
    #MASUK MENU 5
    while 1:
        choose_menu5 = int(input('\nSilakan Pilih Menu [1-2]: '))
        #MASUK SUB-MENU 5.1
        if choose_menu5 == 1:
            if len(ibuhamil) != 0:
                banner_atas()
                data_ps()
                banner_bawah()
                while 1:
                    rmbmi = int(input('\nSilakan Masukkan RM Pasien: \n'))
                    list_rm = []
                    for i in range(len(ibuhamil)):
                        list_rm.append(ibuhamil[i]['RM'])
                    
                    if rmbmi in list_rm:
                        print('...Hitung BMI Akan Dimulai...')
                        while 1:
                            confirm = input('Tekan Y untuk memproses dan N untuk membatalkan: ').capitalize()
                            if confirm == 'Y':
                                #Hitung BMI Pasien
                                namapasien = ibuhamil[list_rm.index(rmbmi)]['Nama']
                                indexingbmi = ibuhamil[list_rm.index(rmbmi)]
                                beratbadan = indexingbmi['BB']
                                tinggibadan = indexingbmi['TB']
                                BMI = (beratbadan/((tinggibadan/100)**2))
                                print('--------------------------------------------------------------------------------')
                                print('\t\tKlasifikasi BMI Berdasarkan World Health Organization')
                                print('--------------------------------------------------------------------------------')
                                print(f'\nPasien ibu hamil berikut;\nNama: {namapasien}\nBB: {beratbadan} kg\nTinggi: {tinggibadan} cm')
                                print(f'\nBMI pasien: {BMI: .2f}')

                                #Status BMI 
                                if BMI < 18.50:
                                    print('Status Hasil: Underweight')
                                    return bmi_ps()
                                elif BMI >= 18.50 and BMI <= 24.90:
                                    print('Status Hasil: Normal Weight')
                                    return bmi_ps()
                                elif BMI >= 25.00 or BMI <= 29.90:
                                    print('Status Hasil: Overweight')
                                    return bmi_ps()
                                elif BMI >= 30.00 or BMI <= 34.90:
                                    print('Status Hasil: Obesity class I')
                                    return bmi_ps()
                                elif BMI >= 35.00 or BMI <= 39.90:
                                    print('Status Hasil: Obesity class II')
                                    return bmi_ps()
                                elif BMI >= 40.00:
                                    print('Status Hasil: Obesity class III')
                                    return bmi_ps()

                            elif confirm == 'N':
                                return bmi_ps()
                            else:
                                print('🔴 Harap Masukkan Y atau N saja! 🔴')
                                continue
                    else:
                        print(f'\n🔴 Data pasien dengan RM {rmbmi} tidak tersedia!\nTambahkan pasien terlebih dahulu.\n')
                        return tambah_ps()
            else:
                print('\n\t🔴 Data Pasien Kosong\nTambahkan pasien terlebih dahulu.\n')
                return tambah_ps()

        #KELUAR DARI SUB-MENU 5
        elif choose_menu5 == 2:
            return choose_menu()

        else:
            print('\n🔴 Anda Hanya Dapat Memasukkan 1 Atau 2! 🔴\n')
            continue

def hapus_ps():
    print("\n============================== HAPUS DATA PASIEN ==================================\n")
    print('\t1. Hapus Data Pasien')
    print('\t2. Kembali ke Menu Utama')
    #MENU HAPUS DATA PASIEN
    #MASUK MENU 6
    while 1:
        choose_menu6 = int(input('\nSilakan Pilih Menu [1-2]: '))
        #MASUK SUB-MENU 6.1
        if choose_menu6 == 1:
            if len(ibuhamil) != 0:
                banner_atas()
                data_ps()
                banner_bawah()
                while 1:
                    confirm = int(input('\nSilakan Masukkan RM Pasien Yang Ingin Dihapus: '))
                    list_rm = []
                    for i in range(len(ibuhamil)):
                        list_rm.append(ibuhamil[i]['RM'])
                    if confirm in list_rm:
                        perintah = input('Tekan Y untuk hapus dan N untuk batal: ').capitalize()
                        if perintah == 'Y':
                            del ibuhamil[list_rm.index(confirm)]
                            banner_atas()
                            data_ps()
                            print(f'\nData dengan RM {confirm} Berhasil Dihapus ✅\n')
                            return hapus_ps()
                        elif perintah == 'N':
                            return hapus_ps()
                        else:
                            print('\n🔴 Masukkan Hanya Y atau N saja! 🔴\n')
                            continue
                    else:
                        print(f'\nRM {confirm} Tidak Ada Dalam Sistem!\n')
                        return choose_menu()
            else:
                print('\n🔴 Data Pasien Tidak Tersedia 🔴\n')
                return choose_menu()
        elif choose_menu6 == 2:
            return choose_menu()
        else:
            print('\n🔴 Anda Hanya Dapat Memasukkan 1 Atau 2! 🔴\n')
            continue

def choose_menu():
    welcome_menu()
    choose_menu = int(input('Silakan Pilih Menu [1-7]: '))
    if choose_menu == 1:
        tampilkan_ps()
    elif choose_menu == 2:
        tambah_ps()
    elif choose_menu == 3:
        ubah_ps()
    elif choose_menu == 4:
        hipertensi_ps()
    elif choose_menu == 5:
        bmi_ps()
    elif choose_menu == 6:
        hapus_ps()
    elif choose_menu == 7:
        print('\n\t👩🏼‍⚕️ TERIMA KASIH, SEMOGA LEKAS SEMBUH 👨🏼‍⚕️\t\n')
    else:
        print('🔴 Anda Hanya Dapat Memilih Menu 1-7 🔴')
choose_menu()

       
             
