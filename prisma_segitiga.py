import tkinter as tk

def hitung_volume_prisma_segitiga():
    try:
        alas = float(alas_entry.get())
        tinggi_segitiga = float(tinggi_segitiga_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())
        volume = (1/2) * alas * tinggi_segitiga * tinggi_prisma
        hasil_volume_prisma_segitiga.config(text=f"Volume Prisma Segitiga: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_prisma_segitiga.config(text="Masukkan angka yang valid untuk alas dan tinggi.")

def hitung_luas_permukaan_prisma_segitiga():
    try:
        alas = float(alas_entry.get())
        tinggi_segitiga = float(tinggi_segitiga_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())
        luas_permukaan = (2 * alas * tinggi_segitiga) + (alas * tinggi_prisma) + (3 * alas * tinggi_segitiga)
        hasil_luas_permukaan_prisma_segitiga.config(text=f"Luas Permukaan Prisma Segitiga: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_prisma_segitiga.config(text="Masukkan angka yang valid untuk alas dan tinggi.")

app = tk.Tk()
app.title("Kalkulator Prisma Segitiga")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

alas_label = tk.Label(frame, text="Alas Segitiga (cm):")
alas_label.grid(row=0, column=0, sticky="w")
alas_entry = tk.Entry(frame)
alas_entry.grid(row=0, column=1)

tinggi_segitiga_label = tk.Label(frame, text="Tinggi Segitiga (cm):")
tinggi_segitiga_label.grid(row=1, column=0, sticky="w")
tinggi_segitiga_entry = tk.Entry(frame)
tinggi_segitiga_entry.grid(row=1, column=1)

tinggi_prisma_label = tk.Label(frame, text="Tinggi Prisma (cm):")
tinggi_prisma_label.grid(row=2, column=0, sticky="w")
tinggi_prisma_entry = tk.Entry(frame)
tinggi_prisma_entry.grid(row=2, column=1)

hitung_volume_prisma_segitiga_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_prisma_segitiga)
hitung_volume_prisma_segitiga_button.grid(row=3, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_prisma_segitiga_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_prisma_segitiga)
hitung_luas_permukaan_prisma_segitiga_button.grid(row=4, column=0, columnspan=2, pady=5)

hasil_volume_prisma_segitiga = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_prisma_segitiga.grid(row=5, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_prisma_segitiga = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_prisma_segitiga.grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()
