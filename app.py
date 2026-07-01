from flask import Flask, render_template
from monitor import get_system_info
from services import get_services

app = Flask(__name__)

@app.route("/")
def home():
    system = get_system_info()
    services = get_services()

    return render_template(
        "index.html",
        system=system,
        services=services
    )

if __name__ == "__main__":
    app.run(debug=True)
