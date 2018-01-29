import argparse
import plistlib
import datetime
import xml.etree.ElementTree as ElementTree
import re
import Constants
import iphone_parser


# Parse a plist file
def parse_plist_file(file_path):
    with open(file_path, 'rb') as file_pointer:
        plist_file = plistlib.load(file_pointer)
    return plist_file


# Convert dictionary key names to readable names (product_version -> Product version)
def convert_to_readable(string):
    return ' '.join(string.split('_')).capitalize()


def convert_to_xml(string):
    return ''.join(string.split('\n'))


def parse_storage_master_to_txt(storage_master):
    parsed_text_array = []

    for storage_category, storage_data in storage_master.items():
        title = convert_to_readable(storage_category)
        parsed_text_array.append(f"{'-' * len(title)}\n{title}\n{'-'* len(title)}\n")

        if isinstance(storage_data, list):
            # Create columns
            for key in storage_data[0].keys():
                parsed_text_array.append(f"* {convert_to_readable(key)} *{' ' * (Constants.COLUMN_WIDTH - (len(key) + 4))}")
            parsed_text_array.append("\n")

            # Populate columns with data
            for list_item in storage_data:
                for iphone_information_key, iphone_information_data in list_item.items():
                    parsed_text_array.append(
                        f"{iphone_information_data}{' ' * (Constants.COLUMN_WIDTH - len(iphone_information_data))}")
                parsed_text_array.append("\n")
        elif isinstance(storage_data, dict):
            for iphone_information_key, iphone_information_data in storage_data.items():
                if isinstance(iphone_information_data, dict):
                    parsed_text_array.append(f"{convert_to_readable(iphone_information_key)}:\n")
                    for dictionary_key, dictionary_value in iphone_information_data.items():
                        parsed_text_array.append(f"\t{convert_to_readable(dictionary_key)}\n\t{dictionary_value}\n")

                else:
                    parsed_text_array.append(
                        f"{convert_to_readable(iphone_information_key)}:\n\t {iphone_information_data}\n")
                parsed_text_array.append("\n")
        else:
            parsed_text_array.append(storage_data)

    return parsed_text_array


def check_and_convert_illegal_xml_tag_start(tag):
    tag = str(tag)
    return f"{Constants.XML_IGNORE_CHARACTER_STRING}{tag}" if re.match('^\d', str(tag)) else tag


def parse_storage_master_to_xml(storage_master):
    # TODO: Add this Parsing method into functions to allow for easier to read and less repeating code
    root_elem = ElementTree.Element('root')
    # backup_number_elem = args.backup_paths[i]

    for storage_category, storage_data in storage_master.items():
        title_elem = ElementTree.SubElement(root_elem, storage_category)

        if isinstance(storage_data, list):
            for list_item in storage_data:
                list_item_elem = ElementTree.SubElement(title_elem, 'Item')
                for iphone_information_key, iphone_information_data in list_item.items():
                    iphone_information_key_elem = ElementTree.SubElement(list_item_elem, iphone_information_key)
                    iphone_information_key_elem.text = str(iphone_information_data)
        elif isinstance(storage_data, dict):
            for iphone_information_key, iphone_information_data in storage_data.items():
                if isinstance(iphone_information_data, dict):
                    iphone_information_key_elem = ElementTree.SubElement(title_elem, check_and_convert_illegal_xml_tag_start(iphone_information_key))
                    for dictionary_key, dictionary_value in iphone_information_data.items():
                        if isinstance(dictionary_value, dict):
                            for dictionary_key_2, dictionary_value_2 in dictionary_value.items():
                                dictionary_key_2_elem = ElementTree.SubElement(dictionary_key_elem, check_and_convert_illegal_xml_tag_start(dictionary_key_2))
                                dictionary_key_2_elem.text = str(dictionary_value_2)

                        else:
                            dictionary_key_elem = ElementTree.SubElement(iphone_information_key_elem, check_and_convert_illegal_xml_tag_start(dictionary_key))
                            dictionary_key_elem.text = str(dictionary_value)
                else:
                    iphone_information_key_elem = ElementTree.SubElement(title_elem, check_and_convert_illegal_xml_tag_start(iphone_information_key))
                    iphone_information_key_elem.text = str(iphone_information_data)
        else:
            title_elem.text = str(storage_data)

    return root_elem


# Create text file, requires array of dictionaries and desired txt file path
def create_text_file(master_storage, text_output_file_path):
    try:
        with open(text_output_file_path, 'w') as file_pointer:
            file_pointer.write(''.join(parse_storage_master_to_txt(master_storage)))

        print(f"TXT file '{text_output_file_path}' written successfully")
        return True
    except IOError as err:
        print("I/O error: {0}".format(err))
    except:
        print(f"An unexpected error occurred")
        raise


# Create XML file, requires array of dictionaries and desired xml file path
def create_xml_file(master_storage, xml_output_file_path):
    root = parse_storage_master_to_xml(master_storage)
    tree = ElementTree.ElementTree(root)
    tree.write('xml_test_output.xml')


# Displays all information in the master storage
def display_all_information(storage_master):
    for element in parse_storage_master_to_txt(storage_master):
        print(element, end='')


parser = argparse.ArgumentParser(description='Analyse IPhone backups.')
parser.add_argument('backup_paths', help='The path to the IPhone backup', nargs='+')
parser.add_argument('--xml_output_path', help='The path to the desired xml path', nargs='?', default=Constants.DEFAULT_XML_OUTPUT_PATH)
parser.add_argument('--txt_output_path', help='The path to the desired txt path', nargs='?', default=Constants.DEFAULT_TXT_OUTPUT_PATH)
parser.add_argument('--xml_output_file', help='Create an xml output file', action='store_true')
parser.add_argument('--txt_output_file', help='Create a txt output file', action='store_true')
parser.add_argument('--min_std_out', help='Set the std output to the minimum amount', action='store_true')
args = parser.parse_args()
args.backup_paths.pop(0)

for backup_path in args.backup_paths:
    parsed_info_file = parse_plist_file(f'{backup_path}\{Constants.PLIST_FILE_INFO_NAME}')
    parsed_manifest_file = parse_plist_file(f'{backup_path}\{Constants.PLIST_FILE_MANIFEST_NAME}')
    parsed_status_file = parse_plist_file(f'{backup_path}\{Constants.PLIST_FILE_STATUS_NAME}')

    iphone_parser = iphone_parser.IPhoneParser(parsed_info_file, parsed_manifest_file, parsed_status_file)

    iphone_parser.parse()

    if not args.min_std_out:
        display_all_information(iphone_parser.get_storage_master())

    if args.xml_output_file:
        create_xml_file(iphone_parser.get_storage_master(), f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{iphone_parser.get_iphone_system_information()['IMEI']}_{args.xml_output_path}")

    if args.txt_output_file:
       create_text_file(iphone_parser.get_storage_master(), f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{iphone_parser.get_iphone_system_information()['IMEI']}_{args.txt_output_path}")