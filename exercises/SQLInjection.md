# SQL-Injection Übung

## Szenario

Eine Webseite verwendet folgende unsichere SQL-Abfrage für die Benutzeranmeldung:

Das ist der Basis-Code der verwendet werden soll:
[python Code](./SQLInjection.py)
(Sie können auch ihren Eigenen Code schreiben in einer Sparacher Ihrer Wahl)

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

   und überlegen Sie sich andere Möglichkeiten den Code zu manipulieren

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