# class CocaCola:
#     formula=['caffine','sugar','water','soda']
#     def drink(coke,how_much):
#         print("Energy")
#         if how_much=="a sip":
#             print("Cool")
#         elif how_much=="whole bottle":
#             print("Headache")
#     def __init__(self,logo_name):
#         # self.local_logo="可口可乐"
#         # for element in self.formula:
#         #     print("Coke has {}".format(element))
#         self.local_logo=logo_name


class CocaCola:
    calories=140
    sodium=45
    total_carb=39
    caffeine=34
    ingredients=[
        "High Fructose Corn Syrup",
        "Carbonate Water",
        "Phosphoric Acid",
        "Natural Flavors",
        "Caramel Color",
        "Caffeine"
    ]
    def __init__(self,logo_name):
        self.local_logo=logo_name
    def drink(self):
        print("You got {} cal energy!".format(self.calories))
