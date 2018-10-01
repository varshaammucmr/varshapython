import random
print("hiiii")
count=0
while(count<=100):
	a=input("press r to roll a dice:")
	if(a=="r"):
		r=random.randint(1,6)
		print("r value is ",r)											
		count=count+r
		print("score is",count)
		if(count==100):
			print("you won")
			print("your score is",count)
		elif(count==11):
			count=2
			print("snake bite")
		elif(count==38):
			count9
			print("snake bite")
		elif(count==25):
			count=4
			print("snake bite")
		elif(count==65):
			count=46
			print("snake bite")
		elif(count==89):
			count=70
			print("snake bite")
		elif(count==93):
			count=64
			print("snake bite")
		elif(count==13):
			count=34
			print("ladder")
		elif(count==8):
			count=37
			print("ladder")
		elif(count==40):
			count=68
			print("ladder")
	else:
		break



dl211@soetcse:~/varsha$ python3 snack.py
hiiii
press r to roll a dice:r
r value is  3
score is 3
press r to roll a dice:r
r value is  4
score is 7
press r to roll a dice:r
r value is  4
score is 11
snake bite
press r to roll a dice:r
r value is  3
score is 5
press r to roll a dice:r
r value is  4
score is 9
press r to roll a dice:r
r value is  5
score is 14
press r to roll a dice:r
r value is  3
score is 17
press r to roll a dice:r
r value is  2
score is 19
press r to roll a dice:r
r value is  1
score is 20
press r to roll a dice:r
r value is  6
score is 26
press r to roll a dice:r
r value is  4
score is 30
press r to roll a dice:r
r value is  1
score is 31
press r to roll a dice:r
r value is  6
score is 37
press r to roll a dice:r
r value is  5
score is 42
press r to roll a dice:r
r value is  2
score is 44
press r to roll a dice:r
r value is  2
score is 46
press r to roll a dice:r
r value is  3
score is 49
press r to roll a dice:r
r value is  1
score is 50
press r to roll a dice:r
r value is  6
score is 56
press r to roll a dice:d



		
		







	
