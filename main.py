from datetime import datetime

nama = input("nama kamu: ")
tanggal_lahir = input("tanggal lahir kamu (format: DD-MM-YYYY): ")

lahir = datetime.strptime(tanggal_lahir, "%d-%m-%Y")
sekarang = datetime.today()
umur = sekarang.year - lahir.year - (
    (sekarang.month, sekarang.day) < (lahir.month, lahir.day))

print(f"Halo {nama}, umur Anda {umur} tahun.")