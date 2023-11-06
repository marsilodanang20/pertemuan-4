import tkinter as tk

def hitung_volume():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    volume = panjang * lebar * tinggi
    hasil_volume.config(text=f"Volume: {volume} cm³")

def hitung_luas_permukaan():
    panjang = float(panjang_entry.get())
    lebar = float(lebar_entry.get())
    tinggi = float(tinggi_entry.get())
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    hasil_luas_permukaan.config(text=f"Luas Permukaan: {luas_permukaan} cm²")

app = tk.Tk()
app.title("Kalkulator Balok")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

panjang_label = tk.Label(frame, text="Panjang (cm):")
panjang_label.grid(row=0, column=0, sticky="w")
panjang_entry = tk.Entry(frame)
panjang_entry.grid(row=0, column=1)

lebar_label = tk.Label(frame, text="Lebar (cm):")
lebar_label.grid(row=1, column=0, sticky="w")
lebar_entry = tk.Entry(frame)
lebar_entry.grid(row=1, column=1)

tinggi_label = tk.Label(frame, text="Tinggi (cm):")
tinggi_label.grid(row=2, column=0, sticky="w")
tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=2, column=1)

hitung_volume_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.grid(row=3, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
hitung_luas_permukaan_button.grid(row=4, column=0, columnspan=2, pady=5)

hasil_volume = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume.grid(row=5, column=0, columnspan=2, pady=10)

hasil_luas_permukaan = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan.grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()
