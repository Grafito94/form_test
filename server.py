from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "ser o no ser" #Clave secreta

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['email'] = request.form['email']

    # Nunca renderices una plantilla en una solicitud POST
    # En su lugar, redirigiremos a nuestra ruta de índice
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template("show.html", name_template = session['name'], email_template = session['email'])
if __name__ == "__main__":
    app.run(debug = True)

