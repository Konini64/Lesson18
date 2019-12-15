"""
my_list = []

with open("st.txt","r",encoding ="utf-8") as f:
    my_list.append(f.read())
print(my_list)

import csv
with open("st.csv","w",newline='') as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])
import csv

with open("st.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
"""

#C01
print("C01")
with open("lesson6_ex.py","r",encoding="utf-8") as f:
    print(f.read())


#C02
print("C02")
c = input("What your name ?:")
with open("anser.txt","w",encoding="utf-8") as f:
    f.write(c)

#C03
print("C03")
import csv
list_en = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("st2.csv","w",encoding="utf-8",newline='') as f:
    w = csv.writer(f,delimiter=",")
    for w_list in list_en:
        w.writerow(w_list)

#C04
print("C04")
#import csv
list_jp = [["トップ・ガン","リスキー・ビジネス","マイノリティレポート"],["タイタニック","レブナント","インセプション"],["トレーニングディ","マンオブファイア","ファイト"]]

with open("タイトル.csv","w",encoding="utf-8",newline='') as f:
    w = csv.writer(f,delimiter=",")
    for w_list in list_jp:
        w.writerow(w_list)
