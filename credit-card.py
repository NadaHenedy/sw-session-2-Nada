
def validation(credit_card):
  odd_values = 0
  even_values = 0
  total = 0
  reverse_card = credit_card[::-1]
  for x in reverse_card[::2]: 
        odd_values += int(x)
  for y in reverse_card[1::2]:
    y = int(y)*2
    if y>=10:
      even_values += ((y%10) + 1)
    else:
      even_values += y
  total = odd_values + even_values
  if(total%10==0):
    print("Valid")
  else:
    print("Invalid")


credit_card = input("Enter credit card value : ")

if(credit_card[0:2]=="34" or credit_card[0:2]=="37"):
    print("American Express")
    validation(credit_card)
elif(credit_card[0:2]=="51" or credit_card[0:2]=="52" or credit_card[0:2]=="53" or credit_card[0:2]=="54" or credit_card[0:2]=="55"):
    print("MasterCard")
    validation(credit_card)
elif(credit_card[0:1]=="4"):
    print("Visa")
    validation(credit_card)
else:
    print("Invalid")




