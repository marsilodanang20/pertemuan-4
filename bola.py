import tkinter as tk

def hitung_volume_bola():
    try:
        radius = float(radius_entry.get())
        volume = (4/3) * 3.141592653589793 * (radius ** 3)
        hasil_volume_bola.config(text=f"Volume Bola: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_bola.config(text="Masukkan angka yang valid untuk radius bola.")

def hitung_luas_permukaan_bola():
    try:
        radius = float(radius_entry.get())
        luas_permukaan = 4 * 3.141592653589793 * (radius ** 2)
        hasil_luas_permukaan_bola.config(text=f"Luas Permukaan Bola: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_bola.config(text="Masukkan angka yang valid untuk radius bola.")

app = tk.Tk()
app.title("Kalkulator Bola")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

radius_label = tk.Label(frame, text="Radius (cm):")
radius_label.grid(row=0, column=0, sticky="w")
radius_entry = tk.Entry(frame)
radius_entry.grid(row=0, column=1)

hitung_volume_bola_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_bola)
hitung_volume_bola_button.grid(row=2, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_bola_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_bola)
hitung_luas_permukaan_bola_button.grid(row=3, column=0, columnspan=2, pady=5)

hasil_volume_bola = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_bola.grid(row=4, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_bola = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_bola.grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
