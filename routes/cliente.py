from flask import Blueprint, render_template, request
from database.models.cliente import Person

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
    clientes = Person.select()
    return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''insere o cliente no servidor'''

    data = request.json
    
    novo_cliente = Person.create(
        nome = data['nome'],
        email = data['email'],
    )

    return render_template('item_cliente.html', cliente= novo_cliente)

@cliente_route.route('/new')
def formulario_clientes():
    '''renderiza o formulario para cadastro do cliente'''
    return render_template('formulario_clientes.html')


@cliente_route.route('/<int:cliente_id>')
def obter_cliente(cliente_id):
    '''obter dados de um cliente'''

    # cliente = Person.get_by_id(cliente_id)
    cliente = Person.get(Person.id == cliente_id)

    return render_template('obter_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def formulario_edit(cliente_id):
    '''renderiza formulario para editar cliente'''

    cliente = Person.get_by_id(cliente_id)

    return render_template('formulario_clientes.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    '''atualiza os dados do cliente'''
    data = request.json    
    
    cliente = Person.get_by_id(cliente_id)
    cliente.nome = data['nome']
    cliente.email = data['email']
    cliente.save()
    
    return render_template('item_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''deleta os dados de um cliente'''
    cliente = Person.get_by_id(cliente_id)
    cliente.delete_instance()
    cliente.save()

    return {'deleted': 'ok'}