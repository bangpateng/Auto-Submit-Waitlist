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


- Download Chrome Driver : https://chromedriver.chromium.org/downloads
- Pastikan Chrome Driver Yang di Download Pilih Sesuai Versi Google Chrome Yang Kalian Pakai


### 2. Mulai Jalankan

```
main.py
```

- Masukan Link Website Waitlist `ENTER`
- Masukan XPATH Email (Silahkan Kalian Inspect Element di Bagian Tempat Isi Email dan Copy XPATH) Masukan ke Terminal
- Masukan XPATH Button (Silahkan Kalian Inspect Element di Bagian Button Tombol Join Waitlist dan Copy XPATH) Masukan ke Terminal
- `ENTER` dan Auto Script Berjalan
- Done, Selesai

Note : Script Ini Berjalan di Website Yang hanya Mengisi Email dan Klik Join Waitlist Saja (Tanpa Ada Verifikasi Email)
