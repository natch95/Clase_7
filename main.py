# from flask import Flask

# app= Flask(__name__)
# # conn=sqlite(./db)
# # clases
# @app.route('/')
# def hello():
#     return "Hola mundo"

# if __name__=='__main__':
#     app.run()

# ********* Clase que agregar objeto persona, despliega y luego la elimina *********
# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1=person("Jhon",23)
# print(p1.name)
# print(p1.age)

# del p1

# ********* Ejercicio con iterador *********
# class nose:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a +=1
#         return x
# myclass=nose()
# myiter=iter(myclass)
# print(next(myiter))