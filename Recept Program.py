

#  |-----------------------------------|
#  |Program to print costumer recept   |
#  |                                   |
#  |Version 1.0                        |
#  |-----------------------------------|

# Variables

StoreName = "Forte Supermarket"     #Store Name

SalesTax = 20            #Default Sales Tax

ID_1 = input("Enter ID_1: ")          #Default Id is 000

ID_2 = input("Enter ID_2: ")          #Default Id is 000

#Print Recept

print()
print(StoreName)
print()
print("------------------------------------")
print("ID     Desc                    R$   ")
print("------------------------------------")
print(str(ID_1)+ "    Arroz                   10,00")
print(str(ID_2)+ "    Feijao                   5,00")
print()
print("                           Tax " + str(SalesTax) + "%")
print("------------------------------------")
print("                               18,00")
print()
print("------------------------------------")
print("  Thank you for shopping with us!")
print("------------------------------------")
