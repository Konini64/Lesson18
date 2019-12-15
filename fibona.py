##１から１万の繰り返し
#roop_cnt = 0
#S = 10000
##SOSU = set()
#for x in range(1,S):
##数値ごとの繰り返し
#    mod_cnt = 0
#    for y in range (1,x):
##ループのなかであまり０の回数をカウント
#        if x%y == 0:
#            mod_cnt += 1
#            roop_cnt += 1
#        else :
#            roop_cnt += 1
##あまり０が、２個（１とその数）の場合素数リストにイン
#    if mod_cnt < 2:
#       print (x)
#
#print (roop_cnt)
#
##ループ後素数リストをソートして表示
#
#MAXの定義
MAX_N = 2**31
#ループ定義
x = 0
y = 1
print(x)
print(y)
cnt = 0
while  y < MAX_N:
    z = x+y
    print(z)
    x = y
    y = z
    cnt += 1
print(cnt)
#プリント
#
#
#
#
#
#
#
#
#
#
#
#
#
#
