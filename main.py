from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "segredo123"  # necessário para usar session

USER = "erick"
PASS = "123"


# rota inicial
@app.route("/", methods=["GET"])
def homepage():
    return redirect(url_for("login"))


# rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        usuario = request.form.get("Usuario", "").strip()
        senha = request.form.get("Senha", "").strip()

        if usuario == USER and senha == PASS:
            session["user"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválida"

    return render_template("login.html", erro=erro)


# dashboard
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", user=session["user"])


if __name__ == "__main__":
    app.run(debug=True, port=5152)