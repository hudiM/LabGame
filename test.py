test = ["alma","szőlő"]
print(test[1:])
test = ["alma"]
print(test[1:])

def print_stuff(*stuff):
    for i in stuff[1:]:
        print(i)


print_stuff(*test)
