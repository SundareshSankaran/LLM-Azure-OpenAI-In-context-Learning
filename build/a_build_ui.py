import os
import json
from py_sas_studio_custom_steps import CustomStep
from datetime import datetime

createdBy="Sundaresh Sankaran and Crystal Baker"
modifiedBy="Sundaresh Sankaran"
name= "LLM - Azure OpenAI In-context Learning"

cs = CustomStep(type="code",createdBy=createdBy, 
              name=name,
              displayName=name,
              creationTimeStamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
              modifiedBy=modifiedBy,
              modifiedTimeStamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

with open(os.path.join(os.getcwd(),"components.json"),"r") as f:
    js = json.load(f)

with open(os.path.join(os.getcwd(),"..","extras",f"{name}.json"),"r") as f:
    js = json.load(f)

jsd = json.dumps(js)

cs["ui"]=jsd

if os.path.isfile(os.path.join(os.getcwd(),"..", "extras", f"{name}.sas")):
    cs.attach_sas_program(sas_file=os.path.join(os.getcwd(),"..","extras", f"{name}.sas"))


cs.create_custom_step(os.path.join(os.getcwd(),"..",name + ".step"))
