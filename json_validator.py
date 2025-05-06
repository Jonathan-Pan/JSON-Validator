#
# This Python script tool is used to validate json syntax format correct or not based on:
# - one single json file
# - one list file which contains multiple json files  
# 
# Author: Jian-Hua Pan(Jonathan)
# Email 1& MS Teams: hdpanjianhua@msn.com
# Email 2: fdpjh@126.com
#
# Version: 1.0
# Update on 2022-5-16

from email import parser
import json
import sys
import argparse
import textwrap

# Validate json syntax format function
def validate_json(filename):
    try:
        json.load(filename)
    except ValueError as err:
        print(err)
        return False
    return True    

# configure file name argument 
arg_parser = argparse.ArgumentParser(
			prog='json_validator.exe',
			formatter_class=argparse.RawDescriptionHelpFormatter,
			description=textwrap.dedent('''\
							JSON Syntax Format Validation Tool
			---------------------------------------------------------------------------------------------------------
			* Default: run the tool directly without any argument,
			           check all json files in "json_file_list.txt" file hardcoded in the same folder of the tool. 

			* Optional: run the tool with "-f" or "--filename", check one single json file. 
					e.g. json_validator.exe -f C:\json_validator\mcc-widgets_de.json
					     json_validator.exe --filename C:\json_validator\mcc-widgets_de.json
			----------------------------------------------------------------------------------------------------------
			'''))

arg_parser.add_argument('-f', '--filename', required=False, help='one single json file path name')
args = arg_parser.parse_args()

# Call validate_json function based on one single json file or json list file
print("############################################################")
print("Start validating JSON files...")
print(" ")

# default: check json list file
if args.filename is None:

	with open('json_file_list.txt') as files:
		for file in files:
			# print(type(file))
			file = file.strip()
			
			with open(file, encoding='utf8') as f:

				print(file)
				print("Valid JSON? : ",validate_json(f))
				print("************************************************************")
# customized: check provided single json file
else:
	single_file = args.filename 

	with open(single_file, encoding='utf8') as f:
		print(single_file)
		print("Valid JSON? : ",validate_json(f))
		print("************************************************************")	

print(" ")
print("Finish validating JSON files! ^_^")
print("############################################################")

