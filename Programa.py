from flask import Flask 



class Programa:
    def init(self):
        
        self .app=Flask(__name__)
        
        self.app.add_url_rule('/nuevo', view_func=self.agregar)
        
        #inicializar el servidor 
        self.app. run(debug=True)
        
        
        def agregar(self):
            return 
        
        
  
   
miProgrma=Programa()   