names=[]

while True:
    try:
        names.append(input("name: ").title())
    except EOFError:
        break

    print("")            

if len(names) > 2:
     print("Adieu, adieu, to " + str(', '.join(names[:-1])))
elif len(names)== 2:
     print("Adieu, adieu, to " + str(' and '.join(names)))    
else:
     print("Adieu, adieu, to "+ str(names))    