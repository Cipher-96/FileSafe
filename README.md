# FileSafe

FileSafe is a privacy-first public utility for converting documents, PDFs, and images without requiring login or tracking users.

## Features
- DOC, DOCX, PPT, PPTX, XLS, XLSX, PDF, JPG, PNG, and HTML conversion support
- Drag & drop upload
- File chooser upload
- 100 MB max file size
- Secure temporary file cleanup
- No login or account system
- No personal data collection or tracker cookies
- Security headers included
- SEO pages and sitemap
- AdSense-ready layout
- Responsive design for desktop and mobile

## Tech stack
- Backend: Python + Flask
- Frontend: HTML, CSS, JavaScript
- Conversion: LibreOffice CLI, Pillow, pypdf, WeasyPrint
- Deployment: Gunicorn

## Local development

1. Clone the repository
2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install system dependencies on Linux:

```bash
sudo apt-get update
sudo apt-get install -y libreoffice poppler-utils libcairo2 libpango-1.0-0 libgdk-pixbuf2.0-0 libffi-dev
```

5. Create a .env file:

```env
SECRET_KEY=change-me
FLASK_DEBUG=1
HOST=0.0.0.0
PORT=5000
TEMP_FOLDER=tmp
```

6. Run the app:

```bash
python app.py
```

Open http://localhost:5000

## Production deployment

### Render
- Create a Web Service
- Connect this repository
- Build command:

```bash
pip install -r requirements.txt
```

- Start command:

```bash
gunicorn app:app
```

- Add environment variables:
  - `SECRET_KEY`
  - `TEMP_FOLDER`
  - `HOST`
  - `PORT`

### Railway
- Import the repository
- Use the Python service
- Add the same environment variables
- Start command:

```bash
gunicorn app:app
```

## Privacy and security
FileSafe is built with privacy-first defaults:
- No login system
- No user tracking
- No account database
- No long-term file retention
- Temporary files are deleted after conversion
- Security headers are applied to responses

## System requirements
A production Linux server should have:
- Python 3.11+
- LibreOffice installed for DOC/DOCX/PPT/PPTX/XLS/XLSX conversions
- Poppler utilities for PDF image conversion
- Enough memory for conversion jobs

## License
MIT
