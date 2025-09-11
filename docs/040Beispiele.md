# Beispiele aus der Praxis (Case Studies)

## 1. SolarWinds-Hack und FireEye-Schwachstelle
- Entdeckt am: 8. Dezember 2020

- Patch veröffentlicht am: 13. Dezember 2020

- Status: aktiv

Der **SolarWinds-Angriff** im Dezember 2020 wird von Trustwave als der *„lähmendste und verheerendste Breach des Jahrzehnts“* bezeichnet. Es handelte sich um einen **Supply-Chain-Angriff** auf das Netzwerküberwachungstool **SolarWinds Orion**, der weltweit Schockwellen auslöste.

### Wichtige Fakten:

- **Angreifer** nutzten:
  - Red-Team-Tools von **FireEye**
  - Interne **Threat-Intelligence-Daten**
- Ziel: Installation eines **bösartigen Backdoor-Updates** namens **Sunburst**
- Rund **18.000 Kunden** luden das infizierte Update herunter – darunter große Unternehmen und US-Regierungsbehörden.
- **Funktion von Sunburst**:
  - Veränderung, Diebstahl oder Zerstörung von Daten innerhalb betroffener Netzwerke

### Ausmaß des Schadens:

- Trotz der hohen Anzahl betroffener Kunden, gab SolarWinds an, dass **weniger als 100 Kunden tatsächlich kompromittiert** wurden.
- Diese Zahlen decken sich mit den **offiziellen Schätzungen des Weißen Hauses**.

### Aktueller Stand:

- Ein **Patch** wurde am **13. Dezember 2020** veröffentlicht.
- **Noch immer sind Server infiziert**, da:
  - Unternehmen häufig nichts von den **inaktiven Angriffsvektoren** wissen.
  - Angreifer weiterhin über bestehende Sicherheitslücken aktiv sind.

### Experteneinschätzungen:

- **David Kennedy** (ehemaliger NSA-Hacker, Gründer von TrustedSec) sagte im Dezember 2021:
  > "Angreifer können sich buchstäblich jedes Ziel auswählen, das dieses Produkt nutzt. Und das betrifft eine große Anzahl von Unternehmen auf der ganzen Welt."

- **Shital Thekdi** (Professorin für Risikomanagement, University of Richmond) sagte im Juni 2021:
  > "Der Angriff ist beispiellos, weil er in der Lage ist, erhebliche physische Folgen zu verursachen und auch kritische Infrastrukturen zu beeinträchtigen."


## 2. EternalBlue-Exploit, WannaCry und NotPetya
- Entdeckt am: 14. April 2017

- Patch veröffentlicht am: 14. März 2017

- Status: aktiv

Ein weiterer bedeutender Vorfall in der Geschichte der Cybersicherheit ist der **EternalBlue-Exploit**, der 2017 gemeinsam mit einer Reihe von **verheerenden Ransomware-Angriffen** große Schäden anrichtete. Der Exploit wurde zuvor aus den Systemen der **US-amerikanischen NSA** gestohlen und zielte auf eine Sicherheitslücke in **Microsoft Windows** ab.

### Wichtige Fakten:

- **Microsoft veröffentlichte bereits einen Monat vor den Angriffen einen Patch** für die betreffende Schwachstelle.
- Trotzdem bleibt **EternalBlue laut Trustwave weiterhin aktiv**.
- Die Suchmaschine **Shodan listet derzeit über 7.500 anfällige Systeme**, die noch nicht gepatcht wurden.

### Bekannte Ransomware über EternalBlue:

1. **WannaCry**
2. **NotPetya**

- Beide Ransomware-Varianten nutzten den EternalBlue-Exploit zur Verbreitung.
- Sie **infizierten weltweit Tausende Systeme**.
- Besonders schwer betroffen waren:
  - **Gesundheitsdienste in Großbritannien**
  - **Infrastruktur in der Ukraine**

### Experteneinschätzung:

- Laut den **Cyberanalysten von RiskSense** im Jahr 2017:
  > "Der EternalBlue-Exploit ist so gefährlich, weil er einen sofortigen Remote- und nicht authentifizierten Zugriff auf fast jedes ungepatchte Microsoft-Windows-System ermöglicht. Windows ist eines der am weitesten verbreiteten Betriebssysteme und wird sowohl in der Privat- als auch in der Geschäftswelt genutzt."


## 3. Heartbleed-Fehler in OpenSSL
- Entdeckt am: 21. März 2014

- Patch veröffentlicht am: 7. April 2014

- Status: aktiv

Die **Heartbleed-Schwachstelle**, entdeckt im Jahr 2014, zählt zu den schwerwiegendsten Sicherheitslücken in der Geschichte des Internets. Sie betrifft die **OpenSSL-Verschlüsselungstechnologie**, die einen großen Teil des Webverkehrs absichert.

### Wichtige Fakten:

