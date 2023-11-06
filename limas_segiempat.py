import tkinter as tk

def hitung_volume_limas_segiempat():
    try:
        panjang_alas = float(panjang_alas_entry.get())
        lebar_alas = float(lebar_alas_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        volume = (1/3) * panjang_alas * lebar_alas * tinggi_limas
        hasil_volume_limas_segiempat.config(text=f"Volume Limas Segiempat: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_limas_segiempat.config(text="Masukkan angka yang valid untuk panjang alas, lebar alas, dan tinggi limas.")

def hitung_luas_permukaan_limas_segiempat():
    try:
        panjang_alas = float(panjang_alas_entry.get())
        lebar_alas = float(lebar_alas_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        luas_permukaan = panjang_alas * lebar_alas + 4 * ((1/2) * panjang_alas * tinggi_limas)
        hasil_luas_permukaan_limas_segiempat.config(text=f"Luas Permukaan Limas Segiempat: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_limas_segiempat.config(text="Masukkan angka yang valid untuk panjang alas, lebar alas, dan tinggi limas.")

app = tk.Tk()
app.title("Kalkulator Limas Segiempat")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

panjang_alas_label = tk.Label(frame, text="Panjang Alas (cm):")
panjang_alas_label.grid(row=0, column=0, sticky="w")
panjang_alas_entry = tk.Entry(frame)
panjang_alas_entry.grid(row=0, column=1)

lebar_alas_label = tk.Label(frame, text="Lebar Alas (cm):")
lebar_alas_label.grid(row=1, column=0, sticky="w")
lebar_alas_entry = tk.Entry(frame)
lebar_alas_entry.grid(row=1, column=1)

tinggi_limas_label = tk.Label(frame, text="Tinggi Limas (cm):")
tinggi_limas_label.grid(row=2, column=0, sticky="w")
tinggi_limas_entry = tk.Entry(frame)
tinggi_limas_entry.grid(row=2, column=1)

hitung_volume_limas_segiempat_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_limas_segiempat)
hitung_volume_limas_segiempat_button.grid(row=3, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_limas_segiempat_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_limas_segiempat)
hitung_luas_permukaan_limas_segiempat_button.grid(row=4, column=0, columnspan=2, pady=5)

hasil_volume_limas_segiempat = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_limas_segiempat.grid(row=5, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_limas_segiempat = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_limas_segiempat.grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()
