#question 1
favouritw_singer=['pushu','wubai','zhangyu','huyanbing']

#question2
locations=[('huaian',78,89),('nanjin',79.15,90.45),('hangzhou',25.66,343.44)]

#question3
my_dict={'height':175,'favourite_color':'blue','favourite_writer':'Haimingway'}
keys=['height','favourite_color','favourite_writer']
#question4
x=input('''What do you want to konw?
            1.my height
            2.my favourite color 
            3.my favourite writer \nEnter the number:''')


try:

    x=int(x)
    print(my_dict[keys[x-1]])
except Exception:
    print("You should enter the correct number!")


#question5
singer_song={'Wubai':'Meet again','Pushu':'the way of normal','Beatles':'Hey Jude'}

















































































