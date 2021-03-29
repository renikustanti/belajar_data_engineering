bulan_hari = {
    1 : 31
    2 : 28
    3 : 31
    4 : 30
    5 : 31
    6 : 30
    7 : 31
    8 : 31
    9 : 30
    10 : 31
    11 : 30
    12 : 31
}

bulan_hari_kabisat = {
    1 : 31
    2 : 29
    3 : 31
    4 : 30
    5 : 31
    6 : 30
    7 : 31
    8 : 31
    9 : 30
    10 : 31
    11 : 30
    12 : 31
}

input1 = input()
input2 = input()

tahun1, bulan1, tanggal1 = input1.split("-")
tahun2, bulan2, tanggal2 = input2.split("-")

if (bulan ==1):
    hari = 31
elif(bulan ==1):
    hari = 31
    if((tahun % 4 == 0 and tahun % 100 !=0) 0r tahun % 400 == 0):
        hari = 29
    else:
        hari = 28
elif(bulan == 3):
    hari = 31
elif(bulan == 4):
    hari = 30
elif(bulan == 5):
    hari = 31
elif(bulan == 6):
    hari = 30
elif(bulan == 7):
    hari = 31
elif(bulan == 8):
    hari = 31
elif(bulan == 9):
    hari = 30
elif(bulan == 10):
    hari = 31
elif(bulan == 11):
    hari = 30
elif(bulan == 12):
    hari = 31
else:
    hari = -1
print(hari)
