import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
        result = re.search(r"\d{10}", self.value)
        if not (result and len(self.value) == 10):
            self.value = None
            n = int("b")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"

    def add_phone(self, phone):
        phone2 = Phone(phone)
        if phone2.value:
            self.phones.append(phone2.value)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone_1, phone_2):
        if phone_1 not in self.phones:
            int("a")
        phone_2 = Phone(phone_2)
        if phone_2.value:
            for phone_obj in self.phones:
                if phone_obj == phone_1:
                    index = self.phones.index(phone_1)
                    self.phones.remove(phone_1)
                    self.phones.insert(index, phone_2.value)

    def find_phone(self, phone):
        phone = Phone(phone)
        for phone_obj in self.phones:
            if phone_obj == phone.value:
                return Phone(phone_obj)


class AddressBook(UserDict):
    def add_record(self, book_record):
        phone_list = self.data.get(book_record.name.value, [])
        for phone in book_record.phones:
            phone_list.append(phone)
        self.data[book_record.name.value] = phone_list

    def find(self, find_name):
        phones = self.data.get(find_name, None)
        if phones:
            f_record = Record(find_name)
            f_record.name.value = find_name
            f_record.phones = phones
            return f_record
        return None

    def delete(self, del_name):
        ty = self.data.pop(del_name, None)


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("1234598760")
    john_record.add_phone("12345abcde")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print("test2")
    print(book.find("John"))
    print(john_record)
    print("test2")

    john2_record = Record("John")
    john2_record.add_phone("1234511111")
    book.add_record(john2_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Створення та додавання нового запису для Yurii
    yur_record = Record("Yurii")
    yur_record.add_phone("0953676538")
    book.add_record(yur_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(f'{name}: {record}')

    # Знаходження та редагування телефону для John
    john = book.find("John")

    john.edit_phone("1234567890", "12345abcde")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    john.edit_phone("1234567890", "5555555555")

    print(john)

    jane = book.find("Jane")

    print(jane)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

