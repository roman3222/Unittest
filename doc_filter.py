documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded


def get_doc_owner_name(doc_num):
    doc_exist = check_document_existance(doc_num)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == doc_num:
                return current_document['name']


def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)


def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break
    return directories


def add_new_shelf(shelf_number=''):
    if  shelf_number:
        shelf_number = input('Введите номер полки - ')
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, True
    return shelf_number, False


def append_doc_to_shelf(doc_number, shelf_number):
    for i in directories:
        if shelf_number in i:
            directories[shelf_number].append(doc_number)
    return directories


def delete_doc(num_doc):
    doc_exist = check_document_existance(num_doc)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == num_doc:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return doc_number, True


def get_doc_shelf(doc_num):
    doc_exist = check_document_existance(doc_num)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if doc_num in directory_docs_list:
                return directory_number


def move_doc_to_shelf(doc_num, num_shelf):
    if not any(doc['number'] == doc_num for doc in documents):
        raise ValueError(f'Документ с номером "{doc_num}" не найден')
    remove_doc_from_shelf(doc_num)
    append_doc_to_shelf(doc_num, num_shelf)
    print('Документ номер "{}" был перемещен на полку номер "{}"'.format(doc_num, num_shelf))
    return directories



def show_all_docs_info():
    all_doc = []
    for doc in documents:
        for v in doc.values():
            all_doc.append(v)
    return all_doc




def add_new_doc(type_doc, doc_num, name, shelf_num):
    new_doc = {
        "type": type_doc,
        "number": doc_num,
        "name": name
    }
    documents.append(new_doc)
    append_doc_to_shelf(doc_num, shelf_num)
    return directories


def secretary_program_start(user_command):
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help, для просмотра списка поддерживаемых команд)\n'
    )
    while True:
        if user_command == 'p':
            owner_name = get_doc_owner_name()
            print('Владелец документа - {}'.format(owner_name))
        elif user_command == 'ap':
            uniq_users = get_all_doc_owners_names()
            print('Список владельцев документов - {}'.format(uniq_users))
        elif user_command == 'l':
            show_all_docs_info()
        elif user_command == 's':
            directory_number = get_doc_shelf()
            print('Документ находится на полке номер {}'.format(directory_number))
        elif user_command == 'a':
            print('Добавление нового документа:')
            new_doc_shelf_number = add_new_doc()
            print('\nНа полку "{}" добавлен новый документ:'.format(new_doc_shelf_number))
        elif user_command == 'd':
            doc_number, deleted = delete_doc()
            if deleted:
                print('Документ с номером "{}" был успешно удален'.format(doc_number))
        elif user_command == 'm':
            move_doc_to_shelf()
        elif user_command == 'as':
            shelf_number, added = add_new_shelf()
            if added:
                print('Добавлена полка "{}"'.format(shelf_number))
        elif user_command == 'help':
            print(secretary_program_start.__doc__)
        elif user_command == 'q':
            break


if __name__ == '__main__':
    print(get_doc_owner_name('11-2'))