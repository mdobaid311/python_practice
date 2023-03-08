sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

marks = [sub1, sub2, sub3]

sum = sum(marks)
percentage=round(sum/3)

print("Total marks: ", sum)
print("Percentage: ",percentage)

if percentage>40:
    print("Pass")
else:
    print("Fail")