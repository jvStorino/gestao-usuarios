from flask import Flask
from configs import config_all

# inicialização
app = Flask(__name__)

# rotas
config_all(app)


# execução
if __name__ == "__main__":
    app.run()
