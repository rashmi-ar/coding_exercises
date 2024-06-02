from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from urllib.parse import quote

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load the model and tokenizer
model_name = "./Solution_2/backend/trained_sol2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

class Scenario(BaseModel):
    description: str

def simplify_description(description):
    use_case_name = description.split("Use Case Name:")[1].split("Use Case ID:")[0].strip()
    actors = description.split("Use Case Actors:")[1].split("Use Case Triggers:")[0].strip().split("\n")
    actors = [actor.strip('- ') for actor in actors]
    flow = description.split("Use Case Flow:")[1].split("Exceptions:")[0].strip().split("\n")
    flow = [step.strip() for step in flow]

    simplified_description = {
        "use_case_name": use_case_name,
        "actors": actors,
        "flow": flow
    }
    
    return simplified_description

@app.post("/generate_plantuml/")
def generate_plantuml(scenario: Scenario):
    inputs = tokenizer.encode(scenario.description, return_tensors="pt")
    outputs = model.generate(inputs, max_length=inputs.shape[1] + 50, num_return_sequences=1, max_new_tokens=50)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    simplified_description = simplify_description(text)

    use_case_name = simplified_description['use_case_name']
    actors = simplified_description['actors']
    flow = simplified_description['flow']
    
    plantuml_code = "@startuml\n"
    
    for actor in actors:
        plantuml_code += f"actor {actor}\n"
    
    plantuml_code += f"{actors[0]} --> ({use_case_name})\n"
    for step in flow:
        matched_actor = None
        for actor in actors:
            if step.lower().startswith(actor.lower()):
                matched_actor = actor
                break
        
        if matched_actor:
            plantuml_code += f"{matched_actor} --> ({step})\n"
        else:
            plantuml_code += f"{actors[0]} --> ({step})\n"
    
    plantuml_code += "@enduml"

    base_url = "http://www.plantuml.com/plantuml/img/"
    encoded_code = quote(plantuml_code)
    img_url = base_url + encoded_code
    
    return {"plantuml_code": plantuml_code, "image_url": img_url}