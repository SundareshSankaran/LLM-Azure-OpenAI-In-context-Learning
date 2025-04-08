import os
import json
import pandas

from datetime import datetime

modifiedBy="Sundaresh Sankaran"

from py_sas_studio_custom_steps import CustomStep

createdBy="Sundaresh Sankaran and Crystal Baker"

name= "LLM - Azure OpenAI In-context Learning"


cs = CustomStep()

cs.load_step_file(custom_step_file=os.path.join(os.getcwd(),"..",f"{name}.step"))

js=json.loads(cs.__dict__["ui"])

# Write a Python function to compare two long strings on their values but ignore spaces in between
def compare_strings_ignore_spaces(str1, str2):
    str1_clean = ''.join(str1.split())
    str2_clean = ''.join(str2.split())
    return str1_clean == str2_clean


# Given a nested json , create a function which provides all objects nested wihin layers of the 


# Create a Python dict from a tsv file
def tsv_to_dict(tsv_file_path):
    df = pandas.read_csv(tsv_file_path, sep='\t')
    # Change all cases of None or NaN in df["value"] to empty space
    df['value'] = df['value'].fillna('')
    df['description'] = df['description'].fillna('')
    df.loc[df['type']== 'page', "value"] = df["description"]
    df.loc[df['type']== 'section', "value"] = df["description"]
    df.loc[df['type']== 'inputtable', "value"] = df["description"]
    df.loc[df['type']== 'outputtable', "value"] = df["description"]
    df.loc[df['type']== 'columnselector', "value"] = df["description"]
    df.loc[df['type']== 'textarea', "value"] = df["description"]
    df.loc[df['type']== 'numstepper', "value"] = df["description"]
    df.loc[df['type']== 'textfield', "value"] = df["description"]
    df.loc[df['type']== 'path', "value"] = df["description"]
    return df.to_dict(orient='records')

# Create a Python dict from a tsv file
tsv_file_path = os.path.join(os.getcwd(), "List_of_Variables.tsv")



component_dict = tsv_to_dict(tsv_file_path)

def traverse_nested_json(js):
    if isinstance(js,list):
        for obj in js:
            for key in obj:
                if "id" in key:
                    yield obj
                else:
                    yield from traverse_nested_json(obj[key])



        

# Given component_dict and js, search for all instances of the key "variable" in component_dict 
# within all "id" fields in js.  Note that "id" may be nested.  

# In case the "value" corresponding to "variable" differs from the "label" field corresponding to the 
# "id" field of js, print out the cases where these are different.

def find_nested_ids(js, key="id"):
    if isinstance(js, dict):
        for k, v in js.items():
            if k == key:
                yield v
            else:
                yield from find_nested_ids(v, key)
    elif isinstance(js, list):
        for item in js:
            yield from find_nested_ids(item, key)

for component in component_dict:
    variable = component.get("variable")
    value = component.get("value")
    print(f"Searching for value in variable {variable}")
    for id_value in find_nested_ids(js):
        if id_value == variable:
            for item in traverse_nested_json(js["pages"]):
                if item["id"]==id_value:
                    if "label" in item:
                        label = item["label"]
                    elif "text" in item:
                        label = item["text"]
                    else:
                        label=""
                    if label and compare_strings_ignore_spaces(label,value)==True:
                        print(f"No change detected for {variable}")
                    if label and compare_strings_ignore_spaces(label,value)==False:
                        print("Change detected, updating")
                        if "label" in item:
                            item["label"]=value
                        elif "text" in item:
                            item["text"] = value
                        print("Updated")


# Update the CustomStep object with the new ui field
cs.__dict__["ui"] = json.dumps(js)

cs["modifiedBy"] = modifiedBy
cs["modifiedTimeStamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

cs.create_custom_step(custom_step_path= os.path.join(os.getcwd(),"..",f"{name}.step"))


# Replace the existing components.json file with js
components_json_path = os.path.join(os.getcwd(), "components.json")
with open(components_json_path, 'w') as f:
    json.dump(js, f, indent=4)
components_json_path = os.path.join(os.getcwd(),"..","extras", f"{name}.json")
with open(components_json_path, 'w') as f:
    json.dump(js, f, indent=4)