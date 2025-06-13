# 📝 Task Management System

A simple Django-based web app to manage personal tasks. Users can **create**, **view**, **edit**, and **delete** tasks with an intuitive interface.

---

## 🚀 Features

- ✅ Create, Read, Update, Delete tasks
- ✅ Custom 404 error page
- ✅ Beautiful, responsive UI with CSS
- ✅ Secure with CSRF protection
- ✅ Easy to deploy with Whitenoise static file support
- ✅ Static file support using Whitenoise
- ✅ Production-ready with PostgreSQL support


---

## 🛠️ Tech Stack

- **Python 3**
- **Django**
- **SQLite** (default, currently PostgreSQL)
- **HTML5 + CSS3**

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/task-manager.git
cd task-manager
```

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Run the development server**

```bash
python manage.py runserver
```

---


#### Custom 404 Page

Create a `404.html` in your templates folder and make sure `DEBUG = False` and `ALLOWED_HOSTS` is set correctly in `settings.py`.

---

## 🧪 Testing 404 Page

Run the server and visit a non-existent URL like:

```
http://127.0.0.1:8000/not-a-page
```

Make sure `DEBUG = False` in `settings.py`.

---

## 📁 Folder Structure

```
task-manager/
├── tasks/               # Django app
├── static/              # Static files (CSS, images)
├── templates/           # HTML templates
├── media/               # Uploaded media (if any)
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## 🧠 Future Improvements

- ✅ Add user authentication
- ⏳ Due dates and reminders
- ⏳ Task priority system
- ⏳ Pagination and search

---

