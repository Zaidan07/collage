import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print("=== DATA AWAL ===")
print(df.head())
print("\nJumlah data awal:", len(df))

df = df.dropna()

if "Age" in df.columns:
    df = df[df["Age"] >= 0]

print("\n=== SETELAH HAPUS DATA SALAH ===")
print(df.head())
print("Jumlah data:", len(df))

df = df.drop_duplicates()

print("\n=== SETELAH HAPUS DUPLIKAT ===")
print(df.head())
print("Jumlah data:", len(df))


numeric_cols = df.select_dtypes(include="number").columns

plt.figure()

if len(numeric_cols) >= 2:
    plt.plot(df[numeric_cols[0]], df[numeric_cols[1]])
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.title("Line Plot")

elif len(numeric_cols) == 1:
    plt.hist(df[numeric_cols[0]])
    plt.xlabel(numeric_cols[0])
    plt.title("Histogram")

else:
    print("Tidak ada data numerik untuk diplot")

plt.show()