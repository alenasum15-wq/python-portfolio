import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pengeluaran_kost.csv")

plt.pie(data["Jumlah"], 
        labels=data["Nama Pengeluaran"],
        autopct="%1.1f%%")

plt.title("Porsi Pengeluaran Kost Alen")
plt.show()