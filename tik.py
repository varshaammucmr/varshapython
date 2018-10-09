a=['1','2','3','4','5','6','7','8','9']
def playboard():
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print("-------------")
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print("-------------")
	print('|',a[6],'|',a[7],'|',a[8],'|')
playboard()

playerOneTurn = True
while True:
	playboard()
	p=input("choose an available place :")

	if(p in a):
		if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
			print("place taken, choose another place...")
			continue
		else:
			if playerOneTurn:
				print("player 1 >>")
				a[int(p)-1]='x'
				playerOneTurn= not playerOneTurn
			else:
				print("player 2 >>")
				a[int(p)-1]='o'
				playerOneTurn = not playerOneTurn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("game over");
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("game over...")
					exit()
			if(a[0]==a[4] and a[0]==a[8]):
				print("game over");
				exit()
			if(a[0]==a[4] and a[2]==a[6]):
				print("game over")
				exit()
		else:
			print("Tie")
			exit()

	else:
		print("you have entered an invalid position")
		continue

			dl211@soetcse:~/varsha$ python3 tik.py
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :5
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | x | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :6
player 2 >>
| 1 | 2 | 3 |
-------------
| 4 | x | o |
-------------
| 7 | 8 | 9 |
choose an available place :3
player 1 >>
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| 7 | 8 | 9 |
choose an available place :6
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| 7 | 8 | 9 |
choose an available place :8       
player 2 >>
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| 7 | o | 9 |
choose an available place :^Z
[2]+  Stopped                 python3 tik.py
dl211@soetcse:~/varsha$ python3 tik.py
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :4
player 1 >>
| 1 | 2 | 3 |
-------------
| x | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :8
player 2 >>
| 1 | 2 | 3 |
-------------
| x | 5 | 6 |
-------------
| 7 | o | 9 |
choose an available place :5
player 1 >>
| 1 | 2 | 3 |
-------------
| x | x | 6 |
-------------
| 7 | o | 9 |
choose an available place :3
player 2 >>
| 1 | 2 | o |
-------------
| x | x | 6 |
-------------
| 7 | o | 9 |
choose an available place :6
player 1 >>
game over
dl211@soetcse:~/varsha$ python3 tik.py
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :8
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | x | 9 |
choose an available place :6
player 2 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | o |
-------------
| 7 | x | 9 |
choose an available place :5
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | x | o |
-------------
| 7 | x | 9 |
choose an available place :3
player 2 >>
| 1 | 2 | o |
-------------
| 4 | x | o |
-------------
| 7 | x | 9 |
choose an available place :5
| 1 | 2 | o |
-------------
| 4 | x | o |
-------------
| 7 | x | 9 |
choose an available place :9
player 1 >>
| 1 | 2 | o |
-------------
| 4 | x | o |
-------------
| 7 | x | x |
choose an available place :2
player 2 >>
| 1 | o | o |
-------------
| 4 | x | o |
-------------
| 7 | x | x |
choose an available place :7
player 1 >>
game over
dl211@soetcse:~/varsha$ python3 tik.py
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :7
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| x | 8 | 9 |
choose an available place :9
player 2 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| x | 8 | o |
choose an available place :5
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | x | 6 |
-------------
| x | 8 | o |
choose an available place :6
player 2 >>
| 1 | 2 | 3 |
-------------
| 4 | x | o |
-------------
| x | 8 | o |
choose an available place :3
player 1 >>
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| x | 8 | o |
choose an available place :8
player 2 >>
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| x | o | o |
choose an available place :8
| 1 | 2 | x |
-------------
| 4 | x | o |
-------------
| x | o | o |
choose an available place :2
player 1 >>
| 1 | x | x |
-------------
| 4 | x | o |
-------------
| x | o | o |
choose an available place :4
player 2 >>
| 1 | x | x |
-------------
| o | x | o |
-------------
| x | o | o |
choose an available place :1
player 1 >>
game over
dl211@soetcse:~/varsha$ python3 tik.py
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
choose an available place :7
player 1 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| x | 8 | 9 |
choose an available place :9
player 2 >>
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| x | 8 | o |
choose an available place :3
player 1 >>
| 1 | 2 | x |
-------------
| 4 | 5 | 6 |
-------------
| x | 8 | o |
choose an available place :5
player 2 >>
| 1 | 2 | x |
-------------
| 4 | o | 6 |
-------------
| x | 8 | o |
choose an available place :6
player 1 >>
| 1 | 2 | x |
-------------
| 4 | o | x |
-------------
| x | 8 | o |
choose an available place :1
player 2 >>
game over
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else:
        ^
IndentationError: unindent does not match any outer indentation level
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else:
        ^
IndentationError: unindent does not match any outer indentation level
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else;
        ^
IndentationError: unindent does not match any outer indentation level
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else
       ^
IndentationError: unindent does not match any outer indentation level
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else:
        ^
IndentationError: unindent does not match any outer indentation level
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else:
        ^
TabError: inconsistent use of tabs and spaces in indentation
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else
       ^
TabError: inconsistent use of tabs and spaces in indentation
dl211@soetcse:~/varsha$ python3 tik.py
  File "tik.py", line 42
    else:
       ^
SyntaxError: invalid syntax
dl211@soetcse:~/varsha$ 

