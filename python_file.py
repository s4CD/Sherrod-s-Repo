#! /usr/bin/python

import xml.etree.ElementTree as EL

file 							= EL.parse('data.xml')
root 							= file.getroot()


#I'm just playing around with Python 
company_name 					= root.tag
boss_position 					= root[0].tag
director_first_name 			= root[0][0].text
director_last_name 				= root[0][1].text

for full_name in root.findall("director"):
	first_name = full_name.find("first_name").text
	last_name  = full_name.find("last_name").text

	print(first_name, last_name)


