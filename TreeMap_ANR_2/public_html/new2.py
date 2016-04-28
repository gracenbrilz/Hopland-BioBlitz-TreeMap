import urllib2
import json
import operator
import requests
from pprint import pprint
import re

site = "https://www.inaturalist.org"

def main():
	initial_json = []


	pageNum = 1
	print pageNum

	for pageNum in range(0, 200):
		print "----------This is the page number we are on!!!! %d" % (pageNum)


		# Get project data
		
		observations = requests.get(site+'/observations/project/549.json?page='+str(pageNum))
		pageNum+=1
		data = observations.json()
		flag = 0
		for d in data:
			for attr,value in d.iteritems():
				if attr == 'taxon':
					ancestry = list(reversed(list(str(value['ancestry']).split('/'))))


################     INSECTS      #######################

					# Beetles
					if '47208' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								print "-------again"
								print value['name']
								break

						if flag == 0:
							print "-------first"
							print value['name']
							print value['id']
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Beetles", "value":1})
							break



					# Moths & Butterflies
					if '47157' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Moths & Butterflies", "value":1})
							break


					# Flies
					if '7822' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Flies", "value":1})
							break



					# True Bugs
					if '47744' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"True Bugs", "value":1})
							break

					# Crickets & Grasshoppers
					if '47651' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Crickets & Grasshoppers", "value":1})
							break

																					

					# Ants, Bees, Wasps
					elif '47201' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Ants, Bees & Wasps", "value":1})
							break



					# Dragonflies & Mayflies
					elif '47792' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Dragonflies & Mayflies", "value":1})
							break

##### All Other Insects

					elif '47158' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Insects", "group":"Other Insects", "value":1})
							break



################     OTHER ARTHROPODS     #######################


					# Spiders
					elif '47118' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Spiders, & other Arthropods", "group":"Spiders", "value":1})
							break



					# Mites & Ticks
					elif '52788' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Spiders, & other Arthropods", "group":"Mites & Ticks", "value":1})
							break


##### All Other Arachnids

					elif '47119' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Spiders, & other Arthropods", "group":"Other Arachnids", "value":1})
							break


## All Other Arthropods #####

					elif '47120' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Spiders, & other Arthropods", "group":"Other Arthropods", "value":1})
							break
														



################     BIRDS     #######################

					# Ducks, Geese & relatives
					elif '6888' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Ducks, Geese & relatives", "value":1})
							break

					# Fowl & Quail
					elif '573' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Fowl & Quail", "value":1})
							break



					# Perching Birds
					elif '7251' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Perching Birds", "value":1})
							break


					# Owls
					elif '19350' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Owls", "value":1})
							break


################## Falcons, Eagles, & Buzzards  LOOKS FOR  67570 --OR-- 71261 IN ANSESTRY

					elif '67570' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Falcons, Eagles & Buzzards", "value":1})
							break

					elif '71261' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Falcons, Eagles & Buzzards", "value":1})
							break

##OTHER BIRDS

					elif '3' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Birds", "group":"Other Birds", "value":1})
							break




################ MAMMALS ####################

					#Rabbits, & Hares
					elif '43094' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Mammals", "group":"Rabbits, & Hares", "value":1})
							break

					#Bats
					elif '40268' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Mammals", "group":"Bats", "value":1})
							break



					#Pigs & Deer
					elif '152870' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Mammals", "group":"Pigs & Deer", "value":1}) 
							break
							
					#Rodents
					elif '43698' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Mammals", "group":"Rodents", "value":1}) 
							break



##### Other Mammals
					elif '40151' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Mammals", "group":"Other Mammals", "value":1}) 
							break


######################### REPTILES ###########################

					#Lizards
					elif '85552' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Reptiles", "group":"Lizards", "value":1}) 
							break

					#Snakes
					elif '85553' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Reptiles", "group":"Snakes", "value":1}) 
							break


					#Turtles & Tortoises
					elif '39532' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Reptiles", "group":"Turtles & Tortoises", "value":1}) 
							break

					#Other Reptiles
					elif '26036' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Reptiles", "group":"Other Reptiles", "value":1}) 
							break


######################### AMPHIBIANS ###########################

					#Frogs & Toads
					elif '20979' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Amphibians", "group":"Frogs & Toads", "value":1}) 
							break
							
					#Salamanders
					elif '26718' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Amphibians", "group":"Salamanders", "value":1}) 
							break

					#Other Amphibians
					elif '20978' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Animals", "subregion":"Amphibians", "group":"Other Amphibians", "value":1}) 
							break



######################### VASCULAR PLANTS ###########################

					#Ferns & Horsetails
					elif '311266' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Ferns & Horsetails", "value":1}) 
							break

					#Conifers
					elif '136329' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Conifers", "value":1}) 
							break


					#Bay laurel & Ginger
					elif '47124' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Bay laurel & Ginger", "value":1}) 
							break


					#Coontails
					elif '60998' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Coontails", "value":1}) 
							break

					#Grasses & related flowering plants
					elif '47163' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Grasses & related flowering plants", "value":1})
							break 

					#Other vascular plants
					elif '211194' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Vascular Plants", "group":"Other Vascular Plants", "value":1}) 
							break


######################### NON-VASCULAR PLANTS ###########################

					#Mosses, Hornworts & Liverworts
					elif '311249' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Non-Vascular Plants", "group":"Mosses, Hornworts & Liverworts", "value":1}) 
							break

					#Algae -- looks up 311313, 50863, or 57774
					elif '311313' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Non-Vascular Plants", "group":"Algae", "value":1}) 
							break

					elif '50863' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Non-Vascular Plants", "group":"Algae", "value":1}) 
							break
					 
					elif '57774' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"Non-Vascular Plants", "group":"Algae", "value":1}) 
							break





######## All other plants
					elif '47126' in ancestry:
						for k in range(len(initial_json)):
							flag = 0
							if initial_json[k]["key"] == value['name']:
								flag = 1
								initial_json[k]["value"] += 1
								break

						if flag == 0:    
							initial_json.append({"key":value['name'], "region":"Plants", "subregion":"All Other Plants", "group":"Other Plants", "value":1})
							break 



		# print (output)
		with open("countries.json","w") as handle:
			json.dump(initial_json,handle)

if __name__ == '__main__':
		main()