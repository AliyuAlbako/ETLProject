from typing import List

from pony.orm import *
from customers import customers_entities
from pony import orm
import json
import csv
import xml.etree.ElementTree as ET
# creating database object and binding the object to sqlite database
db = Database()
db.bind(provider="sqlite", filename="databaseFile5.db", create_db=True)
customer = customers_entities(db, orm)
db.generate_mapping(create_tables=True)
# creating customer entity

# paths to the 3 data files saved in variables
all_data= []
combined_csv_xml_data= []
csv_fil_path = "../data/user_data_23_4.csv"
json_file_path = "../data/user_data_23_4.json"
xml_file_path = "../data/user_data_23_4.xml"

# function read csv file


def read_csv(file_path):
    with open(file_path, newline='') as csv_file:
        data = csv.DictReader(csv_file)
        data2 = [row for row in data]
    return data2

# function read xml file


def read_xml(file_path):
    data = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []
    for i in root.iter():
        data.append(i.attrib)

        # data=[row for row in json_file]
    return data

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        # data=[row for row in json_file]
    return data


# calling the  function that read the json file and save the data in a variable
json_data = read_json(json_file_path)

# calling the  function that read the XML file and save the data in a variable
xml_data = read_xml(xml_file_path)
# deleting first dictionary in the list of the dictionaries generated from the XML file which happens to be empty
del xml_data[0]
# calling the function that reads the csv data and save the data in a variable
csv_data = read_csv(csv_fil_path)



@db_session()
def entity(Enty):
    Enty(
        name = 'ali',
        age= 22,
    )
    return Enty

# entity(enty)
# print(matcheddic)
# for i in matcheddic:
#     if i["credit_card_security_code"] =="099" or i["firstName"]== "Valerie":
#         print(i)

# dic_data = {}
# key_list = []
#
#
# csv_keys = list(csv_dic_data[0].keys())
# key_list.extend(csv_keys)
# json_keys = list(json_data[0].keys())
# xml_keys = list(xml_data[0].keys())
# key_list.extend(json_keys[3:])
# key_list.extend(xml_keys[4:11])
# print("Data Save Successfully")

for i in csv_data:
    for j in xml_data:
        if i['firstName']== j['firstName'] and i['lastName']== j['lastName'] and i['age']== j['age']:
            dt = i | j
            combined_csv_xml_data.append(dt)



for k in combined_csv_xml_data:
    for l in json_data:
        if k['firstName']== l['firstName'] and k['lastName']== l['lastName'] and int(k['age'])== l['age']:
            dt =k | l
            all_data.append(dt)







def write_all(file):
    with open(file, 'w', newline='') as csv_out_put:
        fieldnames= list(all_data[0].keys())
        fieldnames.append('debt')
        writer = csv.DictWriter(csv_out_put, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)

write_all("all_data.csv")

print(all_data[0].keys())






dataFromCombineFormat=read_csv('all_data.csv')

print(dataFromCombineFormat[0].keys())


@db_session()
def insert(Customer):
    for i in dataFromCombineFormat:
        if i['firstName']== 'Valerie' and i['lastName']== 'Ellis':
            i['credit_card_security_code']='762'
        Customer(
                 first_name=i['firstName'],
                last_name=i['lastName'],
                age= int(i['age']),
                 sex= i['sex'],
                vehicle_make= i['vehicle_Make'],
                vehicle_model= i['vehicle_Model'],
                vehicle_year= i['vehicle_Year'],
                vehicle_type=  i['vehicle_Type'],
                retired=i['retired'],
                dependants=i['dependants'],
                marital_status=i['marital_status'],
                salary=i['salary'],
                pension=i['pension'],
                company=i['company'],
                commute_distance=i['commute_distance'],
                address_postcode= i['address_postcode'],
                iban= i['iban'],
                credit_card_number=i['credit_card_number'],
                credit_card_security_code=i['credit_card_security_code'],
                credit_card_start_date=i['credit_card_start_date'],
                credit_card_end_date=i['credit_card_end_date'],
                address_main=i['address_main'],
                address_city=i['address_city'],
                debt=i['debt'],
                )
    print('done')
    return Customer


insert(customer)

