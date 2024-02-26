N=10
print("Задание 2. Вариант ",(N-1)%13+1)

def saleslist(salesdata):
    listofbuyers={}
    for i in range(len(salesdata)):
        buyer,item, quantity=salesdata[i].split()
        quantity=int(quantity)
        if(buyer not in listofbuyers):
            listofbuyers[buyer]={}
        if item not in listofbuyers[buyer]:
            listofbuyers[buyer][item]=quantity
        else:
            listofbuyers[buyer][item]+=quantity
    return listofbuyers

salesdata=["Ivanov paper 10","Petrov pens 5","Ivanov marker 3",
            "Ivanov paper 7", "Petrov envelope 20", "Ivanov envelope 5"]
listofbuyers=saleslist(salesdata)
buyers=sorted(listofbuyers.keys())
for buyer in buyers:
    print(buyer,":")
    items=sorted(listofbuyers[buyer].keys())
    for item in items:
        print(item, listofbuyers[buyer][item])