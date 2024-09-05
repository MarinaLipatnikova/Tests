documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return "Документ не найден"

def get_directory(doc_number):
    for id, dir in enumerate(directories.values()):
        if doc_number in dir:
            list_ = list(directories.keys())
            return list_[id]
    return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
    documents.append({'type': document_type, 'number': number, 'name': name})
    directories[shelf_number] = number

