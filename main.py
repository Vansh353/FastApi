#pip install fastapi uvicorn

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'data':{'name':'Rahul'}}
@app.get('/about')
def about():
    return {'data':'about page'}
# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
#hello