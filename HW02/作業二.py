
# coding: utf-8

# In[ ]:


import os                                                           #os為模組名稱
def main():                                                         #main只是一個慣例，非必要條件
    print "Hello world!"                                            #需加4個空白格，才會開始執行 ####
    print "This is Alice's greeting."
    print "This is Bob\'s greeting."
    
    foo(5,10)                                                       #呼叫函數
    
    print "="*10                                                    #=複製10次
    print "Current working directory is" + os.getcwd()              # +號:字串並列. #取工作目錄
    
    counter=0                                                       #變數一開始須被實例化
    counter+=1  
    
    food=["apples","oranges","cats"]                                #同一個清單中,可包含 不同資料型態、其他清單
    
    for i in food:                 
        print "I like to eat"+i    
        print "Count to eat:"
        for i in range(10):        #range()function為[0,1,2,3,4,5,6,7,8,9]  #須加冒號
            print i
            
def foo(param1, secondParam):                                       #定義函數  #須加冒號
    res=param1+secondParam
    print "%s plus %s is equal to %s" % (param1, secondParam, res)  # %s :字串插入，與在C中作的一樣

    if res<50:                                                      #當res<50 ,印出foo
        print"foo"
    elif(res>=50)and((param1==42)or(secondParam==24)):              #當res>50,param1為42,secondParam為24,印出bar 
        print"bar"
    else:                                                           #其他,印出moo
        print"moo"
    return res                                                      # This is a one-line comment.
    '''Amulti-
line string, but can also be a multi-line comment.'''               #長的字串不影響縮排  #縮排只在敘述的一開始

if__name__=='__main__': #當呼叫 main,會執行每一敘述 
    main()              #當 name 被執行時(非載入),name中有main 
                        #若其他字串載入name,main不會被執行
    

