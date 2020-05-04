list_guest=['Liubang','Hanxing','Xiangyu']
for i in range (0,len(list_guest)):
  print("Hello "+list_guest[i]+' ,I want to invite you go to the party!')
refuse=list_guest.pop(1)
print(refuse+' can\'t join.')
list_guest.append('Fanzeng')
for i in range (0,len(list_guest)):
  print("Hello "+list_guest[i]+' ,I want to invite you go to the party!')
print('I find a bigger desk')
list_guest.insert(0,'Xiangzhuang')
list_guest.insert(int((len(list_guest)+1)/2),'Zhangliang')
list_guest.append('Zhaoxing')
for i in range (0,len(list_guest)):
  print("Hello "+list_guest[i]+' ,I want to invite you go to the party!')
print('The bigger desk can\'t arrive in time,only two guests can join in the party!')
del1=list_guest.pop(-1)
print('Sorry '+del1+',I can\'t invite you!')
del2=list_guest.pop(-1)
print('Sorry '+del2+',I can\'t invite you!')
del3=list_guest.pop(0)
print('Sorry '+del3+',I can\'t invite you!')
del4=list_guest.pop(1)
print('Sorry '+del4+',I can\'t invite you!')
print(list_guest[0]+',you still can join in the party!')
print(list_guest[1]+',you still can join in the party!')
del list_guest[1]
del list_guest[0]
print(list_guest)




