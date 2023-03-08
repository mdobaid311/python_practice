import os

def create_table(number, filename):
    for i in range(1, 11):
        with open(filename, "a") as file:
            file.write(f"{number} * {i} = {number*i}\n")


create_table(2, "2_table.txt")
