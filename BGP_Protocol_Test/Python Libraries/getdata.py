import json

def get_data():
   	with open('Topology_file.json') as data_file:    
 		data = json.load(data_file)
   	return data
