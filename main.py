from fastapi import FastAPI
import uvicorn
import dal

app = FastAPI()

@app.get('/')
def root():
    return {'msg':'😊'}

@app.get('/q1')
def q1():
    return dal.q1()

@app.get('/q2')
def q2():
    return dal.q2()

@app.get('/q3')
def q3():
    return dal.q3()

@app.get('/q4')
def q4():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q5')
def q5(entity_id):
    dal.q5(entity_id)

@app.get('/q6')
def q6():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q7')
def q7():
    return {'msg':'The place is under construction! Please be patient.'}


if __name__=='__main__':
    uvicorn.run(app)