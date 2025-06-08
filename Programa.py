from flask import Flask, render_template
from db import db
from Estudiante import Estudiante



class Programa:
    def init(self):
        
        self .app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///estudiantes.sqlite3"
        
        db.init_app(self.app)
        self.app.add_url_rule('/nuevo', view_func=self.buscarTodos)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])
        
        #inicializar el servidor 
        with self.app.app_context():
            db.create_all()
        
        self.app. run(debug=True)
        
        
        def buscarTodos(self):
            return "TO DO: "
        
        
        def agregar(self):
            
            # verficar si debe enviar los datos o procesar los datos
            
            if request.method=="POST":
                
                #Crear un objeto de la clase estudiante con los valores del formulario 
                
                nombre=request.form['nombre']
                email=request.form['email']
                codigo=request.form['codigo.']
                miEstudiante=Estudiante(nombre, email, codigo)
                
                #guardar el objeto en la db
                
                db.session.add(miEstudiante)
                db.session.commit()
            
            
            
            
            return render_template('nuevoEstudiantes.html')
        
        
  
   
miProgrma=Programa()   