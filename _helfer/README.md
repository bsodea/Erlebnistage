# Helfer

## Kurzanleitung: Bilder mit goldenem Rahmen als PDF erstellen

1 Ordner erstellen

Einen images Ordner anlegen und darin die Bilder "erstellen":

text

```text
??/
├── frame_pdf.py
└── images/
    ├── Tom.jpg
    ├── Max.png
    └── Laura.jpg
```

2. Skript ausführen

Im Terminal in den Projektordner wechseln und ausführen:

bash

```bash
python gold_frames_to_pdf.py
```

6. Ergebnis ansehen

Nach erfolgreicher Ausführung werden automatisch zwei Ergebnisse erstellt:

- `gold_framed_collection.pdf` – alle Bilder mit goldenem Rahmen, jeweils auf einer eigenen PDF-Seite.
- `framed_images/` – die einzelnen Bilder inklusive goldenem Rahmen.

Fertig\! Die Bilder werden automatisch angepasst, zentriert und proportional auf das A4-Format skaliert.
