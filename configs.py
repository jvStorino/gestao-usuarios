from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models.cliente import Person

def config_all(app):
    config_route(app)
    config_db()

def config_route(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def config_db():
    db.connect()
    db.create_tables([Person])