#class attribute
class Date:
    separator='/' #class attribute
    def __init__(self):
        self._year, self._month, self._day =0,0,0
    def print_date(self):
        print(str(self._month), end='')
        print(Date.separator, end='') # to call a class attribute is name_class.name_class_attribute
        print(str(self._day), end='')
        print(Date.separator, end='')
        print(str(self._year))
d_1, d_2 = Date(), Date()
d_1._year, d_1._month, d_1._day = 2021,11,4
d_2._year, d_2._month, d_2._day = 2015,5,16
d_1.print_date()
d_2.print_date()
Date.separator = ':'
d_1.print_date()
d_2.print_date()
