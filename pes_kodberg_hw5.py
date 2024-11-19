# task 2 Створити клас Contact з полями surname, name, age, mob_phone, email. Додати методи get_contact, sent_message.
# Створити клас-нащадок UpdateContact з полями surname, name, age, mob_phone, email, job. Додати методи get_message.
# Створити екземпляри класів та дослідити стан об'єктів за допомогою атрибутів: __dict__, __base__, __bases__. 
# Роздрукувати інформацію на екрані.

import inspect

class Contact:
    def __init__(self, surname:str, name:str, age:int, mob_phone:str, email:str):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
    
    def get_contact(self):
        return f'{self.surname}, {self.name}: {self.age} years old'

    def sent_message(self):
        return f'To send SMS by mobile phone number {self.mob_phone} or by email {self.email}'

class UpdateContact(Contact):
    def __init__(self, surname:str, name:str, age:int, mob_phone:str, email:str, job:str):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f'Message will be sent to email {self.email}'


who1 = Contact('Smith', 'John', 40, '5552467', 'js@gmail.com')
who2 = UpdateContact('Duck', 'Donald', 45, '5551276', 'dd@gmail.com', 'worker')
print(who1.get_contact())
print(who1.sent_message())
print(who2.get_contact())
print(who2.sent_message())
print(who2.get_message())

print(who1.__dict__)
print(who2.__dict__)
print(Contact.__base__)
print(UpdateContact.__base__)
print(Contact.__bases__)
print(UpdateContact.__bases__)

# task 3 Використовуючи код з завдання 2, використати функції hasattr(), getattr(), setattr(), delattr().
# Застосувати ці функції до кожного з атрибутів класів, подивитися до чого це призводить.

print(hasattr(who1, 'surname'))
print(hasattr(who1, 'job'))
print(hasattr(who2, 'job'))
print(getattr(who1, 'name'))
print(getattr(who2, 'job'))
setattr(who1, 'age', 38)
print(who1.age)
setattr(who2, 'job', 'driver')
print(who2.job)
delattr(who1, 'age')
print(hasattr(who1, 'age'))

# task 4 Використовуючи код з завдання 2, створити 2 екземпляри обох класів.
# Використати функції isinstance() – для перевірки екземплярів класу (за яким класом створені) та issubclass() – для перевірки і визначення класу-нащадка.

print(isinstance(who1, Contact))
print(isinstance(who2, UpdateContact))
print(isinstance(who1, UpdateContact))
print(isinstance(who2, Contact))
print(issubclass(Contact, UpdateContact))
print(issubclass(UpdateContact, Contact))

# task 5 Використовуючи код завдання 2 надрукуйте у терміналі інформацію, яка міститься у класах Contact та UpdateContact та їх екземплярах.
# Видаліть атрибут job, і знову надрукуйте стан класів та їх екземплярів. Порівняйте їх. Зробіть відповідні висновки.

print(dir(Contact('Smith', 'John', 40, '5552467', 'js@gmail.com')))
print(dir(UpdateContact('Duck', 'Donald', 45, '5551276', 'dd@gmail.com', 'worker')))
print(Contact.__dict__)

# task 6 Використовуючи код завдання 2 надрукуйте у терміналі всі методи, які містяться у класі Contact та UpdateContact.

print(inspect.ismethod(who1.get_contact))
print(inspect.ismethod(who1.sent_message))
print(inspect.ismethod(who1))
print(inspect.ismethod(who2.get_message))
print(inspect.ismethod(who2))
