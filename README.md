## Quizly_Backend

**Quizly Backend** is a RESTful API built with Django and Django REST Framework.
It allows users to generate quizzes automatically from YouTube videos using AI-powered transcription and question generation.

---

## Technologies
- **Python 3.11+**
- **Django 5.2.10**
- **Django REST Framework 3.16.1**
- **Simple JWT 5.5.1 (JWT Authentication with Access & Refresh Tokens)**
- **Google Gemini API (google-genai 1.59.0)**
- **OpenAI Whisper 20250625 (audio transcription)**
- **yt-dlp 2025.12.8 (YouTube audio extraction)**
- **PyTorch 2.10.0 (AI model runtime)**
- **python-dotenv 1.2.1 (environment variable management)**
- **django-cors-headers 4.9.0 (CORS handling)**

---

## Features
- User registration and authentication using JWT tokens and cookies
- Generate quizzes from YouTube URLs:
- Downloads audio from the video
- Transcribes audio into text
- Uses AI to generate 10 quiz questions from the transcript
- CRUD operations for quizzes (create, read, update, delete)
- Permission-based access (users can only manage their own quizzes)
- RESTful API architecture
  
---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/LarsThoennes/Quizly_Backend
cd Quizly_Backend
```
### 2. Create a virtual environment
```bash
python -m venv venv
```
### 3. Activate the environment

#### 3.1 macOS / Linux
```bash
source venv/bin/activate
```
#### 3.2 Windows
```bash
venv\Scripts\activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Create your `.env` file

A template file `.env.template` is provided in the project root with example values for development.

Copy the template file and rename it to `.env`:

Then update the values in the .env file with your own configuration:
```env
DEBUG=True
CORS_ALLOW_CREDENTIALS=True
CORS_ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
CSRF_TRUSTED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
ALLOWED_HOSTS=localhost,127.0.0.1
SECRET_KEY=your_secret_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```
### 6. Create migrations
```bash
python manage.py makemigrations
```
### 7. Apply migrations
```bash
python manage.py migrate
```
### 8. (Optional) Create a superuser for the admin panel
```bash
python manage.py createsuperuser
```
### 9. Run the Development Server
```bash
python manage.py runserver
```
### 10. The server will start at:
```bash
http://127.0.0.1:8000/
```

