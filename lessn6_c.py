"""
list1 = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for i in list1:
    print (i)
#2
for i in range (25,51):
    print(i)
#3
list1_i = 0
for entry in list1:
    print (entry,list1_i)
    list1_i += 1

#5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
list_new = []
for i in list1:
    for j in list2:
        list_new.append(i*j)

print(list_new)

"""
list1 = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

list1_i = 0
for entry in list1:
    print (entry,list1_i)
    list1_i += 1
shows = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for index,show in enumerate(shows):
    print (index)
    print (show)

#4
listn = [31,1,54,5,63,45,75]
k = "k"
while k == "k":
    a = input("type q to quit :")
    if a == "q":
        break
    
    try:
        a = int(a)
        if  a in listn:
            print("GREAT!!!")
            break
        else:
            print("one more!!!")
            continue
    except:
            print("数字を入力するか、qで終了します")
