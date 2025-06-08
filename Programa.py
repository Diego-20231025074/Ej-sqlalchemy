from flask import Flask, render_template



class Programa:
    def init(self):
        
        self .app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABSE_URI']="sqlite:///estudiantes.sqlite3"
        
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #inicializar el servidor 
        self.app. run(debug=True)
        
        
        def agregar(self):
            return render_template('nuevoEstudiantes.html')
        
        
  
   
miProgrma=Programa()   