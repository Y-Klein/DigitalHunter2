from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return {'msg':'😊'}

@app.get('/q1')
def q1():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q2')
def q2():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q3')
def q3():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q4')
def q4():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q5')
def q5():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q6')
def q6():
    return {'msg':'The place is under construction! Please be patient.'}

@app.get('/q7')
def q7():
    return {'msg':'The place is under construction! Please be patient.'}


if __name__=='__main__':
    uvicorn.run(app)