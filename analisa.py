import pandas as pd
data = pd.read_csv('pengeluaran_kost.csv')
print(data)
total=data["Jumlah"].sum()
print(f"Total:Rp{total}")
rata=data["Jumlah"].mean()
print(f"Rata-rata: Rp{rata}")