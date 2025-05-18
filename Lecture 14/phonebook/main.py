from lab_phonebook import Phone


def main():
    """Функция запуска программы телефонного справочника."""

    phone = Phone()
    phone.import_contacts_from_csv("contacts.csv")
    phone.show()
    phone.search_contacts()
    phone.export_contacts_to_csv("exported_contacts.csv")

if __name__ == "__main__":
    main()
