# -*- coding: utf-8 -*-
"""tas_kagit_makas_proje.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bUEYA77EUi1jpiQLD0ijh0h-Li09BhNU
"""

import random

def tas_kagit_makas_furkan_kececi():
  print("Taş Kağıt Makas Oyununa Hoş Geldiniz!")
  print("Bir oyun en fazla 3 turdan oluşur, 2 puan olan oyunu kazanır!")
  print("Oyunda taş,kağıt,makas seçeneklerinden birini seçmelisiniz. Taş makası, makas kağıdı, kağıt taşı kapar!")
  print("Başarılar!")

tas_kagit_makas_furkan_kececi()
player = input("Oyun oynamak ister misiniz?")
good_bye = "Kendine iyi bak!"


while player == "evet" or "hayır":
  if player == "hayır":
    print("Oyun kapatılıyor...")
    print(good_bye)
    exit()
    break
  if player == "evet":
    print("Oyun başlıyor...")
    break
  if player not in ["evet","hayır"]:
    print("Lütfen evet veya hayır yazınız!")
    player = input("Oyun oynamak ister misiniz?")

game_counter = 0
player_score = 0
computer_score = 0
choices = ["taş","kağıt","makas"]

while player_score < 2 and computer_score < 2:
  player_choice = input("Seçimini yap!")
  computer_choice = random.choice(choices)
  if player_choice not in choices:
    print("Lütfen sadece taş, kağıt veya makas yazınız!")
    input("Seçimini yap!")
  else:
    print("Bilgisayarın seçimi: ", computer_choice)
    print("Senin seçimin: ", player_choice)

  if player_choice == computer_choice:
    print("Berabere!")
    player_score += 0
    computer_score += 0
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "taş" and computer_choice == "makas":
    print("Kazandınız!")
    player_score += 1
    computer_score += 0
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "kağıt" and computer_choice == "taş":
    print("Kazandınız!")
    player_score += 1
    computer_score += 0
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "makas" and computer_choice == "kağıt":
    print("Kazandınız!")
    player_score += 1
    computer_score += 0
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "taş" and computer_choice == "kağıt":
    print("Kaybettiniz!")
    player_score += 0
    computer_score += 1
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "kağıt" and computer_choice == "makas":
    print("Kaybettiniz!")
    player_score += 0
    computer_score += 1
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_choice == "makas" and computer_choice == "taş":
    print("Kaybettiniz!")
    player_score += 0
    computer_score += 1
    game_counter += 1
    print("{}. turun sonu!".format(game_counter))
    print("Oyuncunun skoru: ", player_score)
    print("Bilgisayarın skoru: ", computer_score)

  if player_score == 2:
    print("Tebrikler! Kazandınız!")
    break

  if computer_score == 2:
    print("Maalesef kaybettiniz!")
    break