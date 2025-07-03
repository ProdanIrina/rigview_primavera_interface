# RigView - Primavera Interface (Backend)

## Structură foldere

```
backend/
└── app/
    ├── api/                # Endpoints FastAPI (expun API REST către frontend)
    ├── models/             # Modele Pydantic (structuri de date pentru API)
    ├── services/           # Servicii business logic + integrare Primavera
    └── utils/              # Config, DB connection, utilitare, security, etc.
```

---

## Rolul principalelor fișiere:

- **api/** – endpoints API (nu au logică business, doar apelează serviciile)
- **models/** – structuri de date tip Pydantic, clare, strict tipizate
- **services/**
    - `primavera_client.py` – se ocupă DOAR de comunicarea cu REST API-ul Primavera (requests, autentificare, etc).
    - `sync_service.py` – logica de filtrare și procesare a datelor pentru sincronizare (ex: doar proiecte active, doar activități cu S/AR etc).
- **utils/** – DB connection, configs, security helpers, etc.

---

## Flux tipic pentru sincronizarea activităților

1. **Endpointul `/sync/activities`** (de exemplu) apelează o funcție din `sync_service.py`.
2. Acea funcție folosește metode din `primavera_client.py` pentru a prelua date din Primavera.
3. Datele brute sunt filtrate și procesate în `sync_service.py`, apoi structurate pentru frontend sau pentru persistare.
4. **Toată logica de integrare externă stă în services/** – API-ul e “curat” și clar.

---

## Exemple de business logic:
- Se iau doar proiectele cu `Status` diferit de `Completed`/`Canceled`.
- Din aceste proiecte, doar activitățile care au la codul “Rig View” valorile “S” sau “AR”.
- Se ignoră activitățile fără cod UWI (ProjectCodeType == "UWI").
- Se returnează datele minim necesare pentru UI sau sincronizare.

---

## Configurare rapidă:
- **.env**: pune acolo datele pentru Primavera (user, pass, url).
- **requirements.txt**: să fie requests, fastapi, pydantic etc.

---

## Best Practice:
- Nicio funcție din services/ sau api/ nu face “requests” direct, doar prin `primavera_client.py`.
- Nu amestecați logica de business cu integrarea externă.
- Testele și mock-urile se fac pe nivelul de “service”, nu pe nivelul de client.

---

> **Structura asta permite schimbarea Primavera cu alt sistem, doar înlocuind clientul, nu și business logic-ul.
