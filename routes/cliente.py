from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

'''
Rota de Clientes

    /clientes/ (GET) - listar os clientes
    /clientes/ (POST) - insere o cliente no servidor
    /clientes/new (GET) - renderiza o formulario para cadastro do cliente
    /clientes/<id> (GET) - obter dados de um cliente
    /clientes/<id>/edit (GET) - renderiza formulario para editar cliente
    /clientes/<id>/update (PUT) - atualiza os dados do cliente
    /clientes/<id>/delete (DELETE) - deleta os dados de um cliente 
'''

@cliente_route.route('/')
def lista_clientes():
    '''listar os clientes'''
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''insere o cliente no servidor'''

    data = request.json
    
    novo_usuario = {
        'id': len(CLIENTES)+1,
        'nome': data['nome'],
        'email': data['email']
    }
    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente= novo_usuario)


@cliente_route.route('/new')
def formulario_clientes():
    '''renderiza o formulario para cadastro do cliente'''
    return render_template('formulario_clientes.html')


@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    '''obter dados de um cliente'''

    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('obter_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def formulario_edit(cliente_id):
    '''renderiza formulario para editar cliente'''
    cliente= None

    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c

    return render_template('formulario_clientes.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    '''atualiza os dados do cliente'''
    cliente = None

    data = request.json

    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            cliente = c
    
    return render_template('item_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''deleta os dados de um cliente'''
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'deleted': 'ok'}