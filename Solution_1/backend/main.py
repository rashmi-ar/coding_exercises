from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import plantuml

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
model_name = "./Solution_1/backend/trained_sol1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

class Scenario(BaseModel):
    description: str

def clean_plantuml_code(code: str) -> str:
    lines = code.split("\n")
    valid_lines = [line for line in lines if "->" in line]
    return "\n".join(valid_lines)

@app.post("/generate_plantuml/")
def generate_plantuml(scenario: Scenario):
    inputs = tokenizer.encode(scenario.description, return_tensors="pt")
    outputs = model.generate(inputs, max_length=inputs.shape[1] + 50, num_return_sequences=1, max_new_tokens=50)

    plantuml_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

    plantuml_code = clean_plantuml_code(plantuml_code)
    plantuml_code = f"@startuml\n{plantuml_code}\n@enduml"

    # Get url
    plantuml_img = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/')
    img_url = plantuml_img.get_url(plantuml_code)
    
    return {"plantuml_code": plantuml_code, "image_url": img_url}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, max_request_size=100 * 1024 * 1024)  # Set max request size to 100MB