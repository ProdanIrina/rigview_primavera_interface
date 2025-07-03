Sigur! Uite conținutul pentru `frontend/README.md` scris ca bloc de cod, să-l copiezi direct:

```markdown
# RigView–Primavera Interface (Frontend)

> Interfață React pentru vizualizarea și gestionarea sincronizării dintre Primavera și RigView.

---

## 📁 Structura proiectului

```

frontend/
├── public/
├── src/
│   ├── assets/                # Imagini, SVG-uri etc.
│   ├── components/
│   │   ├── ui/                # Butoane, Layout, Navbar, etc.
│   │   └── pages/             # DashboardPage.jsx, LogsPage.jsx, LoginPage.jsx, SyncPage.jsx
│   ├── utils/                 # auth.jsx, classnames.jsx etc.
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
├── .gitignore
├── README.md
├── package.json
├── vite.config.js
└── etc.

````

---

## ⚙️ Pornire locală

1. **Instalează dependențele:**
    ```bash
    npm install
    ```

2. **Pornește aplicația:**
    ```bash
    npm run dev
    ```
    > Aplicația va fi disponibilă pe [http://localhost:5173](http://localhost:5173).

---

## 🧩 Paginile principale

- **DashboardPage.jsx** – status sincronizări, buton pentru sincronizare manuală
- **LogsPage.jsx** – tabel loguri cu căutare și export Excel
- **LoginPage.jsx** – autentificare utilizator (inclusiv test user)
- **SyncPage.jsx** – sincronizare manuală (dacă e cazul)
- **components/ui/** – butoane, layout, navbar, ProtectedRoute etc.
- **utils/** – autentificare și funcții helper

---

## 🔒 Autentificare

- **LoginPage.jsx** folosește endpointul `/login` de pe backend (FastAPI).
- User de test rapid:  
````

user: testuser
pass: testpass

````

---

## 🔗 Legătură cu backend

- Backend-ul trebuie să ruleze pe `http://localhost:8000`.
- Dacă schimbi portul sau adresa, actualizează URL-urile din fetch-uri din cod sau folosește variabile de mediu (Vite).

---

## 📦 Comenzi utile

- **Build pentru producție:**  
```bash
npm run build
````

* **Preview local build de producție:**

  ```bash
  npm run preview
  ```

---

## ❓ Ajutor

* Pentru probleme tehnice, contactează echipa de dezvoltare sau deschide un issue.
* Documentație suplimentară: vezi și `backend/README.md`.

```

### Copiază direct acest cod în `frontend/README.md` și ai un README complet și curat!  
Dacă vrei și exemplu pentru backend, spune și ți-l scriu imediat, în același stil.
```
