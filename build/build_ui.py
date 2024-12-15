import os
import json
from py_sas_studio_custom_steps import CustomStep

cs = CustomStep()

with open(os.path.join(os.getcwd(),"components.json"),"r") as f:
    js = json.load(f)

jsd = json.dumps(js)

cs["ui"]=jsd

cs.create_custom_step(custom_step_path=os.path.join(os.getcwd(),"..","LLM - Azure OpenAI Zero-Shot Prompting.step"))


