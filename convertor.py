import json
from argparse import ArgumentParser
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
from xml_marshaller import xml_marshaller



class Human:
    def __init__(self, name: str, age: int, gender: str, birth_year: int):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    @staticmethod
    def convert_to_json():
        human = Human("John", 15, "man", 2003)
        to_json = json.dumps(vars(human))
        to_file = json.loads(to_json)
        with open("human.json", "w") as file:
            json.dump(to_file, file, indent=4)

    @staticmethod
    def convert_to_xml():
        human = Human("John", 15, "man", 2003)
        xml_from_class = xml_marshaller.dumps(vars(human))
        xml_data = xml_marshaller.loads(xml_from_class)
        xml = dicttoxml(xml_data, attr_type=False)
        xml_decode = xml.decode()
        xml_format = parseString(xml_decode).toprettyxml()
        xml_file = open("human.xml", "w")
        xml_file.write(xml_format)
        xml_file.close()


parser = ArgumentParser(description="Converter")
parser.add_argument('--convert', help='Converts to json or xml', default='jsontocli')
arguments = parser.parse_args()

if arguments.convert == 'jsontocli':
    Human.convert_to_json()
elif arguments.convert == 'xmltocli':
    Human.convert_to_xml()
