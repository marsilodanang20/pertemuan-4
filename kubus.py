import tkinter as tk

def hitung_volume_kubus():
    try:
        sisi = float(sisi_entry.get())
        volume = sisi**3
        hasil_volume_kubus.config(text=f"Volume Kubus: {volume:.2f} cm³")
    except ValueError:
        hasil_volume_kubus.config(text="Masukkan angka yang valid untuk panjang sisi kubus.")

def hitung_luas_permukaan_kubus():
    try:
        sisi = float(sisi_entry.get())
        luas_permukaan = 6 * sisi**2
        hasil_luas_permukaan_kubus.config(text=f"Luas Permukaan Kubus: {luas_permukaan:.2f} cm²")
    except ValueError:
        hasil_luas_permukaan_kubus.config(text="Masukkan angka yang valid untuk panjang sisi kubus.")

app = tk.Tk()
app.title("Kalkulator Kubus")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack(padx=10, pady=10)

sisi_label = tk.Label(frame, text="Panjang Sisi (cm):")
sisi_label.grid(row=0, column=0, sticky="w")
sisi_entry = tk.Entry(frame)
sisi_entry.grid(row=0, column=1)

hitung_volume_kubus_button = tk.Button(frame, text="Hitung Volume", command=hitung_volume_kubus)
hitung_volume_kubus_button.grid(row=1, column=0, columnspan=2, pady=5)

hitung_luas_permukaan_kubus_button = tk.Button(frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan_kubus)
hitung_luas_permukaan_kubus_button.grid(row=2, column=0, columnspan=2, pady=5)

hasil_volume_kubus = tk.Label(frame, text="", font=("Arial", 12))
hasil_volume_kubus.grid(row=3, column=0, columnspan=2, pady=10)

hasil_luas_permukaan_kubus = tk.Label(frame, text="", font=("Arial", 12))
hasil_luas_permukaan_kubus.grid(row=4, column=0, columnspan=2, pady=10)

app.mainloop()
