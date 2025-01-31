import os
import json
import pandas

with open(os.path.join(os.getcwd(),"components.json"),"r") as f:
    js = json.load(f)
    
# _getattr_
# preload with None

var_dict={"variable":[], "description":[], "type":[],"value":[]}

def parse_object(page_object, var_dict):
    if "id" in page_object:
        var_dict["variable"].append(page_object["id"])
    if "label" in page_object:
        var_dict["description"].append(page_object["label"])
    else:
        var_dict["description"].append(None)
    if "type" in page_object:
        var_dict["type"].append(page_object["type"])
    else:
        var_dict["type"].append(None)
    if "text" in page_object:
        var_dict["value"].append(page_object["text"].strip().strip("\r").strip("\t").replace("\n", ""))
    else:
        var_dict["value"].append(None)
    if "children" in page_object:
        for child in page_object["children"]:
            parse_object(child, var_dict)
    
for page in js["pages"]:
    parse_object(page, var_dict)

pandas.DataFrame(var_dict).to_markdown(os.path.join(os.getcwd(),"List_of_Variables.md"))
pandas.DataFrame(var_dict).to_csv(os.path.join(os.getcwd(),"List_of_Variables.tsv"), sep="\t")

