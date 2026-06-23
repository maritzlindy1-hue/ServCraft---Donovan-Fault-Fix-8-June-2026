GitHub files for Donovan Ticket Dashboard.

This keeps the same previous dashboard layout:
- Current Dashboard tab
- Ticket Trend tab

Upload all files to GitHub and redeploy on Render.

Render settings:
Environment: Python
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
