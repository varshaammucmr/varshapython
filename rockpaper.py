s1=0
s2=0
while(s1<=3 or s2<=3):

	a=input('enter r for rock,p for paper,s for scissor')
	import random
	d=['r','p','s']
	s=random.choice(d)
	print(s)
	if(a==s):
		print('draw')
		print(s1)
		print(s2)
	elif(s1==3):
		print('you won')
		break
	elif(s2==0):
		print('you lose')
		break
	elif(a=='p' and s=='r'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='p' and s=='s'):
		print('try')
		s2=s2+1
		print(s2)
		print(s1)
	elif(a=='s' and s=='r'):
		print('try')
		s2=s2+1
		print(s1)
		print(s2)
	elif(a=='s' and s=='p'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='r' and s=='s'):
		print('point')
		s1=s1+1
		print(s1)
		print(s2)
	elif(a=='r' and s=='p'):
		print('try')
		s2=s2+1
		print(s1)
		print(s2)








dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
s
you lose
dl211@soetcse:~/varsha$ s
s: command not found
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissors
r
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorp
r
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorp
s
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissors
p
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
r
draw
0
0
enter r for rock,p for paper,s for scissorr   
p
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissors
p
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
p
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorp
p
draw
0
0
enter r for rock,p for paper,s for scissorr
s
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
p
you lose
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
s
you lose
dl211@soetcse:~/varsha$ python rockpaper.py
enter r for rock,p for paper,s for scissorr
Traceback (most recent call last):
  File "rockpaper.py", line 5, in <module>
    a=input('enter r for rock,p for paper,s for scissor')
  File "<string>", line 1, in <module>
NameError: name 'r' is not defined
dl211@soetcse:~/varsha$ python rockpaper.py
enter r for rock,p for paper,s for scissorr
Traceback (most recent call last):
  File "rockpaper.py", line 5, in <module>
    a=input('enter r for rock,p for paper,s for scissor')
  File "<string>", line 1, in <module>
NameError: name 'r' is not defined
dl211@soetcse:~/varsha$ python3 rockpaper.py
enter r for rock,p for paper,s for scissorr
r
draw
0
0
enter r for rock,p for paper,s for scissors
p
you lose

