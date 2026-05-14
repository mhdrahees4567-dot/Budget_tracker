import json

file_name="data.txt"

def load_data():
    try:
        with open(file_name,'r') as file:
            return json.load(file)
        
    except :
        return {"income":0,"expenses":[]}
    

def save_data(data):
    with open(file_name,'w') as file:
        
        json.dump(data,file,indent=4)