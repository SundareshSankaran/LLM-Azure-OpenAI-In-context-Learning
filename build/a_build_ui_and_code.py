import os
import json
from py_sas_studio_custom_steps import CustomStep

cs = CustomStep(type="code")

with open(os.path.join(os.getcwd(),"components.json"),"r") as f:
    js = json.load(f)

jsd = json.dumps(js)

cs["ui"]=jsd

with open(os.path.join(os.getcwd(),"..","extras","LLM - Azure OpenAI Zero-Shot Prompting.sas")) as sas_f:
    sas_code_obj={"SAS":sas_f.read()}

cs["templates"]=sas_code_obj

cs.create_custom_step(custom_step_path=os.path.join(os.getcwd(),"..","LLM - Azure OpenAI Zero-Shot Prompting.step"))


