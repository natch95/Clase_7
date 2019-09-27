from flask import Flask

app= Flask(__name__)
# conn=sqlite(./db)
# clases
@app.route('/')
def hello():
    return "Hola mundo"

if __name__=='__main__':
    app.run()