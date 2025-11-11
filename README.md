# Лабораторная работа №5
## Задание А - JSON ↔ CSV
```python

import csv
import json
import sys
import os
from pathlib import Path

def check_file_extension(file_path: str, expected_extensions: tuple) -> bool:
    return any(Path(file_path).suffix.lower().endswith(ext) for ext in expected_extensions)


def json_to_csv(json_path: str, csv_path: str) -> None:
    #функция конвертанции JSON в CSV


    if not check_file_extension(json_path, ('.json',)):  #проверяем расширение входящего файла
        raise ValueError(f"Входной файл не является JSON.")

    if not os.path.exists(json_path): #проверяет, существует ли файл по указанному пути
        raise FileNotFoundError #если не существует выдает ошибку
    if os.path.getsize(json_path) == 0: #получает размер файла в байтах и проверяет, равен ли размер нулю (пустой файл или нет)
        raise ValueError

    with open(json_path, 'r', encoding='utf-8') as json_file: #безопасно открывае файл для прочтения(автомвтически закрывает после использовния #json_path - путь к файлу
        json_data = json.load(json_file) #закгружает и преобразовывает JSON данные в Python объект #json_data - переменная, содержащая данные из JSON файла
        if not all(type(x) == dict for x in json_data): #type(x) == dict - проверяет, является ли элемент словарем
                                                        #for x in json_data - перебирает все элементы в данных
                                                        #all() - проверяет, что ВСЕ элементы соответствуют условию
                                                        #if not all() - если НЕ все элементы являются словарями
            raise ValueError #если не все элементы подходят под условие выдает ошибку


    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile: #открывает CSV файл для записи(или замены)                                                                           #newline='' - убирает лишние пустые строки
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) #csv.DictWriter() - создает объект для записи CSV из словарей
                                                                         #fieldnames=json_data[0].keys() - название колонок берутся из ключей первого словаря
        writer.writeheader() #запиывает заголовок(название колонок) в CSV файл
        writer.writerows(json_data) #записывает все данные из JSON в CSV файл

def csv_to_json(csv_path: str, json_path: str) -> None: #функция конвертанции CSV в JSON
    if not os.path.exists(csv_path): #проверяет, существует ли файл по указанному пути
        raise FileNotFoundError #если не существует выдает ошибку

    if os.path.getsize(csv_path) == 0: #получает размер файла в байтах и проверяет, равен ли размер нулю (пустой файл или нет)
        raise ValueError

    with open(csv_path, 'r', encoding='utf-8') as csvfile: #безопасно открывае файл для прочтения(автомвтически закрывает после использовния #csv_path - путь к файлу
        reader = csv.reader(csvfile) #создает объект для чтения CSV
        header = next(reader, None) #читает первую строку(заголовок), NONE - значение по умолчанию, если файл пустой
        if not header: #проверяет, что заголовк есть
            raise ValueError #если заголовка нет выводит ошибку

        reader = csv.DictReader(csvfile) #читает файл
        data = list(reader) #преобразовывет все данные в список
    with open(json_path, 'w', encoding='utf-8') as jsonfile:  #открывает JSON файл для записи(или замены)
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) #json.dump() - записывает Python объект в JSON файл
                                                                #ensure_ascii=False - разрешает русские символы
                                                                #indent=4 - красивое форматирование с отступами
csv_to_json(r"/Users/matvejtetevin/laba/src/date/samples/people.csv", r"/Users/matvejtetevin/laba/src/date/out/people_from_csv.json")

json_to_csv( r"/Users/matvejtetevin/laba/src/date/samples/people.json",  r"/Users/matvejtetevin/laba/src/date/out/people_from_json.csv" )

```
## Задание B - CSV → XLSX
```python
import os
import csv
import sys
from pathlib import Path

from openpyxl import Workbook #из библиотеки openpyx1 импортирует только класс Workbook для создаия Excel файлов

def check_file_type(file_path: str, valid_types: tuple) -> bool: #функция для проверки типа файла по расширению

    return Path(file_path).suffix.lower() in valid_types


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None: #функция конвертанции CSV в XLSX
    if not os.path.exists(csv_path): #если не существует файл по указанному пути, то
        raise FileNotFoundError #выводит сообщение об ошибке
    if not check_file_type(csv_path, ('.csv',)): #проверка расширения входящего файла (должен быть .csv)
        raise ValueError(f"Входной файл '{csv_path}' не является CSV.")

    if not check_file_type(xlsx_path, ('.xlsx',)):  #проверка расширения выходящего файла (должен быть .xlsx)
        raise ValueError(f"Выходной файл '{xlsx_path}' не является XLSX.")

    if os.path.getsize(csv_path) == 0: #получает размер в байтах и проверяет не равен ли он 0 (пустой файл)
        raise ValueError

    wb = Workbook() #создаем новую Excel книгу
    ws = wb.active #берем первый лист
    ws.title = "Sheet1" #переменовываем лист в Sheet1

    with open(csv_path, "r", encoding="utf-8") as csv_file: #безопасно открывае файл для прочтения(автомвтически закрывает после использовния #csv_path - путь к файлу
        reader = csv.reader(csv_file) #создает объект для чтения CSV файла
        for row in reader: #перебирает каждую строку в CSV файле, row - переменная, содержащая данные одной строки(как список)
            ws.append(row) #добавляет строку данных в Excel лист

#Настройка ширины колонок
    for column_cells in ws.columns: #перебирает содержания ячейки одной колонки и возвращает все колонки листа
        max_length = 0 #создает переменную для хранения максимальной длины теста в колонке
        column_letter = column_cells[0].column_letter #присваивает букву колонки
        for cell in column_cells: #перебирает все ячейки в текущей колонке
            if cell.value: #проверяет есть ли значение в ячейки(не пустая)
                max_length = max(max_length, len(str(cell.value))) #обновляет длину строкиб сравнивая прошлое значение с настоящим
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8) #обращается к настройкам ширины конкретной колонки, устанавливает ширину колонки, максимальная длина + 2 символа для отступа, 8- выбирает большее значение между расчитанной шириной и минимальной шириной 8
    wb.save(xlsx_path) #сохраняет Excel книгу по указанному пути
csv_to_xlsx(r"/Users/matvejtetevin/laba/src/date/samples/cities.csv", r"/Users/matvejtetevin/laba/src/date/out/people.xlsx")
```  