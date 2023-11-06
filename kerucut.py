import tkinter as tk

def hitung_volume_kerucut():
    try:
        radius = float(radius_entry.get())
        tinggi = float(tinggi_entry.get())
        volume = (1/3) * 3.141592653589793 * (radius ** 2) * tinggi
        hasil_volume_kerucut.config(text=f"Volume Kerucut: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_kerucut.config(text="Masukkan angka yang valid untuk radius dan tinggi kerucut.")

def hitung_luas_permukaan_kerucut():
    try:
        radius = float(radius_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_permukaan = 3.141592653589793 * radius * (radius + (radius**2 + tinggi**2)**0.5)
        hasil_luas_permukaan_kerucut.config(text=f"Luas Permukaan Kerucut: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_kerucut.config(text="Masukkan angka yang valid untuk radius dan tinggi kerucut.")

app = tk.Tk()
app.title("Kalkulator Kerucut")

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

hitung_volume_kerucut_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_kerucut)
hitung_volume_kerucut_button.grid(row=2, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_kerucut_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_kerucut)
hitung_luas_permukaan_kerucut_button.grid(row=3, column=0, columnspan=2, pady=5)

hasil_volume_kerucut = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_kerucut.grid(row=4, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_kerucut = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_kerucut.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
