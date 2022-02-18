from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from src.model import generate_iam_policy

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    result = "Type a ARN"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, arn: str = Form(...), type: str = Form(...)):
    result = generate_iam_policy(arn, type)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

