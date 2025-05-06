# Häufige Angriffsvektoren in der Praxis

## Phishing und Social Engineering

Bei phisching, Social Engineering usw. nutzt man Menschen als Angriffsvectoren. Menschen sind oft naiv und können leicht geteuscht werden. Das macht man sich dabei zu nutzen um an Informationen wie Passwörter oder ähnliches zu kommen.

## Web-basierte Angriffe
- **SQL Injection**: Manipulation von Datenbank-Abfragen
- **Cross-Site Scripting (XSS)**: Einschleusen von bösartigem JavaScript
- **CSRF**: Ausführen unerwünschter Aktionen im Namen des Benutzers

## Netzwerk-basierte Angriffe
- **Man-in-the-Middle**: Abhören/Manipulieren von Kommunikation
- **DDoS**: Überlasten von Servern/Diensten
- **Port Scanning**: Suche nach offenen Ports/Schwachstellen

## Physische Angriffe
- **USB-Drops**: Platzieren infizierter USB-Sticks
- **Shoulder Surfing**: Ausspähen von Passwörtern
- **Dumpster Diving**: Durchsuchen von Müll nach sensiblen Daten

# OWASP Top 10

### 1) Broken Access Control
- Umgehung von Authentifizierung und Autorisierung
- Horizontale und vertikale Privilegien-Eskalation
- Manipulation von URLs, um auf geschützte Ressourcen zuzugreifen
- Änderung von API-Anfragen zur Umgehung von Berechtigungen

### 2) Cryptographic Failures
- Verwendung schwacher oder veralteter Verschlüsselungsalgorithmen
- Übertragung sensibler Daten im Klartext
- Unsichere Speicherung von Passwörtern
- Verwendung von hartcodierten Schlüsseln

### 3) Injection
- SQL Injection: Einschleusen schädlicher Datenbankbefehle
- Command Injection: Ausführung von Systembefehlen
- LDAP Injection: Manipulation von Verzeichnisanfragen
- XPath Injection: Manipulation von XML-Abfragen

### 4) Insecure Design
- Fehlende Sicherheitskontrollen auf Architekturebene
- Unzureichende Validierung von Geschäftslogik
- Mangelnde Berücksichtigung von Sicherheitsanforderungen im Design
- Fehlendes "Security by Design"-Prinzip

### 5) Security Misconfiguration
- Standard-Passwörter und -Konten nicht geändert
- Unnötige Features und Dienste aktiviert
- Fehlende oder veraltete Sicherheitspatches
- Aussagekräftige Fehlermeldungen nach außen

### 6) Vulnerable & Outdated Components
- Verwendung veralteter Bibliotheken und Frameworks
- Fehlende Prozesse für Updates und Patches
- Unbekannte Abhängigkeiten in Anwendungen
- Nicht gepatchte bekannte Schwachstellen

### 7) Identification & Authentication Failures
- Schwache Passwort-Policies
- Fehlende oder schwache Multi-Faktor-Authentifizierung
- Unsichere Passwort-Wiederherstellung
- Session-Handling-Schwachstellen

### 8) Software & Data Integrity Failures
- Verwendung nicht vertrauenswürdiger Quellen
- Fehlende Integritätsprüfungen bei Updates
- Unsichere CI/CD-Pipelines
- Fehlende Code-Signing-Mechanismen

### 9) Security Logging & Monitoring Failures
- Fehlende oder unzureichende Logging-Mechanismen
- Keine Echtzeitüberwachung von Sicherheitsereignissen
- Fehlende Alarmierung bei Sicherheitsvorfällen
- Unzureichende Aufbewahrung von Logs

### 10) Server-Side Request Forgery (SSRF)
- Manipulation von Server-Anfragen durch Benutzer
- Zugriff auf interne Systeme über manipulierte URLs
- Umgehung von Netzwerk-Segmentierung
- Ausnutzung von Cloud-Metadaten-Endpunkten
