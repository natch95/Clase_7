# from flask import Flask

# app= Flask(__name__)
# # conn=sqlite(./db)
# # clases
# @app.route('/')
# def hello():
#     return "Hola mundo"

# if __name__=='__main__':
#     app.run()

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1=person("Jhon",23)
print(p1.name)
print(p1.age)

del p1