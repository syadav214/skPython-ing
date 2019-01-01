from chef import Chef

# Inheriting Chef class
class ChineseChef(Chef):
    def make_fried_rice(self):
        print('The chef makes fried rice')

    # Overriding method of parent class
    def make_special_dish(self):
        print('The chef makes bbq')