- Die Schwachstelle befindet sich in der **Heartbleed-Erweiterung der TLS/DTLS-Implementierung** (Transport Layer Security Protocols).
- Sie ermöglicht es Angreifern, **RAM-Speicher über das Internet auszulesen** – potenziell mit vertraulichen Daten wie Passwörtern oder privaten Schlüsseln.
- Trotz ihrer Entdeckung 2014 sind laut Trustwave **heute noch über 200.000 Systeme** verwundbar.

### Auswirkungen:

- Die Entdeckung sorgte für **weltweite Panik** in der IT-Sicherheitsbranche.
- Der Sicherheitsforscher **Bruce Schneier** schrieb in seinem Blog:
  > „Auf der Skala von 1 bis 10 ist Heartbleed eine 11.“
- **Roger Grimes**, Sicherheitsberater, betonte:
  > OpenSSL laufe **auf etwa 60 % der Websites**, die HTTPS-Verbindungen anbieten – was das Ausmaß der Bedrohung verdeutlicht.

### Aktueller Stand:

- **Heartbleed wird auch heute noch aktiv ausgenutzt**.
- Viele Systeme bleiben aufgrund fehlender Patches oder unzureichender Updates weiterhin **angreifbar**.

## 4. Sicherheitslücke Shellshock in Bash-Shell
- Entdeckt am: 12. September 2014

- Patch veröffentlicht am: 24. September 2014

- Status: inaktiv

**Shellshock** ist eine schwerwiegende Sicherheitslücke in der *“Bourne again Shell” (Bash)*, die bereits **30 Jahre existierte**, bevor sie im Jahr **2014 entdeckt** wurde. Sie ermöglichte es Angreifern, **vollständige Kontrolle über ein System zu erlangen – ohne Benutzername oder Passwort**.

### Wichtige Fakten:

- **Betroffene Komponente**: Bash, die Standard-Shell auf den meisten **Linux-basierten Systemen**
- **Angriffsvektor**:
  - Webfähige Prozesse, die Bash zur Verarbeitung von Eingaben oder zur Ausführung von Befehlen aufrufen
- **Schweregrad**:
  - Laut Analysten **noch gravierender als Heartbleed**
  - Erlaubte **vollständige Systemübernahme** durch Ausführen beliebiger Befehle

### Sicherheitsmaßnahmen:

- Ein **Patch wurde im September 2014** veröffentlicht.
- Die Schwachstelle gilt **heute als inaktiv**.

### Spätere Nutzung:

- **2019** wurde Shellshock im Rahmen der **„Sea Turtle“-Kampagne** erneut verwendet.
  - Dabei nutzten Hacker **DNS-Hijacking**, um Zugang zu **sensiblen Systemen** zu erlangen.

### Experteneinschätzung:

- **Daniel Ingevaldson**, CTO von Easy Solutions, erklärte 2014 gegenüber CSO:
  > „Das Problem mit Bash ist, dass diese Shell für alles verwendet wird. Auf einem Linux-basierten System ist sie die Standard-Shell, und jedes Mal, wenn ein webfähiger Prozess eine Shell aufrufen muss, um Eingaben zu verarbeiten oder einen Befehl auszuführen, ruft er Bash auf.“


## 5. Zero Day im Framework Apache Struts 2
- Entdeckt am: 6. März 2017

- Patch veröffentlicht am: 5. September 2017

- Status: inaktiv

Diese **kritische Zero-Day-Schwachstelle** betraf den **Multipart-Parser von Jakarta** im Anwendungsentwicklungs-Framework **Apache Struts 2**. Parser analysieren und zerlegen Quelltext, damit dieser von anderen Programmen wie Compilern oder HTML-Renderern verwendet werden kann.

### Wichtige Fakten:

- Die Schwachstelle ermöglichte eine **Remote Command Injection**.
  - Eigentlich dient diese Funktion dazu, Systembefehle auszuführen oder Anwendungen/Skripte zu starten.
  - In diesem Fall wurde sie **missbraucht**, da Eingaben **nicht validiert** wurden.
  - Ergebnis: **Angreifer konnten beliebige Befehle ausführen** und dadurch **Daten einsehen, manipulieren oder löschen**.

### Bekannter Vorfall: Equifax-Datenpanne

- **Equifax**, ein US-Finanzdienstleister, wurde **Monate nach Bekanntwerden der Schwachstelle** Opfer eines massiven Datenlecks.
- **Angriffsvektor**: die ungepatchte Sicherheitslücke in **Apache Struts 2**
- **Betroffene**:
  - Rund **143 Millionen Menschen** in den **USA**, **Großbritannien** und **Kanada**
- Der Vorfall gilt als **einer der größten Datenschutzverstöße** weltweit.

### Aktueller Stand:

- Laut **Trustwave** wird die Schwachstelle aktuell als **inaktiv** eingestuft.
