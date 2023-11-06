import tkinter as tk

def hitung_volume_limas_segitiga():
    try:
        alas_segitiga = float(alas_segitiga_entry.get())
        tinggi_segitiga = float(tinggi_segitiga_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        volume = (1/3) * (1/2) * alas_segitiga * tinggi_segitiga * tinggi_limas
        hasil_volume_limas_segitiga.config(text=f"Volume Limas Segitiga: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_limas_segitiga.config(text="Masukkan angka yang valid untuk alas segitiga dan tinggi.")

def hitung_luas_permukaan_limas_segitiga():
    try:
        alas_segitiga = float(alas_segitiga_entry.get())
        tinggi_segitiga = float(tinggi_segitiga_entry.get())
        tinggi_limas = float(tinggi_limas_entry.get())
        luas_permukaan = (1/2) * alas_segitiga * tinggi_segitiga + 3 * ((1/2) * alas_segitiga * tinggi_limas)
        hasil_luas_permukaan_limas_segitiga.config(text=f"Luas Permukaan Limas Segitiga: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_limas_segitiga.config(text="Masukkan angka yang valid untuk alas segitiga dan tinggi.")

app = tk.Tk()
app.title("Kalkulator Limas Segitiga")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

alas_segitiga_label = tk.Label(frame, text="Alas Segitiga (cm):")
alas_segitiga_label.grid(row=0, column=0, sticky="w")
alas_segitiga_entry = tk.Entry(frame)
alas_segitiga_entry.grid(row=0, column=1)

tinggi_segitiga_label = tk.Label(frame, text="Tinggi Segitiga (cm):")
tinggi_segitiga_label.grid(row=1, column=0, sticky="w")
tinggi_segitiga_entry = tk.Entry(frame)
tinggi_segitiga_entry.grid(row=1, column=1)

tinggi_limas_label = tk.Label(frame, text="Tinggi Limas (cm):")
tinggi_limas_label.grid(row=2, column=0, sticky="w")
tinggi_limas_entry = tk.Entry(frame)
tinggi_limas_entry.grid(row=2, column=1)

hitung_volume_limas_segitiga_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_limas_segitiga)
hitung_volume_limas_segitiga_button.grid(row=3, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_limas_segitiga_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_limas_segitiga)
hitung_luas_permukaan_limas_segitiga_button.grid(row=4, column=0, columnspan=2, pady=5)

hasil_volume_limas_segitiga = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_limas_segitiga.grid(row=5, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_limas_segitiga = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_limas_segitiga.grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()
