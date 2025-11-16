import pandas as pd  # buat bikind an simpan DataFrame
import random  # untuk randomisasi kategori, harga, dll
from datetime import datetime, timedelta  # untuk buat tanggal pesanan
import numpy as np  # random seed + keperluan numerik

# Reproducibility
# supaya dataset konsisten a.k.a setiap running hasil randomnya sama
random.seed(42)
np.random.seed(42)

# Sampe categories and products
categories = {
    "Electronics": ["House Wireless", "Keyboard Mechanical", "Earphone Bass", "Powerbank 10000mAH", "USB Hub"],
    "Fashion": ["Hoodie Oversize", "Kaos Unisex", "Celana Kargo", "Jaket Denim", "Topi Bucket"],
    "Beauty": ["Serum Vitamin C", "Facial Wash", "Moisturizer Gel", "Sunscreen", "Lip Tint"],
    "Food": ["Kopi Susu", "Mie Instan Premium", "Coklat Batangan", "Keripik Pedas", "Basreng"]
}  # memetakan kategori -> daftar produk

# nanti ini diacak-acak di loop
cities = ["Jakarta", "Bandung", "Pontianak", "Makassar", "Medan"]
payment_methods = ["ShopeePay", "COD", "TF Bank", "Gopay", "Dana"]

# Generate Dataset
data = []  # siapin list kosong untuk nantinya menampung seluruh baris dataset
start_date = datetime(2024, 1, 1)  # tanggal pesanan paling awal

for i in range(1, 501):  # loop sebanyak 500 baris
    category = random.choice(list(categories.keys()))  # ambil kateogori random
    # ambil produk sesuai kategori
    product = random.choice(categories[category])
    price = random.randint(20000, 500000)  # generate harga 20k - 500k
    quantity = random.randint(1, 5)  # genetate jumlah pembelian
    total_sales = price * quantity
    # generate tanggal random dalam 180 hari
    order_date = start_date + timedelta(days=random.randint(0, 180))

    data.append([  # masukin data ke list bernama data
        f"TRX{i:04d}",  # format ID contoh TRSX0001
        order_date.date(),  # simpan format tanggal saja
        product,
        category,
        price,
        quantity,
        total_sales,
        random.choice(cities),  # diacak tiap loop
        random.choice(payment_methods)  # diacak tiap loop
    ])

# buat dataframe krna harus ubah list jadi dataframe(tabel) kalau mau simpan ke csv
df = pd.DataFrame(data, columns=[
    "order_id", "order_date", "product_name", "category",
    "price", "quantity", "total_sales", "customer_city", "payment_method"
])

# save to csv
file_path = "D:/1. KULIAH/1.PROFESSIONAL NEEDS/data analysis/ecommerce_sales.csv"
df.to_csv(file_path, index=False)

file_path  # return path (buat nampilin path pas skrip dijalankan)
