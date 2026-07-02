from flask import Flask, render_template
from modules.monitor import get_system_info
from modules.services import get_services
from modules.website_monitor import check_website
from modules.health_checker import check_thresholds

app = Flask(__name__)

@app.route("/")
def home():
    system = get_system_info()
    alerts = check_thresholds(system)
    services = get_services()
    website = check_website("https://www.google.com")

    return render_template(
        "index.html",
        system=system,
        services=services,
        website=website,
        alerts=alerts
    )

if __name__ == "__main__":
    app.run(debug=True)
