# Auto-Submit-Waitlist
Ini Cara Untuk Mengisi Whitelist Airdrop di Website Dengan Banyak Email

### Untuk Menjalankan Ini pastikan Kalian Sudah Install Python & git di Pc Kalian

### 1. Buka Vscode Anda Atau Buka Terminal Kalian dan Install Bahan

```
pip install pandas selenium time
```

```
git clone https://github.com/bangpateng/Auto-Submit-Waitlist
```
```
cd Auto-Submit-Waitlist
```
```
ls
nano emaildata.csv
```
Masukan Data Email Email Yang Kalian Gunakan `CTRL` + `X` `Y` `ENTER` Untuk Save


```
ls
nano main.py
```
- Ganti Bagian `INI_ISI_DENGAN_DIREKTORY_PATH_CHROME_DRIVER_ANDA` dengan Lokasi Path Kalian
- Contoh : C:/Users/BANG PATENG/Downloads/chromedriver_win32/chromedriver.exe
- Download Jika Anda Belom memilikinya di : https://chromedriver.chromium.org/downloads
- Pilih Sesuai Versi Google Chrome Yang Kalian Pakai Lalu `Extract` dan Lihat di mana lokasi Filenya
- Masukan Jalur Path nya dan `CTRL` + `X` `Y` `ENTER` Untuk Save


### 2. Mulai Jalankan

```
python main.py
atau
python3 main.py
```

- Masukan Link Website Waitlist `ENTER`
- Masukan XPATH Email (Silahkan Kalian Inspect Element di Bagian Tempat Isi Email dan Copy XPATH) Masukan ke Terminal
- Masukan XPATH Button (Silahkan Kalian Inspect Element di Bagian Button Tombol Join Waitlist dan Copy XPATH) Masukan ke Terminal
- `ENTER` dan Auto Script Berjalan
- Done, Selesai

Note : Script Ini Berjalan di Website Yang hanya Mengisi Email dan Klik Join Waitlist Saja (Tanpa Ada Verifikasi Email)
