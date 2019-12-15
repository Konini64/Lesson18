#print("c01")
ka = "カミュ"
i = 0
while i < len(ka):
  #print(ka[i] )
  i += 1

#print("c02")
#a = input ("input first:")
#b = input ("input second:")
#print("{} is {} " .format (a,b))

#print("c03")
#print("aldous huxley was born in 1894.".capitalize())

#print("c04")
#listw = "where? who? when?".split(" ")
#print(listw)
print("c05")
list5 = ["The","fox","jumped","over","the","fence","."]
list5_2 = " ".join(list5)
print(list5_2.replace(" .","."))

#print("c06")
list6 = "A screaming comes across the sky.".replace("s","$")
print(list6)

#print("c07")
print ("hemingway".index("m"))


#print("c08")
god = "god is say 'Light !'"
print(god)
#print("c09")
th = "theree "
th3 = (th+th+th).strip()
print (th3)
th4 = th * 3
print (th4)

#print("c10")
moji = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
print(moji[:(moji.index("、"))])


for let in "Camus":
    	print(let)

senten = "Where now? Who now? When now?"
stringer = ""
result = []
for let in senten:
	stringer = stringer + let
	if let == "?":
		if stringer[0] == " ":
			result.append(stringer[1:])
		else:
			result.append(stringer)
		stringer = ""
print(result)

chal8 = "\"Wow!\" she said. \"This is a stupid challenge\" Kurt interrupted."
print(chal8)