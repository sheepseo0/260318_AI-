'''
#3-6
#(1)
for i in range(5):
    print("Hello, Python")

#(2)
for i in range(5):
    print(i)

#3-7
#(1)
print(list(range(1,101)))

#(2)
print(list(range(0,101,2)))

#(3)
print(list(range(1,101,2)))

#(4)
print(list(range(-100,1)))

'''
#3-8
#(1)
s = 0
for i in range(1,101):
    s = s+i
print(s)

#(2)
s = 0
for i in range(0,101,2):
    s = s+i
print(s)

#(3)
s = 0
for i in range(1,101,2):
    s = s+i
print(s)

    
#3-9
n = 7
for i in range(n):
    print(' '*(n-i-1) + '#')
