#以二分查找与简单查找进行比较，提出大O表示法分析算法的速度，即操作数的增速
#不仅需要知道算法多长时间都能运行完，还需要知道运行时间如何随列表增长而增长
#大O表示法指出了算法有多快。假设列表有n个元素，简单查找运行时间为O（n），二分查找为O（logn）
# 大O表示法指出了最糟情况下的运行时间
#常见的大O运行时间：
#O（logn），对数时间，包括二分查找
#O(n),线性时间，包括简单查找
# O（n*logn）,包括快速排序————速度较快
# O（n²），包括选择排序————速度较慢
# O（n！），包括旅行商问题的解决方案
def binary_search(list, item):
  low=0
  high=len(list)-1
  while low<=high:
     mid=int((low+high)/2)
     guess=list[mid]
     if guess==item:
        return mid
     if guess>item:
        high=mid-1
     else:
        low=mid+1
  return None
my_list=[1,3,5,7,9]
print(binary_search(my_list,1))
print(binary_search(my_list,-3))