import json
from argparse import ArgumentParser
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
        to_json = json.dumps(human.__dict__)
        with open("human.txt", "w") as file:
            json.dump(to_json, file)

    @staticmethod
    def convert_to_xml():
        human = Human("John", 15, "man", 2003)
        xml_from_class = xml_marshaller.dumps(human.__dict__)
        with open("human.xml", "wb") as file:
            xml_marshaller.dump(xml_from_class, file)


parser = ArgumentParser(description="Converter")
parser.add_argument('--convert', help='Converts to json or xml', default='xml to cli')
arguments = parser.parse_args()

if arguments.convert == 'json to cli':
    Human.convert_to_json()
elif arguments.convert == 'xml to cli':
    Human.convert_to_xml()
