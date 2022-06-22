#from src import app
from src.__init__ import app
from src.config import default_config, csrf
from src.routes import index, login



def status_401(error):
    return login

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


# Ejecución de la App

if __name__ == '__main__':
    app.config.from_object(default_config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(debug=True)
    index