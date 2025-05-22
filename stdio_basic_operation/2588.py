x = int(input())
y = input()

for i in reversed(range(3)):
    print(x*int(y[i]))

print(x*int(y))