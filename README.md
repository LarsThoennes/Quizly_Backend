## Quizly_Backend

**Quizly Backend** is a RESTful API built with Django and Django REST Framework.
It allows users to generate quizzes automatically from YouTube videos using AI-powered transcription and question generation.

---

## Technologies
- **Python**
- **Django**
- **Django REST Framework**
- **JWT Authentication (Access & Refresh Tokens)**
- **AI Services (Whisper & Gemini)**
- **yt-dlp**

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
### Create a virtual environment
```bash
python -m venv venv
```
### Activate the environment

#### macOS/Linux
```bash
source venv/bin/activate
```
#### Windows
```bash
venv\Scripts\activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Create migrations
```bash
python manage.py makemigrations
```
### Apply migrations
```bash
python manage.py migrate
```
### (Optional) Create a superuser for the admin panel
```bash
python manage.py createsuperuser
```
### Run the Development Server
```bash
python manage.py runserver
```
### The server will start at:
```bash
http://127.0.0.1:8000/
```
### Create a .env file in the project root and define the following variables:
```env
GEMINI_API_KEY=your_gemini_api_key
```
