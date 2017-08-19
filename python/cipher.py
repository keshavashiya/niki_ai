m = input("Enter m....")
n = input("Enter n....")

def colnum_string(n):
    div=n
    string=""
    temp=0
    while div>0:
        module=(div-1)%26
        string=chr(65+module)+string
        div=int((div-module)/26)
    return string

for x in range(m, n+1):
	print colnum_string(x)