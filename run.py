<<<<<<< HEAD:run.py
=======

import os

>>>>>>> 46452180217b1e9d5761da862ba3bf9ff4ffff11:app.py
from app import crear_app

app = crear_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
