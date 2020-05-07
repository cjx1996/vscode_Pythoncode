import re


#the use of regular expression 
text=''' Giraffes have aroused
 the curiously of __PLURAL_NOUN__
 since earliest times. The
 giraffe is the tallest of all
 living __PLURAL_NOUN__, but 
 scientists are unable to 
 explain how it got its long 
 __PART_OF_THE_BODY__. The 
 giraffe's tremendous height,
  which might reach __NUMBER__
  __PLURAL_NOUN__, comes from 
   it legs and __BODYPART__.
'''
def mad_libs(mls):
    '''
    :param mls:字符串
    双下划綫部分的内容要由玩家来补充。
    双下划綫不能出现在提示语中，如不能
    出现 __hint_hint__，只能是__hint__。

    '''
    hints=re.findall('__.*?__',
    mls)

    if hints is not None:
        for word in hints:
            q='Enter a {}'.format(word)
            new= input(q)
            mls=mls.replace(word, new, 1)
        print('\n')
        mls=mls.replace('\n','')
        print(mls)
    else:
        print('invalid mls')

mad_libs(text)






































































































































