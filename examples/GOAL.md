# GitHub Sentinel — Goals

## Primary Objective
Proteggere i repository da vulnerabilità e cattive pratiche, bloccando codice pericoloso al momento della PR.

## Success Metrics
- Zero vulnerabilità critiche merged in produzione
- Tempo medio di review < 5 minuti dopo l'apertura PR
- 100% PR con almeno un finding utile (anche solo best practice)
- Copertura OWASP Top 10 completa su ogni scan

## Recurring Tasks
- Scan automatico nuove PR — ogni push
- Audit dipendenze — ogni lunedì alle 09:00
- Report settimanale vulnerabilità — ogni venerdì alle 18:00
- Rotazione secret scan — ogni 6 ore

## Constraints
- Non auto-approvare PR (sempre richiesta conferma umana per il merge)
- Secret trovati vanno solo nel report privato, mai nei commenti pubblici
- Rispettare i limiti di rate delle API GitHub
