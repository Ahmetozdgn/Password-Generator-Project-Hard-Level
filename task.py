#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#Password Generator Project

import random # Rastgele seçimler yapmak ve listeyi karıştırmak için random modülü eklenir.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Kullanıcıya hoş geldiniz mesajı gösterilir.
print("Welcome to the PyPassword Generator!")

#  Kullanıcıdan kaç harf, sembol ve rakam olacağını öğrenmek için input() ile veri alınır.
# Alınan veri int() ile tam sayıya çevrilir.
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Şifreyi karakterler halinde tutmak için boş bir liste oluşturulur.
password_list = []

# Kullanıcının istediği sayıda rastgele harf seçilip listeye eklenir.
for char in range(0, nr_letters):
  password_list.append(random.choice(letters))

# Kullanıcının istediği sayıda rastgele sembol seçilip listeye eklenir.
for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

# Kullanıcının istediği sayıda rastgele rakam seçilip listeye eklenir.
for char in range(0, nr_numbers):
  password_list.append(random.choice(numbers))

print(password_list)

# Karakterlerin sırası rastgele karıştırılır.
random.shuffle(password_list)

print(password_list)

password = ""

# Şifre listesindeki her karakter birleştirilerek password değişkenine eklenir.
for char in password_list:
    password += char

print(f"your password is:{password}")

