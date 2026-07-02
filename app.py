from flask import Flask, render_template
from modules.monitor import get_system_info
from modules.services import get_services
from modules.website_monitor import check_website

app = Flask(__name__)

@app.route("/")
def home():

    system = get_system_info()
    services = get_services()

    website = check_website("http://127.0.0.1:5000")

    return render_template(
        "index.html",
        system=system,
        services=services,
        website=website
    )

if __name__ == "__main__":
    app.run(debug=True)
