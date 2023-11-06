import tkinter as tk

def hitung_volume_tabung():
    try:
        radius = float(radius_entry.get())
        tinggi = float(tinggi_entry.get())
        volume = 3.141592653589793 * (radius ** 2) * tinggi
        hasil_volume_tabung.config(text=f"Volume Tabung: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_tabung.config(text="Masukkan angka yang valid untuk radius dan tinggi.")

def hitung_luas_permukaan_tabung():
    try:
        radius = float(radius_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_permukaan = 2 * 3.141592653589793 * radius * (radius + tinggi)
        hasil_luas_permukaan_tabung.config(text=f"Luas Permukaan Tabung: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_tabung.config(text="Masukkan angka yang valid untuk radius dan tinggi.")

app = tk.Tk()
app.title("Kalkulator Tabung (Silinder)")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

radius_label = tk.Label(frame, text="Radius (cm):")
radius_label.grid(row=0, column=0, sticky="w")
radius_entry = tk.Entry(frame)
radius_entry.grid(row=0, column=1)

tinggi_label = tk.Label(frame, text="Tinggi (cm):")
tinggi_label.grid(row=1, column=0, sticky="w")
tinggi_entry = tk.Entry(frame)
tinggi_entry.grid(row=1, column=1)

hitung_volume_tabung_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_tabung)
hitung_volume_tabung_button.grid(row=2, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_tabung_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_tabung)
hitung_luas_permukaan_tabung_button.grid(row=3, column=0, columnspan=2, pady=5)

hasil_volume_tabung = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_tabung.grid(row=4, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_tabung = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_tabung.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
