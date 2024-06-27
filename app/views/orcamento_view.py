from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import orcamento_form
from app.models import orcamento_model
from app import db
@app.route("/cadorcamento",methods=["POST","GET"])
def cadastrar_orcamento():
      form = orcamento_form.OrcamemtoForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       orcamento = orcamento_model.Orcamento(nome=nome)
       try:
          #adicionar na sessão 
          db.session.add(orcamento)
          #salvar a sessão
          db.session.commit()
          if request.method == 'POST':
           return redirect(url_for('listar_equipamentos'))
       except:
         print("orcamento não cadastrado")
      return render_template("orcamento/form_orcamento.html",form=form)

