Correct Render upload files.

Upload all files in this folder to GitHub:
- app.py
- dashboard.html
- requirements.txt
- render.yaml

Render settings:
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
