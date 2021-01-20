import uvicorn
from fastapi import FastAPI



from pydantic import BaseModel


class mat(BaseModel):
    num1 : float
    num2 : float 
    operation : str
    
    
app = FastAPI()


@app.get("/")
def home_page():
    return ("Hello World")


    #return templating('index.html')
@app.get('/{name}')
def get_name(name:str):
    return {'Welcome': f'{name}'}



@app.post('/predict')  # This will be called from UI
def math_operation(data:mat):
    
    data = data.dict()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']
    
    if(operation=='add'):
        r=num1+num2
        result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
    if (operation == 'subtract'):
        r = num1 - num2
        result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'multiply'):
        r = num1 * num2
        result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
    if (operation == 'divide'):
        r = num1 / num2
        result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
    return  result
    

if __name__ == '__main__':
    uvicorn.run(app,host = '127.0.0.1', port= 8000)