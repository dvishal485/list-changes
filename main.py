import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {
        'api_name': 'list-changes',
        'repository': 'https://github.com/dvishal485/list-changes',
        'author': 'dvisha485@gmail.com',
        'author_github': 'https://github.com/dvishal485',
        'description': 'Returns the newly added entries in a list',
        'usage': 'https://github.com/dvishal485/list-changes#usage'
    }


@app.post('/api')
async def getAPI(request: Request):
    data = await request.json()
    newList = json.loads(unquote(data["new"]))
    oldList = json.loads(unquote(data["old"]))
    return [x for x in newList if x not in oldList]
