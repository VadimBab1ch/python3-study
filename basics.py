#Basic aspects to study python.
#!/bin/python3
def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return ("We're getting a drink!")
	elif (age >= 21) and (money < 5 ):
		return ("Come back with more money")
	elif (age < 21) and (money >= 5):
		return ("Nice try, kid!")
	else:
		return ("You're too poor and too young!")

print(alcohol(24,5))
print(alcohol(21,4))
print(alcohol(20,4))



#!/bin/python3
print("boolean expressions")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))

#relational operators
greater = 7 > 4
print(greater)
test = 3 < 6 and 5 > 4
print(test)
ntest_not = not True #False



#!/bin/python3
def my_func():
	print ("I'm in function daaaamn!")
my_func()
def func2(name, age):
	print("Hello " + name + " you are " + str(age) + " years old!")
func2('vadym', 22)

def multiply(x,y):
	return x * y
print(multiply(5,5))


#!bin/python3
movies = ["the exorcist" ,"hangover" , "film2", "film3"]
print(movies[0])
print(movies[1:3])
print(movies[1:])
print(movies[:1])
print(movies[-1]) # take last item
print(len(movies))
movies.append("JASW")
print(movies)
movies.pop() # delete last item
print (movies)
movies.pop(0)
print (movies)


#!bin.python3
# Tuples do not change!, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])


#!/bin/python3
quote = "Something went wrong!"
print(quote.upper())
print(quote.title())
print(len(quote))


#For loops, start to finish of an iterate
vegetabels = ["cucumber", "spinach" , "cabage"]
for x in vegetabels:
	print (x)


#while loops
i = 1
while i < 10:
	print (i)
	i+= 1




