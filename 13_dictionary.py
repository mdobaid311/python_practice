myDict = {
    "name": "John",
    "age": 30,
    "anotherDict": {
        "name2": "obaid"
    }
}
myDict["age"] = 23

# print(list(myDict.keys()))
# print(list(myDict.values()))
# print(list(myDict.items()))
myDict2 = {
    "name1": "obaid",
    "age": 23
}

myDict.update(myDict2)
print(myDict)
print(myDict.get("name"))

print(myDict.popitem())