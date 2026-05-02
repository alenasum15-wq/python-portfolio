import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset Titanic
titanic = sns.load_dataset("titanic")

# Lihat 5 data pertama
print(titanic.head())

# Info dataset
print(titanic.shape)
# Berapa yang selamat vs tidak?
print(titanic["survived"].value_counts())

# Grafik yang selamat
titanic["survived"].value_counts().plot(
    kind="bar",
    color=["red", "green"]
)
plt.title("Titanic: Selamat vs Tidak")
plt.xticks([0, 1], ["Tidak Selamat", "Selamat"])
plt.ylabel("Jumlah Penumpang")
plt.show()
# Analisa 1 - Pria vs Wanita yang selamat
plt.figure()
sns.countplot(x="sex", hue="survived", 
              data=titanic,
              palette=["red", "green"])
plt.title("Selamat berdasarkan Jenis Kelamin")
plt.xlabel("Jenis Kelamin")
plt.ylabel("Jumlah")
plt.legend(["Tidak Selamat", "Selamat"])
plt.show()

# Analisa 2 - Berdasarkan Kelas Tiket
plt.figure()
sns.countplot(x="pclass", hue="survived",
              data=titanic,
              palette=["red", "green"])
plt.title("Selamat berdasarkan Kelas Tiket")
plt.xlabel("Kelas (1=Mewah, 2=Menengah, 3=Ekonomi)")
plt.ylabel("Jumlah")
plt.legend(["Tidak Selamat", "Selamat"])
plt.show()
# Analisa 3 - Distribusi Umur
plt.figure()
titanic["age"].hist(bins=20, color="blue", 
                    edgecolor="black")
plt.title("Distribusi Umur Penumpang Titanic")
plt.xlabel("Umur")
plt.ylabel("Jumlah Penumpang")
plt.show()

# Analisa 4 - Rata rata umur yang selamat vs tidak
selamat = titanic[titanic["survived"]==1]["age"].mean()
tidak = titanic[titanic["survived"]==0]["age"].mean()

print(f"Rata-rata umur yang selamat: {selamat:.1f} tahun")
print(f"Rata-rata umur yang tidak selamat: {tidak:.1f} tahun")