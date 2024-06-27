from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import cliente_form
from app.models import cliente_model
from app import db

@app.route("/cadcliente", methods=["POST", "GET"])
def cadastrar_cliente():
    form = cliente_form.ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
        cpf = form.cpf.data
        telefone = form.telefone.data
        email = form.email.data
        
        cliente = cliente_model.Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
        
        try:
            db.session.add(cliente)
            db.session.commit()
            if request.method == 'POST':
             return redirect(url_for('listar_clientes'))  # Redireciona para a lista de clientes após o cadastro
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {str(e)}")
    
    return render_template("cliente/form_cliente.html", form=form, editar=False)

@app.route("/listarclientes")
def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return render_template("cliente/lista_cliente.html", clientes=clientes)

@app.route("/liscliente/<int:id>")
def listar_cliente(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()  # Consulta o cliente pelo ID
    return render_template("cliente/lista_cliente_id.html", cliente=cliente)

@app.route("/editarcliente/<int:id>", methods=["POST", "GET"])
def editar_cliente(id):  # Renomear para editar_cliente
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()   # Buscar cliente pelo ID
    form = cliente_form.ClienteForm(obj=cliente)  # Usar o formulário do cliente
    
    if form.validate_on_submit():
        cliente.nome = form.nome.data
        cliente.cpf = form.cpf.data
        cliente.telefone = form.telefone.data
        cliente.email = form.email.data
        
        try:
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except Exception as e:
            print(f"Erro ao editar cliente: {str(e)}")
    
    return render_template("cliente/form_cliente.html", form=form, editar=True)

@app.route("/removercliente/<int:id>", methods=["POST", "GET"])
def remover_cliente(id):  # Renomear para remover_cliente
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()   # Buscar cliente pelo ID
    
    if request.method == "POST":
        try:
            db.session.delete(cliente)
            db.session.commit()
            return redirect(url_for("listar_clientes"))
        except Exception as e:
            print(f"Erro ao remover cliente: {str(e)}")
    
    return render_template("cliente/remover_cliente.html", cliente=cliente)
