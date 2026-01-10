# Fruits Project (Django on Raspberry Pi)

A small learning project built with Django and running on a Raspberry Pi.  
The project originally started as a JSON backend for a separate frontend, but has evolved into a **server-rendered Django application using templates and static files**.

The Raspberry Pi runs the application continuously via systemd and serves HTML pages directly to the browser.

---

## Goal

Practice core Django concepts in a realistic setup:

- Django project and app structure
- Views, URLs, and templates
- Template inheritance (`base.html`, blocks, includes)
- Static files (CSS and images)
- Conditional rendering in templates
- Custom 404 error page
- Running Django persistently on a Raspberry Pi (systemd)

---

## Tech Stack

- Python
- Django
- SQLite (default Django database)
- HTML (Django templates)
- CSS (static files)
- Raspberry Pi (LAN server)
- systemd (24/7 runtime)

---

## Project Layout

```
raspberry-pi-backend-test/
├─ core/                 Django project (settings, urls, wsgi)
├─ fruits_app/           Django app
│  ├─ templates/
│  │  └─ fruits_app/
│  │     ├─ base.html
│  │     ├─ header.html
│  │     ├─ fruitlist.html
│  │     └─ info.html
│  ├─ static/
│  │  └─ fruits_app/
│  │     ├─ css/
│  │     │  └─ style.css
│  │     └─ img/
│  │        ├─ header.png
│  │        ├─ 404.png
│  │        └─ fruit images …
│  └─ views.py
├─ templates/
│  └─ 404.html            Global custom 404 template
├─ manage.py
├─ requirements.txt
├─ .gitignore
└─ .venv/                 Virtual environment (not committed)
```

---

## Setup (Raspberry Pi)

```bash
cd ~/projects/raspberry-pi-backend-test

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

---

## Running the Project

### Persistent mode (recommended)

The backend runs automatically via systemd:

```bash
sudo systemctl status fruits-backend
sudo systemctl start fruits-backend
```

Application URL:

```
http://192.168.0.96:8000/fruits/
```

### Manual run (development / testing)

```bash
source .venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

For testing static files with `DEBUG = False`:

```bash
python manage.py runserver --insecure 0.0.0.0:8000
```

---

## Pages / Routes

- `/fruits/`  
  Main page showing all fruits, including ordered and non-ordered sections

- `/fruits/info/`  
  Info page rendered via template inheritance

- Custom `404.html`  
  Displayed when `DEBUG = False`

---

## Templates & Rendering

- Server-side rendering using Django templates
- `base.html` defines the global layout
- `header.html` is included globally
- `fruitlist.html` renders fruit data in tables
- Template logic uses `for` loops and `if` conditions

---

## Static Files

- CSS and images are served via Django static files
- Static assets are referenced using `{% static %}`
- Fruit images are defined in the view and rendered in templates

---

## Notes

- The original standalone frontend is now obsolete.
- Django handles both data and presentation.
- systemd manages the virtual environment and process lifecycle.
- `runserver` is used only for development and testing.
- This is a learning project, intentionally kept explicit and simple.

---

License: Private learning project
