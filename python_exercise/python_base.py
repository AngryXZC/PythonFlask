
print(__name__)
if  __name__=="__main__":
    '''整型测试'''
    a,b,c,d=50,5.5,True,5+3j
    print(type(a),type(b),type(b),type(c),type(d))
    '''字符串不赘述'''
    '''列表 不赘述'''
    '''元组只读，不能修改，不能修改(不变的可读列表)'''
    '''集合'''
    student={"Tom","Jack","Marry","Jim","Rose"}
    
    print(student);
    if "Rose" in student:
        print("Rose 在集合中")
    else:
        print("Rose不在集合中")
    '''字典不赘述'''