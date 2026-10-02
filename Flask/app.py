from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal: renderiza la interfaz interactiva index.html
@app.route("/")
def inicio():
    return render_template("index.html")

# Ruta dinámica para validar edad y voto (conecta con info2.html)
@app.route("/info/<name>/<age>")
def info(name, age):
    return render_template("info2.html", nameHtml=name, ageHtml=age)

# Ruta dinámica para el saludo simple (conecta con user2.html)
@app.route("/user/<name>")
def usuario(name):
    return render_template("user2.html", nameHtml=name)

if __name__ == "__main__":
    app.run(debug=True)