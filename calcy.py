def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def divide(a,b):
	return a/b

i=int(input("enter value of a:"))
j=int(input("enter value of b:"))
o=input("what do you want to do? +,-,x,/:")

if(o=='+'):
	res=add(i,j)
elif(o=='-'):
	res=sub(i,j)
elif(o=='x'):
	res=mult(i,j)
elif(o=='/'):
	res=divide(i,j)

print(res)



dl211@soetcse:~/varsha$ python3 calcy.py
enter value of a:45
enter value of b:36
what do you want to do? +,-,x,/:x
1620
dl211@soetcse:~/varsha$ 78
78: command not found
dl211@soetcse:~/varsha$ python3 calcy.py
enter value of a:67
enter value of b:78
what do you want to do? +,-,x,/:/
0.8589743589743589
dl211@soetcse:~/varsha$ python3 calcy.py
enter value of a:98
enter value of b:78
what do you want to do? +,-,x,/:-
20
dl211@soetcse:~/varsha$ python3 calcy.py
enter value of a:45
enter value of b:45
what do you want to do? +,-,x,/:+
90

