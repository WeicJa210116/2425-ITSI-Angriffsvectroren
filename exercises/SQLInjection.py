import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)


# Datenbankverbindung und Setup
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


with get_db() as conn:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
        """
    )
    # Nur einmal einfügen, falls Tabelle leer ist
    if not conn.execute("SELECT * FROM users WHERE username='admin'").fetchone():
        conn.execute("INSERT INTO users VALUES ('admin', '  ')")
        conn.commit()

# HTML-Formular
form_html = """
<!doctype html>
<title>SQL Injection Demo</title>
<style>
body {
    background: #f4f4f4;
    font-family: Arial, sans-serif;
}
h2 {
    text-align: center;
    color: #333;
}
form {
    background: #fff;
    padding: 2em 2em 1em 2em;
    margin: 2em auto;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    max-width: 350px;
}
input[type="text"], input[type="password"] {
    width: 95%;
    padding: 0.5em;
    margin: 0.5em 0 1em 0;
    border: 1px solid #bbb;
    border-radius: 4px;
    font-size: 1em;
}
input[type="submit"] {
    background: #0078d7;
    color: #fff;
    border: none;
    padding: 0.7em 1.5em;
    border-radius: 4px;
    font-size: 1em;
    cursor: pointer;
    transition: background 0.2s;
}
input[type="submit"]:hover {
    background: #005fa3;
}
p {
    text-align: center;
    font-size: 1.1em;
}
b {
    color: #0078d7;
}
</style>
<h2>Login</h2>
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
{% if query %}
<p><b>Ausgeführte SQL-Abfrage:</b><br>{{ query }}</p>
{% endif %}
{% if result is not none %}
<p><b>{{ result }}</b></p>
{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def login():
    query = None
    result = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        # Unsichere SQL-Abfrage (nur zu Demo-Zwecken!)
        query = (
            f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        )
        try:
            with get_db() as conn:
                cur = conn.execute(query)
                user = cur.fetchone()
                if user:
                    result = "Login erfolgreich!"
                else:
                    result = "Login fehlgeschlagen!"
        except Exception as e:
            result = f"Fehler: {e}"
    return render_template_string(form_html, query=query, result=result)


if __name__ == "__main__":
    app.run(debug=True)
