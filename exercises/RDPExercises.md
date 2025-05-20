# Übungsbeispiel 4: Brute-Force-Angriff auf ein Remote Desktop Protocol (RDP)

## Theoretische Aufgabe
1. Erkläre, warum schwache Passwörter ein großes Risiko bei RDP darstellen und recherchiere den Standard-Port.

## Praktische Übung - RDP Penetrationstest

### Voraussetzungen
- Zwei virtuelle Maschinen im gleichen Netzwerk
- Kali Linux als Angreifer-VM
- Windows Server/Pro als Ziel-VM
- VirtualBox oder VMware für die Virtualisierung

### Durchführung

1. **Vorbereitung der Ziel-VM:**
   - Windows-Einstellungen → System → Remote Desktop aktivieren
   - Testbenutzer "rdptest" mit Passwort "Password123!" anlegen
   - Firewall-Regeln für RDP überprüfen

2. **Reconnaissance:**
   ```bash
   # Netzwerk-Scan
   sudo nmap -p 3389 -sV [Ziel-IP]
   
   # RDP-Informationen sammeln
   nmap --script rdp-* -p 3389 [Ziel-IP]
   ```

3. **Verbindungstests:**
   - Xfreerdp verwenden:
   ```bash
   xfreerdp /v:[Ziel-IP] /u:rdptest /p:Password123!
   ```
   
   - Hydra für Brute-Force Test:
   ```bash
   hydra -l rdptest -P wordlist.txt [Ziel-IP] rdp
   ```

4. **Log-Analyse:**
   - Auf der Ziel-VM:
     - Ereignisanzeige → Windows-Protokolle → Sicherheit
     - Nach Event-IDs 4624 (erfolgreiche Anmeldung) und 4625 (fehlgeschlagene Anmeldung) suchen

5. **Dokumentation:**
   - Screenshots der Scans
   - Gefundene Schwachstellen
   - Erfolgreiche/fehlgeschlagene Anmeldeversuche
   - Empfehlungen zur Härtung

### Auswertung
- Wie viele Anmeldeversuche wurden protokolliert?
- Welche Schwachstellen wurden identifiziert?
- Wie kann der RDP-Dienst gehärtet werden?

## Weiterführende Ressourcen
- Microsoft RDP Security Guidelines
- NIST Special Publication 800-53
- CIS Benchmarks für RDP-Sicherheit
