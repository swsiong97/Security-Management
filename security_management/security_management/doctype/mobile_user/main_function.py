

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json


# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://re-444ac.firebaseio.com'
})

class myDict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

def syncFirebase() :
 	print ("syncing ...")



def getFromFirebase(ref):
	ref = db.reference(ref)
	print(ref.get())

def saveToFirebase(ref, keyArray, valueArray):
	
	ref = db.reference(ref)
	data = myDict()
	key = value = 0
	if (len(keyArray) == len(valueArray)):
		
		while (key < len(keyArray) and value < len(valueArray)):
			data.add(keyArray[key],valueArray[value])
			key+=1
			value+=1
			
	
	ref.push().set(data)
	print('Data saved')

syncFirebase()
getFromFirebase('user')

key = ['name','email','user_type']
value = ['Ramzguard','ramzguard@gmail.com', 'resident']
saveToFirebase('user',key,value)
