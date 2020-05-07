import keyword
import math
import random
import statistics


print(math.pow(2,3))

print(random.randint(0,100))

nums=[1,5,33,12,46,33,2]
#均值
print(statistics.mean(nums))

#中值
print(statistics.median(nums))

#众数
print(statistics.mode(nums))


#查看是否是关键字
print(keyword.iskeyword('for'))
print(keyword.iskeyword('football'))

#导入自建module
import hello
hello.print_hello()



















