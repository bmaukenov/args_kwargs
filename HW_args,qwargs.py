
# Не использовал *args в выводе контакта в классе Contact, потому вроде что любая дополнительная  
# информация в контактах является необязательным именованным аргументом. 


class Contact:
        def __init__(self, name, surname, number, chosen=False, *args, **kwargs):
            self.name = name
            self.surname = surname
            self.number = number
            if chosen is False:
                self.chosen = "нет"
            else:
                self.chosen = "да"
            self.kwargs = kwargs


        def __str__(self):
            def additional_info_func():
                line = ""
                for key in self.kwargs.keys():
                    line += f"    {key} : {self.kwargs[key]}\n"
                return line
            return f"Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.number}\nВ избранных: {self.chosen}\nДополнительная информация:\n{additional_info_func()}"



class PhoneBook:
    def __init__(self, name, contacts=[]):
        self.name = name
        self.contacts = contacts
        self.chosen_contacts = []

    def print_contacts(self):
        for contact in self.contacts:
            print(f"{contact}\n")

    def add_contact(self, contact):
        self.contacts.append(contact)
        if contact.chosen:
            self.chosen_contacts.append(contact)

    def delete_contact(self, contact):
    	self.contacts.remove(contact)

    def search_chosens(self):
        for contact in self.chosen_contacts:
            print(f"{contact}\n\n")

    def search_contact(self, query):
        queried_contacts = []
        for contact in self.contacts:
            if contact.name.find(query) != -1:
                print(f"{contact}\n\n")
            elif contact.surname.find(query) != -1:
                print(f"{contact}\n\n")



if __name__ == "__main__":
    test = Contact("Бексултан", "Маукенов", "+77758327252", chosen=True, telegram="@Beksultan_Maukenov", email="bmaukenov@gmail.com")
    testBook = PhoneBook("MyPhoneBook")
    testBook.add_contact(test)
    testBook.print_contacts()
    testBook.search_chosens()
    testBook.search_contact("укен")
