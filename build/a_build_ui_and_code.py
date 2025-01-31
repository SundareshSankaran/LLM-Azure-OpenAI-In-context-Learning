import os
import json
from py_sas_studio_custom_steps import CustomStep
from datetime import datetime

createdBy="Sundaresh Sankaran and Crystal Baker"
modifiedBy="Crystal Baker"
name= "LLM - Azure OpenAI In-context Learning"

cs = CustomStep(type="code",createdBy=createdBy, 
              name=name,
              displayName=name,
              creationTimeStamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
              modifiedBy="Crystal Baker",
              modifiedTimeStamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"))

with open(os.path.join(os.getcwd(),"components.json"),"r") as f:
    js = json.load(f)

jsd = json.dumps(js)

cs["ui"]=jsd

# cs.create_custom_step(custom_step_path=os.path.join(os.getcwd(),"..","LLM - Azure OpenAI Zero-Shot Prompting.step"))
cs.create_custom_step(os.path.join(os.getcwd(),"..",name + ".step"))