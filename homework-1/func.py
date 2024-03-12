import csv


def data_read(csv_file):
    """
    Получает csv файл, возвращает списком
    """
    file = open(csv_file, 'r', newline='')
    data = csv.reader(file)
    next(data)
    return data
