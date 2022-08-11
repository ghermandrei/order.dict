order = {
    'client' : ' Andrei',
    'item'   :  'Salad ',
   'quantity':    15,
   'price'   :   15.00
}
discount = 0.8
order['total'] = order['quantity'] * order['price']



print (order)
##############################################



print("Order for            :",order['client'])
print("Food                 :",order['item'])
print("Pric x qnt           :",order['price'],"x",order['quantity'])
print('Total                :',order['total'] )
if order['quantity'] > 7:
    order['discount_price']=order['total'] * discount
    print('Total after discount :',order['discount_price'])
print()
######## delivery option   ###################
delivery_cost = 50 
delivery = input("DO YOU WANT DELIVERY : YES/NO "  )

if delivery =='no' and  order['total'] < 300 or  order['discount_price'] < 300:
    print('free')

 
if delivery =='yes' and  order['total'] < 300 or  order['discount_price'] < 300:
    print('your delivery cost is : ',delivery_cost)

    if order['quantity'] <= 7:
     print("your final price is : ", order['total'] + delivery_cost)
    if order['quantity'] > 7 :
     print ("your final price is : ", order['discount_price'] + delivery_cost) 
    
if delivery == 'yes' and order['discount_price'] > 300 :
    print ('You got free delivery\nYour total is :',order['discount_price'])
if delivery == 'no' and order['discount_price'] > 300 :
    print ("NO DELIVERY\n Your total is :",order['discount_price'])
