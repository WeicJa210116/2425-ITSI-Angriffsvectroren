# Angriffsvektoren Gegenmaßnahmen

### Definition:
Gegenmaßnahmen sind präventive oder reaktive Maßnahmen, die ergriffen werden, um potenzielle Sicherheitsrisiken zu minimieren oder Angriffe abzuwehren. Sie umfassen technische, organisatorische und personelle Maßnahmen zum Schutz von IT-Systemen und Daten.

## Ziele der Sicherheit in Netzen

- Geheimhaltung (privacy)

- Datenintegrität muss gewährleistet sein, d.h. gegen absichtliche Veränderungen geschützt sein (data integrity)

- Teilnehmer müssen sich zweifelsfrei identifizieren können (Authentifikation oder authenticity).

## Generelle Vorsichtsmaßnahmen

- Bedrohungsanalyse („threat modelling“)

- Minimal nötige Rechtevergabe („least privilege“)

- Angriffspunkte oder Angriffsvektoren eliminieren

- Angriffsfläche minimieren („Attack Surface Reduction“) z.B. nicht benötigte Dienste abschalten

## Die verschiedenen Schritte von Gegenmaßnahmen

## Bedrohungen und ihre Gegenmaßnahmen
*Hier sind nicht alle Bedrohungen und Gegenmaßnahmen aufgelistet*

### Mail:
- Bedrohungen:

  ![InitialAccessTacticsMail](/imgs/InitialAccessTacticsMail.png)

- Gegenmaßnahmen:
    - Mail-Gateway mit KI und Verhaltensanalyse
    - Cloud Application Security Broker (CASB)
    - Sicheres Web-Gateway (SWG)
    - Mitarbeiterschulungen, da der Mensch die größte Schwachstelle ist

### Web und Webanwendungen:

- Bedrohungen:

  ![InitialAccessTacticsWeb](/imgs/InitialAccessTacticsWeb.png)

- Gegenmaßnahmen:

    - Schließen aller Schwachstellen
    - Suche nach bösartigen Skripts
    - Deaktivieren aller nicht benötigten Ports auf Webservern

### Schwachstellen:

- Bedrohungen:

  ![InitialAccessTacticsVulnerabilites](/imgs/InitialAccessTacticsVulnerabilites.png)

- Gegenmaßnahmen:
    - Priorisiertes Patch-Management
    - Zero-Day-Planung und kontinuierliche Überwachung
    - Virtuelle Patches als temporäre Absicherung
    - Aufbau einer Sicherheitskultur

## Links:

- [stefanux.de](https://www.stefanux.de/wiki/doku.php/securityangriffsmethoden-und-gegenma%C3%9Fnahmen)
- [trendmicro.com](https://www.trendmicro.com/de_de/research/24/i/schutz-vor-angriffsvektoren-fur-den-erstzugriff-teil-1.html)