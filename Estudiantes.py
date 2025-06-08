from db import db 

class Estudiante(db.Model):
    
    #Nombre de la tabla 
    __tablename__="estudiante"
    
    # conjunto de atributos que vana ser los campos de la tabla 
    # Llave primaria
    id=db.Colunm(db.integer, primary_key=True)
    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))
    
    #Metodo constructor para mapear datos a los cmpos definidos 
    
    def __init__(self, nombre, email, codigo):
        
        self.nombre=nombre
        self.email=email
        self.codigo=codigo
     