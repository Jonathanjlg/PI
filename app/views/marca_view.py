from app import app
from flask import render_template, redirect, url_for, request
from app.forms import marca_form
from app.models import marca_model
from app import db

@app.route("/cadmarca", methods=["POST", "GET"])
def cadastrar_marca():
    form = marca_form.MarcaForm()
    if form.validate_on_submit():
        nome = form.nome.data
        marca = marca_model.Marca(nome=nome)
        try:
            db.session.add(marca)
            db.session.commit()
            return redirect(url_for('listar_marcas'))  # Corrigido para listar_marcas
        except:
            print("Marca não cadastrada")
    return render_template("marca/form_marca.html", form=form, editar=False)

@app.route("/listarmarcas")  # Renomeado para listar_marcas
def listar_marcas():
    marcas = marca_model.Marca.query.all()
    return render_template("marca/lista_marca.html", marcas=marcas)

@app.route("/listarmarca/<int:id>")  # Renomeado para listar_marca_por_id
def listar_marca_por_id(id):
    marca = marca_model.Marca.query.filter_by(id=id).first()
    return render_template("marca/lista_marca_id.html", marca=marca)

@app.route("/editarmarca/<int:id>", methods=["POST", "GET"])
def editar_marca(id):
    marca = marca_model.Marca.query.filter_by(id=id).first()
    form = marca_form.MarcaForm(obj=marca)
    if form.validate_on_submit():
        nome = form.nome.data
        marca.nome = nome
        try:
            db.session.commit()
            return redirect(url_for("listar_marcas"))
        except:
            print("Erro ao editar marca")
    return render_template("marca/form_marca.html", form=form, editar=True)

@app.route("/removermarca/<int:id>", methods=["POST", "GET"])
def remover_marca(id):
    marca = marca_model.Marca.query.filter_by(id=id).first()
    if request.method == "POST":
        try:
            db.session.delete(marca)
            db.session.commit()
            return redirect(url_for("listar_marcas"))
        except:
            print("Erro ao deletar marca")
    return render_template("marca/remover_marca.html", marca=marca)
