import json
def load_phonebook():
    try:
        with open('phonebook.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_phonebook(data):
    with open('phonebook.json', 'w') as file:
        json.dump(data, file, indent=4)

def search_contacts(query):
    contacts = load_phonebook()
    search_results = []
    for contact in contacts.values():
        if query.lower() in contact['first_name'].lower() or query.lower() in contact['last_name'].lower():
            search_results.append(contact)
    return search_results

def update_contact(contact_id):
    contacts = load_phonebook()
    if contact_id in contacts:
        print('Введите новые данные контакта:')
        first_name = input('Имя: ')
        last_name = input('Фамилия: ')
        phone_number = input('Номер телефона: ')
        email = input('Адрес электронной почты: ')
        contacts[contact_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'email': email
        }
        save_phonebook(contacts)
        print('Контакт успешно обновлен.')
    else:
        print('Контакт не найден.')

def delete_contact(contact_id):
    contacts = load_phonebook()
    if contact_id in contacts:
        del contacts[contact_id]
        save_phonebook(contacts)
        print('Контакт успешно удален.')
    else:
        print('Контакт не найден.')

# Пример использования функций

def main():
    while True:
        print('Меню:')
        print('1. Поиск контакта')
        print('2. Изменение контакта')
        print('3. Удаление контакта')
        print('4. Выход')
        choice = input('Выберите опцию: ')

        if choice == '1':
            query = input('Введите имя или фамилию для поиска: ')
            results = search_contacts(query)
            if results:
                print('Результаты поиска:')
                for contact in results:
                    print(f'Имя: {contact["first_name"]}')
                    print(f'Фамилия: {contact["last_name"]}')
                    print(f'Номер телефона: {contact["phone_number"]}')
                    print(f'Адрес электронной почты: {contact["email"]}')
            else:
                print('Контакты не найдены.')

        elif choice == '2':
            contact_id = input('Введите идентификатор контакта для изменения: ')
            update_contact(contact_id)

        elif choice == '3':
            contact_id = input('Введите идентификатор контакта для удаления: ')
            delete_contact(contact_id)

        elif choice == '4':
            break

        else:
            print('Неправильный выбор. Повторите ввод.')

if __name__ == '__main__':
    main()