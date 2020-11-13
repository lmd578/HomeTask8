#Задание 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])


    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Данные верны'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('13 - 11 - 2020')
print(today)
print(Data.valid(13, 11, 2022))
print(today.valid(13, 13, 2020))
print(Data.extract('13 - 11 - 1994'))
print(today.extract('13 - 11 - 2020'))
print(Data.valid(13, 11, 2020))



#Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionByZero(2, 4)
print(DivisionByZero.divide_by_zero(2, 0))
print(DivisionByZero.divide_by_zero(2, 1))
print(div.divide_by_zero(2, 0))


#Задание 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
#Класс-исключение должен контролировать типы данных элементов списка.


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Хотите продолжить ввод? Yes/No ')

                if y_or_n == 'Yes' or y_or_n == 'yes':
                    print(try_except.my_input())
                elif y_or_n == 'No' or y_or_n == 'no':
                    return f'Ввод прекращен'
                else:
                    return f'Ввод прекращен'


try_except = Error(1)
print(try_except.my_input())



#4-6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Warehouse:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Device model': self.name, 'Price': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} quantity {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Add name: ')
            unit_p = int(input(f'Add price per 1: '))
            unit_q = int(input(f'Add quantity: '))
            unique = {'Device model': unit, 'Price': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current list -\n {self.my_store}')

        except:
            return f'Input error'

        print(f'To escape - Q, continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Exit'
        else:
            return Warehouse.reception(self)


class Printer(Warehouse):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())



#Задание 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


z_1 = ComplexNumber(3, 1)
z_2 = ComplexNumber(9, -4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)