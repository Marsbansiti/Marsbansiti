'''

JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.

JSON is built on two structures:

A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.

An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

JSON is a language-independent data format. It was derived from JavaScript, but many modern programming languages include code to generate and parse JSON-format data. It is a very common data format with a diverse range of applications.

The text in JSON is done through quoted string which contains the values in key-value mappings within { }. It is similar to the dictionary in Python.

Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script.

'''
import json

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

#------------------------- Writing JSON to a File ----------------------------
'''
json.dump() method can be used for writing to JSON file.

Syntax: json.dump(dict, file_pointer)

Parameters:

dictionary – name of the dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.

'''

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)


'''
json.dumps() that helps in converting a dictionary to a JSON object.

It takes two parameters:

dictionary – name of the dictionary which should be converted to JSON object.
indent – defines the number of units for indentation
'''

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

print(json_object)

#------------------------Reading JSON to a File---------------------------------
  '''
  Using json.load()
The JSON package has json.load() function that loads the json content from a json file into a dictionary.

It takes one parameter:

File pointer : A file pointer that points to a JSON file.
'''


# Opening JSON file 
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object)) 

