#Import json file from libary
import json

#Creating a json dictionary

data1 = {
    
    'name': 'John Doe',
    'age': 30,
    'city': 'New York, NY',
    'interests':['Traveling','Fotball','Gold','Running','Videogames','History'],
    'is_student': False

}


#Creating a json and writing the python object contents to the json.
with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)

    print("Data has been written to data1.json")

#Reading the json data from the json file created
with open('data1.json', 'r') as json_file:

    #Create an object called loaded_data. Load the json file into the argument parameter.
    loaded_data = json.load(json_file)

    print("Successfully able to read data1.json")
    print(loaded_data)



#Altering the JSON Object.
loaded_data['age'] = 34 #<--ints
loaded_data['interests'].append('Secret Hobby')

#Rewrite the changes to the json file.
with open('data1.json','w') as json_file:

    json.dump(loaded_data,json_file,indent=4)

    print("Data has been re-written to data1.json")