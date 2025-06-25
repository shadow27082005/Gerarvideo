
# ------------------------------------
# frontend/app.py
# ------------------------------------
from lib.backend.app_factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
