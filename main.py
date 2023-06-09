# uvicorn main:app --host 0.0.0.0 --port 10000
from pydantic import BaseModel
# import pinecone
from fastapi import FastAPI
from typing import Optional
import os, json
 

app = FastAPI()


# Define a Pydantic model that will be used to validate the incoming JSON payload
class HF_Convo_Item(BaseModel):
    prompt: str
    chat_history: list
    script_name: str
    page_number: int
        
@app.post("/conversation/")
async def read_item(payload: HF_Convo_Item):
 
 
# "chat_history":[["this is my question","this is my answer"]], "script_name":"hf_intro", "page_number":1}' https://hf-confo-test.onrender.com/conversation/
  
  
 
#     a_list = [1,2,3]
     
#     everything = {"a_list": a_list, "a_dict": a_dict}
#     json.dumps(everything)
  
     
    # Access individual fields of the JSON payload
    prompt = payload.prompt
    print(prompt)
    
    chat_history = payload.chat_history
    chat_history = [tuple(inner_list) for inner_list in chat_history]
    print(chat_history)
      
    script = payload.script_name
    print(script)
      
    page = payload.page_number
    print(page)
    
    result = 'the resulto'
    chat_history = [("this is my question","this is my answer")]
    
    # Repack the payload
    payload = {
        "response": result,
        "chat_history": chat_history
        
    }

    return payload
  
