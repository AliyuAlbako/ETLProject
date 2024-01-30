from pony.orm import *
from customers import customers_entities
from pony import orm
import json
import csv
import xml.etree.ElementTree as ET
# creating database object and binding the object to sqlite database
db = Database()
db.bind(provider="sqlite", filename="databaseFile2.db", create_db=True)
customer = customers_entities(db, orm)
db.generate_mapping(create_tables=True)
# creating customer entity

# paths to the 3 data files saved in variables
csv_fil_path = "../data/user_data_23_4.csv"
json_file_path = "../data/user_data_23_4.json"
xml_file_path = "../data/user_data_23_4.xml"

# function read csv file


def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_file]
    return data

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
# cleaning up the csv data and convert the data into list of dictionaries
keys = ['firstName', 'lastName', 'age', 'sex', 'Vehicle_make', 'Vehicle_model', 'Vehicle_year', 'Vehicle_type']
csv_dic_data = []
for data in (csv_data[1:]):
    dt = data.split(',')
    mydic = dict(zip(keys, dt))
    csv_dic_data.append(mydic)

matcheddic = []
matchedCSV_XML = []
# matching csv data with json file to fetch one  customer customers that exist in both files
for dy in csv_dic_data:
    for dx in json_data:
        if dx['firstName'].title() == dy['firstName'].title() and dx['lastName'].title() == dy['lastName'].title():
            matcheddic.append(dx)

# # matching csv data with xml file to fetch one  customer customers that exist in both files

for dy in csv_dic_data:
    for dx in xml_data:
        if dx['firstName'].title() == dy['firstName'].title() and dx['lastName'].title() == dy['lastName'].title():
            matchedCSV_XML.append(dx)


@db_session()
def insert(Customer):
    counting = 0
    while counting < len(csv_dic_data):
        Customer(
                first_name=csv_dic_data[counting]['firstName'],
                last_name=csv_dic_data[counting]['lastName'],
                age=csv_dic_data[counting]['age'],
                sex= csv_dic_data[counting]['sex'],
                vehicle_make= csv_dic_data[counting]['Vehicle_make'],
                vehicle_model= csv_dic_data[counting]['Vehicle_model'],
                vehicle_year= csv_dic_data[counting]['Vehicle_year'],
                vehicle_type=  csv_dic_data[counting]['Vehicle_type'],
                iban= matcheddic[counting]['iban'],
                credit_card_number=matcheddic[counting]['credit_card_number'],
                credit_card_security_code=matcheddic[counting]['credit_card_security_code'],
                credit_card_start_date=matcheddic[counting]['credit_card_start_date'],
                credit_card_end_date=matcheddic[counting]['credit_card_end_date'],
                address_main=matcheddic[counting]['address_main'],
                address_city=matcheddic[counting]['address_city'],
                address_postcode=matcheddic[counting]['address_postcode'],
                retired=matchedCSV_XML[counting]['retired'],
                dependants=matchedCSV_XML[counting]['retired'],
                marital_status=matchedCSV_XML[counting]['retired'],
                salary = matchedCSV_XML[counting]['salary'],
                pension = matchedCSV_XML[counting]['pension'],
                company = matchedCSV_XML[counting]['company'],
                commute_distance = matchedCSV_XML[counting]['commute_distance'],


               )
        counting += 1

    return Customer


insert(customer)


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
print("Data Save Successfully")