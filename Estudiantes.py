from db import db 

class Estudiante(db.Model):
    
    #Nombre de la tabla 
    __tablename__="estudiante"
    
    # conjunto de atributos que vana ser los campos de la tabla 
    
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))