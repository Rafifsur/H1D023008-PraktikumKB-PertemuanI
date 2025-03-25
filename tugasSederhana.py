import random
import datetime

def main():
    print("=== PROGRAM MANAJEMEN TUGAS SEDERHANA ===")
    print(f"Hari ini: {datetime.datetime.now().strftime('%A, %d %B %Y')}\n")
    
    # Struktur data: dictionary untuk menyimpan tugas
    daftar_tugas = {
        "Belajar Python": "Belajar konsep dasar Python",
        "Praktikum KB": "Mengerjakan tugas praktikum",
        "Olahraga": "Lari pagi 30 menit"
    }
    
    # Struktur kontrol: perulangan while untuk menu interaktif
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Hapus Tugas")
        print("4. Rekomendasi Tugas Acak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        # Struktur kontrol: percabangan if-elif-else
        if pilihan == "1":
            judul = input("Masukkan judul tugas: ")
            deskripsi = input("Masukkan deskripsi tugas: ")
            daftar_tugas[judul] = deskripsi
            print(f"Tugas '{judul}' berhasil ditambahkan!")
            
        elif pilihan == "2":
            print("\nDaftar Tugas:")
            for i, (judul, deskripsi) in enumerate(daftar_tugas.items(), 1):
                print(f"{i}. {judul}: {deskripsi}")
                
        elif pilihan == "3":
            print("\nDaftar Tugas yang bisa dihapus:")
            tugas_list = list(daftar_tugas.keys())
            for i, judul in enumerate(tugas_list, 1):
                print(f"{i}. {judul}")
            
            try:
                nomor = int(input("Pilih nomor tugas yang akan dihapus: ")) - 1
                if 0 <= nomor < len(tugas_list):
                    judul = tugas_list[nomor]
                    del daftar_tugas[judul]
                    print(f"Tugas '{judul}' berhasil dihapus!")
                else:
                    print("Nomor tidak valid!")
            except ValueError:
                print("Masukkan angka yang valid!")
                
        elif pilihan == "4":
            if daftar_tugas:
                tugas_acak = random.choice(list(daftar_tugas.keys()))
                print(f"\nRekomendasi tugas untuk dikerjakan sekarang: {tugas_acak}")
                print(f"Deskripsi: {daftar_tugas[tugas_acak]}")
            else:
                print("Tidak ada tugas yang tersedia!")
                
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")

if __name__ == "__main__":
    main()