
#FizzBuzz问题
for i in range(1,101):
    sign=''
    if i%3 != 0 and i%5 != 0:
        sign+=str(i)
    elif i%3 ==0 and i%5 == 0:
        sign ='FizzBuzz'
    elif i%3 == 0:
        sign ='Fizz'
    elif i%5 == 0:
        sign = 'Buzz'
    print(sign)


#squential search
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n :
            found = True
            break
    return found
numbers =range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)

#回文词检查(palindrome)
def palindrome(word):
    '''
    :param word:str,输入的单词
    '''
    word = word.lower()
    return word[::-1] == word

print(palindrome('Mother'))
print(palindrome('Mom'))

#变位词(anagram)
def anagram(str1,str2):
    '''
    :param str1:比较的第一个单词
    :param str2:比较的第二个单词
    :return bool:返回比较结果
    '''
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2) 

print(anagram('iceman','cinema'))
print(anagram('leaf','tree'))




#计算字母频数
def count_characters(string):
    count_dict={}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        if c not in count_dict:
            count_dict[c] = 1
    print(count_dict)

count_characters('Dynasty')


#递归(recursion)
def bottles_of_beer(bob):
    '''
    Prints 99 Bottle 
    of Beer on the 
    Wall lyrics.
    :param bob:Must
    be a positive 
    integer.
    '''
    if bob<1:
        print("""No more bottles of beer on the wall. No more bottles of  beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer. 
    Take one down, pass it around, {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(99)



















































