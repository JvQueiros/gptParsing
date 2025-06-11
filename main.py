from fastapi import FastAPI
from task_controler import process_file_task
import model

app = FastAPI()

@app.post("/gptparsing")
async def parsing(obj: model.Item):
    
    form_id = obj.id
    content = obj.file

    if content:
        process_file_task.apply_async(args=[form_id, content])
        return {'message': 'Arquivo recebido. Em processamento...'}

@app.get("/hc")
async def healthCheck():
    return 200