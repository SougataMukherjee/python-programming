from fastapi import FastAPI, Request,Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

app=FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/index/',response_class=HTMLResponse)
def index(request:Request, hx_request: Optional[str] = Header(None)):
    films = [
        {'name': 'Sam ', 'director': 'Sougata'},
        {'name': 'Rupai', 'director': 'Sougata'},
        {'name': 'Rik', 'director': 'Sougata'},
    ]
    context={'request':request,'films':films}
    if hx_request:
        return templates.TemplateResponse("partials/table.html", context)
    return templates.TemplateResponse("index.html",context)

#start dev server cli run with install pip install "fastapi[standard]" and( fastapi dev main.py)
# if __name__=='__main__':
#     import uvicorn
#     uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)