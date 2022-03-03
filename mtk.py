import os 
import time as tm

for i in range(1000):
	os.system("clear")
	print('='*35)
	print("============ Main Menu ============")
	print("1.Segi 4")
	print("2.Kubus")
	print("3.Balok")
	print("4.Tabung")
	print("5.Kerucut")
	print("0.Exit")
	print('='*35)
	op = input("Pilih Salah Satu Option 1,2,etc : ")
	if op == '0':
		print("Exit")
		break;
	if op == '1':
		os.system("clear")
		print('='*35)
		one = int(input("Masukkan P : "))
		two = int(input("Masukkan L : "))
		rst = one * two
		print("Hasil Nya Adalah", str(rst) + "CM²")
		print("Waitt 10S to Refresh")
		tm.sleep(10)
	if op == '2':
		os.system("clear")
		print('='*35)
		one = int(input("Masukkan S : "))
		rst = one * one * one
		rstl = 6 * one * one
		print("Hasil Volume Nya Adalah", str(rst) + "CM²")
		print("Hasil Luas Permukaan Nya Adalah", str(rstl) + "CM²")
		print("Waitt 10S to Refresh")
		tm.sleep(10)
	if op == '3':
		os.system("clear")
		print('='*35)
		one = int(input("Masukkan T : "))
		two = int(input("Masukkan P : "))
		three = int(input("Masukkan l : "))
		rst = one * two * three
		rstl = 2 * (one + two + three)
		print("Hasil Volume Nya Adalah", str(rst) + "CM²")
		print("Hasil Luas Nya Adalah", str(rstl) + "CM²")
		print("Waitt 10S to Refresh")
		tm.sleep(10)
	if op == '4':
		os.system("clear")
		print('='*35)
		one = int(3.14)
		two = int(input("Masukkan r : "))
		three = int(input("Masukkan t : "))
		rst = one * two * two * three
		rstlp =  2 * one * two * (two + three)
		rstls = 2 * one * two * three
		rstla = one * two * two
		print("Hasil Volume Nya Adalah", str(rst) + "CM²")
		print("Hasil Luas Permukaan Nya Adalah", str(rstlp) + "CM²")
		print("Hasil Luas Selimut Nya Adalah", str(rstls) + "CM²")
		print("Hasil Luas Alas Nya Adalah", str(rstla) + "CM²")
		print("Waitt 10S to Refresh")
		tm.sleep(10)
	if op == '5':
		os.system("clear")
		print('='*35)
		one = int(3.14)
		two = int(input("Masukkan T : "))
		three = int(input("Masukkan R : "))
		four = int(input("Masukkan S : "))
		rst = one * three * three * two / 3
		rstla = one * three * three
		rstls = one * three * four
		rs5lp = rstla + rstls
		print("Hasil Volume Nya Adalah", str(rst) + "CM²")
		print("Hasil Luas permukaan Nya Adalah", str(rstlp) + "CM²")
		print("Hasil Luas alas Nya Adalah", str(rstla) + "CM²")
		print("Hasil Luas selimut Nya Adalah", str(rstls) + "CM²")
		print("Waitt 10S to Refresh")
		tm.sleep(10)
