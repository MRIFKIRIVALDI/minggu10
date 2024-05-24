import array as arr
print(" SOAL NO 1")
print('=' * 12)
arr = [8, 3, 12, 4, 7, 2]
output_arr = []
# mengganti angka yang kurang dari sama dengan 5 menjadi 0
for i in arr:
    if i <= 5:
        output_arr.append(0)
    else:
        output_arr.append(i)
# Mengurutkan nilai
output_arr.sort(reverse=True)
print(output_arr)  # Output: [12, 8, 7, 0, 0, 0]

print(" SOAL NO 2")
print('=' * 12)
arr = [7, 4, 9, 2, 5, 1]
output_arr = []
# Menghapus bilangan ganjil
for i in arr:
    if i % 2 == 0:
        output_arr.append(i)

output_arr.sort()
print(output_arr)  # Output: [2, 4]

print(" SOAL NO 3")
print('=' * 12)
kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []
# Menghapus kata yang kurang dari lima karakter
for i in kata:
    if len(i) >= 5:
        output.append(i)

output.sort()
print(output)  # Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

print(" SOAL NO 4")
print('=' * 12)
list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]
# Menggabungkan, menghapus duplikat, dan mengurutkan 
hasil = sorted(set(list1 + list2))
print(hasil)  # Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']


print(" SOAL NO 5")
print('=' * 12)
input_arr = [105, 20, 8, 150, 30, 5, 200]
output_arr = []
# Menyaring nilai
for i in input_arr:
    if 10 <= i <= 100:
        output_arr.append(i)

# Mengurutkan hasilnya
output_arr.sort()
print(output_arr)  # Output: [20, 30]