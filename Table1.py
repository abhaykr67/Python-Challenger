
a = int(input("Enter starting no.: "))
b = int(input("Enter ending no.: "))
c = int(input("Total times: "))
d = int(input("How many columns: "))

    
for i in range(1, c+1):
    for j in range(a, b + 1):
        print(j, "*", i, "=", j * i, end="\t")
    print()
while True:
    choice = input("Do you want to start again or end? ")
    if choice == "end":
        break
