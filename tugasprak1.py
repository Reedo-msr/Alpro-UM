#Nama: Muhammad Syifa Ridhoni
#NIM: 220535604579
#Prodi/Offering: S1 Teknik Informatika / C

#Himpunan bilangan asli kurang dari 10 yang merupakan kelipatan 3 atau 5 adalah 3,5,6,9.
#Jumlah seluruh bilangan tersebut adalah 23. Hitung jumlah seluruh bilangan asli yang merupakan
#kelipatan 3 atau 5 dan kurang dari 1000.

sum = 0 #untuk menyimpan nilai
for i in range(1000): #membatasi nilai i dari 0 hingga 999
  if (i%3 == 0 or i%5 == 0): #mendeklarasikan jika i habis dibagi 3 atau 5
    sum = sum + i #nilai sum ditambah nilai i

#Untuk menampilkan nilai dari sum
print("Jadi jumlah dari seluruh bilangan asli kelipatan 3 atau 5 yang kurang dari 1000:", sum)