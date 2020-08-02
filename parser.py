# Библиотеки
from bs4 import BeautifulSoup
import requests as req
import json
import re
from DB import insert_results
# Сайт, с которого парсим
domen='https://www.reformagkh.ru'

#Создаем входные параметры Регион, город, улицу(рядом с улицей можно указывать номер дома)
# region=''#input()
# city='казань'     #input()
# street='чистопольская' #input()
# house='4'

# Создаем функцию, в атрибутах указываем входные парметры
def parser(address):

    # делаем get - запрос
    resp=req.get(domen+'/search/houses?query='+address+'+')
    soup=BeautifulSoup(resp.text,'lxml')
    search_result=soup.find('td').find('a').get('href')
    print(domen+search_result)
    res_url=domen+search_result

    # Переходим на ссылку с результатами поиска get-запроса
    resp_for_pars=req.get(res_url)
    pars=BeautifulSoup(resp_for_pars.text,'lxml')

    # Получаем выходные данные, поиск можно осуществить
    # по индексам тегов, но по ключевым словам поиск будет точнее
    birth_year=pars.find('td',text=re.compile('Год ввода дома в эксплуатацию:')).next_sibling.next_sibling.get_text()
    print(birth_year)
    floor=pars.find('td',text=re.compile('наибольшее, ед.')).next_sibling.next_sibling.get_text()
    print(floor)
    seria=pars.find('td',text=re.compile('Серия, тип постройки здания:')).next_sibling.next_sibling.get_text()
    print(seria)
    house_type=pars.find('td',text=re.compile('Тип дома:')).next_sibling.next_sibling.get_text()
    print(house_type)
    house_crash=pars.find('td',text=re.compile('Дом признан аварийным:')).next_sibling.next_sibling.get_text()
    print(house_crash)
    cadastr_number=pars.find('td',text=re.compile('Кадастровый номер')).next_sibling.next_sibling.get_text()
    print(cadastr_number)
    floor_type=pars.find('td',text=re.compile('Тип перекрытий')).next_sibling.next_sibling.get_text()
    print(floor_type)
    walls_material=pars.find('td',text=re.compile('Материал несущих стен')).next_sibling.next_sibling.get_text()
    print(walls_material)
    insert_results(address, res_url, birth_year, floor, seria,
                   house_type, house_crash, cadastr_number,
                   floor_type, walls_material)

if __name__ == '__main__':
    try:
        print("1. Написать адрес одной строкой\n"
              "2. Расширенный поиск\n"
              )
        choice = input("Введите 1 или 2: ")
        address = None
        result = -1
        if choice == '1':
            address = input("Напишите адрес, где расположен дом: ")
        if choice == '2':  # Лучше не использовать else, потому что функционал может дополниться
            region = input("Регион: ")
            city = input("Город/нас.пункт: ")
            street = input("Улица: ")
            house = input("Номер дома: ")
            address_block = input("№ корпуса(необяз): ")
            flat = input('Квартира: ')
            if address_block is not None:
                address = f"{region},г.{city},{street},д.{house},корп.{address_block},кв.{flat}"
            else:
                address = f"{region},г.{city},{street},д.{house},кв.{flat}"
                print(f"Адрес для валидации: {address}")
        parser(address)
    except NameError:
        print('Адрес не зарегистрирован либо некорректно введены данные')
