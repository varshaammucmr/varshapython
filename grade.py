a=int(input("marks"))
if(a>=90):
	print("grade-A+")
elif(a>=80):
	print("grade-A")
elif(a>=70):
	print("grade-B+")
elif(a>=60):
	print("grade-B")
elif(a>=40):
	print("grade-c")
else:
	print("fail")





l211@soetcse:~/varsha$ python grade.py
marks90
grade-A+
dl211@soetcse:~/varsha$ python grade.py
marks67
grade-B
dl211@soetcse:~/varsha$ python grade.py
  File "grade.py", line 17
    dl211@soetcse:~/varsha$ python grade.py
         ^
SyntaxError: invalid syntax
dl211@soetcse:~/varsha$ python grade.py
  File "grade.py", line 17
    dl211@soetcse:~/varsha$ python grade.py
         ^
SyntaxError: invalid syntax
dl211@soetcse:~/varsha$ python grade.py
marks56
grade-c
dl211@soetcse:~/varsha$ python grade.py
marks43
grade-c
dl211@soetcse:~/varsha$ python grade.py
marks34
fail
dl211@soetcse:~/varsha$ 

