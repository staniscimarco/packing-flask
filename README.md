# packing-flask

## Struttura del progetto
Il progetto è strutturato nelle seguenti directory e file principali:

- `app.py`: Il file principale che gestisce il backend del sistema.
- `static/`: Directory contenente file statici come immagini e audio.
  - `static/image/`: Contiene il logo del progetto.
  - `static/audio/`: Contiene il file audio per l'allarme.
- `templates/`: Directory contenente i template HTML utilizzati per la dashboard e le workstation.
  - `templates/index.html`: Pagina principale della dashboard con la visualizzazione delle workstation.
  - templates/workstation.html`: Pagina dove visualizzare i menu per resettare l'errore delle workstation.
  - `templates/workstation_simple.html`: Pagina di dettaglio per una singola workstation.

## Installazione
1. Clona il repository sul tuo sistema locale:
   ```bash
   git clone https://github.com/tuonome/workstation-dashboard.git
   cd workstation-dashboard
