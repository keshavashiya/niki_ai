
list1 = []

n = input("How many strings you want to enter....")

def input():
	for i in range(n):
		s1 = raw_input("Enter string....")
		list1.append(s1)
	print(sorted(list1))


input()