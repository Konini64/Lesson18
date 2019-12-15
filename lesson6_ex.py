"""
数字あてゲーム
・ランダム数値は４桁の数値
・数値は重複しない
・インプット時も数値の重複は認めない（0000と入れて、どの数字が有効化の判定できてしまうのを避ける）

"""


import random
i = 0
list_rand = []

while  i < 4:
    ran_item = random.randrange(0,10)
    #print (ran_item)
    if str(ran_item) not in list_rand:
        list_rand.append(str(ran_item))
        i += 1


    
str_rand = "".join(list_rand)
#print (str_rand)
chance = 1
print ("Please number of 4 hit!")
while True:
    a = input ("0000-9999 " + str(chance) +"th input!! : ")

    if a == "q":
        print (str_rand)
        break

    if len(a) != 4:
        print("INPUT 4桁!!!")
        continue

    if len(set(a)) != 4:
        print("INPUT another number!!")
        continue
    chance += 1
    try:
        b = int(a)
        hit = 0
        brow = 0
        i = 0
        for a_item in a:
            if a_item == str_rand[i]:
                hit += 1 
                i += 1
                #print ("p1_"+a_item)
                #continue
            else:
                j = 0
                if a_item in a[:i]:
                    j += 1
                    #print ("p2_"+a_item)
                    #continue
                else:
                    if a_item in str_rand:
                        #print ("p3_"+a_item)
                        brow += 1 
                        j += 1
                    else:
                        #print ("p4_"+a_item)
                        j += 1
                i += 1
        if hit == 4:
            print("GREATE!! NUMBER is " + str_rand)
            break


        print ("you input number "+str(hit) + "hit & " + str(brow) + "brow!")
    except:
        print("INPUT NUMBER!!!")

