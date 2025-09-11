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
