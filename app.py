from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html",titulo_pagina="Página inicial")
    
@app.route("/agenda")
def agenda():
    return render_template("agenda.html",titulo_pagina="Agenda")
    
@app.route("/agendamento")
def agendamento():
    return render_template("agendamento.html",titulo_pagina="Agendamento Online")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html",titulo_pagina="Contatos")

if __name__ == "__main__":
    app.run(debug=True)