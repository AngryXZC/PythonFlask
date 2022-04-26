import CocaCola as coke
import CaffeineFree as myCoke
# coke_for_me=coke.CocaCola()
# coke_for_you=coke.CocaCola()
# # print(coke.CocaCola.formula)
# # print(coke_for_me.formula)
# # print(coke_for_you.formula)
# coke_for_china=coke.CocaCola()
# coke_for_china.local_logo="可口可乐"
# coke_for_china.drink();
# coke.CocaCola.drink(coke_for_china)
# print(coke_for_china.local_logo)

# ice_coke=coke.CocaCola()
# ice_coke.drink("a sip")
# print(ice_coke.local_logo)

# ice_coke=coke.CocaCola("可口可乐")
# print(ice_coke.local_logo)

# coke_a= myCoke.CaffeineFree("Cocacola-FREE")
# coke_a.drink()

##类属性被重新被赋值
# class TestA:
#     attr = 1 
# obj_a = TestA() 
# TestA.attr = 42
# print(obj_a.attr)

# class TestA:
#     attr = 1
# obj_a = TestA()
# obj_b = TestA()
# obj_a.attr = 42
# print(obj_b.attr)

# class TestA:
#     attr = 1
# obj_a = TestA()
# obj_b = TestA()
# obj_a.attr = 42
# print(obj_b.attr)
# print(TestA.__dict__)
# print(obj_a.__dict__)
'''类的扩展理解'''
# obj1 = 1
# obj2 = 'String!'
# obj3 = []
# obj4 = {}
# print(type(obj1),type(obj2),type(obj3),type(obj4))


from bs4 import BeautifulSoup

soup=BeautifulSoup()

print(type(soup))
