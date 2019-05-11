#!/env/bin/python3

import json
from argparse import ArgumentParser
from prettytable import PrettyTable

def main():
	parse = ArgumentParser(description='Pass the hex syscalls an argument to search')
	shells = json.loads(open('shellcodes.json').read())
	parse.add_argument('hex_arg', type=str, help='A required hex syscall to search e.g. "python main.py 0x0a"')
	getdata = parse.parse_args()
	print(getdata.hex_arg)
	noofrows = len(shells["allshells"])
	#print("Data in JSON : "+str(noofrows))
	found = -1
	for i in xrange(noofrows):
		if getdata.hex_arg == shells["allshells"][i][3]:
			found = i
			break
	if found > -1:
		#print("# : "+str(shells["allshells"][found][0]))
		print("Name : "+str(shells["allshells"][found][1]))
		print("Signature : "+str(shells["allshells"][found][2]))
		
		print("Register[EAX] : "+str(shells["allshells"][found][3]))
		if "type" in str(shells["allshells"][found][4]):
			print("Register[EBX] : "+str(shells["allshells"][found][4]["type"]))
		else:
			print("Register[EBX] : "+str(shells["allshells"][found][4]))

		if "type" in str(shells["allshells"][found][5]):
			print("Register[ECX] : "+str(shells["allshells"][found][5]["type"]))
		else:
			print("Register[ECX] : "+str(shells["allshells"][found][5]))

		if "type" in str(shells["allshells"][found][6]):
			print("Register[EDX] : "+str(shells["allshells"][found][6]["type"]))
		else:
			print("Register[EDX] : "+str(shells["allshells"][found][6]))

		if "type" in str(shells["allshells"][found][7]):
			print("Register[ESI] : "+str(shells["allshells"][found][7]["type"]))
		else:
			print("Register[ESI] : "+str(shells["allshells"][found][7]))

		if "type" in shells["allshells"][found][8]:
			print("Register[EDI] : "+str(shells["allshells"][found][8]["type"]))
		else:
			print("Register[EDI] : "+str(shells["allshells"][found][8]))

		print("Definition : "+str(shells["allshells"][found][9])+":"+str(shells["allshells"][found][10]))
	else:
		print("[***] ERROR: Not found!!")


if __name__ == '__main__':
	main()
