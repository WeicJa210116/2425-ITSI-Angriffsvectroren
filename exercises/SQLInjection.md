// ...existing code...

## 3. SQL-Injection Übung

### Szenario
Eine Webseite verwendet folgende unsichere SQL-Abfrage für die Benutzeranmeldung:

```sql
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
```

Beispiel-Login-Formular:
```html
<form method="post" action="login.php">
    Benutzername: <input type="text" name="username">
    Passwort: <input type="password" name="password">
    <input type="submit" value="Login">
</form>
```

### Aufgaben

1. Analysieren Sie folgende Eingaben und deren Auswirkungen:
   ```sql
   Username: admin' --
   Password: egal
   ```
   ```sql
   Username: ' OR '1'='1
   Password: ' OR '1'='1
   ```

2. Erklären Sie:
   - Wie die originale SQL-Abfrage manipuliert wird
   - Warum der Angriff funktioniert
   - Welche Daten potenziell gefährdet sind

3. Entwickeln Sie sichere Alternativen:
   - Prepared Statements
   - Input Validation
   - Parametrisierte Abfragen

4. Implementieren Sie grundlegende Schutzmaßnahmen:
   - Eingabevalidierung
   - Escape-Funktionen
   - Fehlerbehandlung ohne Details