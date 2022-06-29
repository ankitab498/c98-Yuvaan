

# age = int(input("Enter age : "))
# print("Age : " , age)


f = open("demo.txt")
print(f.read())

f = open("demo.txt")
lines = f.readlines()

for line in lines:
    print(line)


string = "Hello World"
print(string.split())


# ------------------------- functions ----------------------------------------------------
print("--------------------------")
def Name():
    print("Hello")

Name()

def sum(a,b):
    print(a + b)

sum(12,8)






