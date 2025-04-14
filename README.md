# 🌐 Moke Travels API

This is the backend API for the **Moke Travels** web application, built using **Django** and **Django REST Framework**. It serves data and handles authentication, likes, comments, and more for the Moke Travel frontend.

> The frontend (built with React) is available in a separate repository:  
> [🔗 Moke Travel Frontend](https://github.com/mohd-yaseen-official/moke-travels.git)

---

## ⚙️ Features

- ✅ **User Authentication** (Register, Login, Logout)
- 📍 **Place Listing**
  - Title, Description, Cover Image, Location
- 🖼️ **Single Place Page**
  - Full Description
  - Gallery Images
  - Likes and Comments
  - Location
- ❤️ **Like/Unlike Places**
- 💬 **Comment on Places**
- 🔒 JWT or Token-Based Authentication

---

## 🛠️ Tech Stack

- **Backend Framework**: Django
- **API Layer**: Django REST Framework (DRF)
- **Authentication**: JWT
- **Database**: PostgreSQL
- **Media Handling**: Django's media storage for image uploads

---
## 📁 Project Structure
```
moke-travels/ 
├── venv/
├── src/ 
|    └── traveller/
|        ├── api/
|        |   └── v1/
|        |       └── places/
|        |       |   ├── serializer.py
|        |       |    └── views.py
|        |       |   └── urls.py
|        |       └── category/ 
|        |       |   ├── serializers.py 
|        |       |   └── views.py 
|        |       |   └── urls.py
|        ├── places/
|        ├── category/
|        ├── traveller/
|        |   ├── urls.py
|        |   └── settings.py
|        ├── manage.py
|        ├── r.txt
```      
---
## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohd-yaseen-official/moke-travels-api.git
cd moke-travels-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r r.txt
```

### 4. Create a `.env` file in the root directory and add:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True-or-False
DB_NAME=your-db-name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=your-db-port
```

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a superuser (optional but recommended)

```bash
python manage.py createsuperuser
```

### . Start the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## ✨ Credits

Developed with 💙 by [Mohamed Yaseen](https://github.com/mohd-yaseen-official)
