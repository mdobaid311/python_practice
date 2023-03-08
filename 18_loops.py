i = 0
while i < 10:
    print(i)
    i = i + 1
list = [1, 25, "hello"]

for item in list:
    print(item)

for i in range(10):
    print("range ", i)

for i in range(1, 10):
    if (i == 5):
        break
else:
    print("else")  # does not print else because the loop did not execute till the end
