import subprocess


def check_service(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True
        )

        if result.stdout.strip() == "active":
            return "Running"

        return "Stopped"

    except Exception:
        return "Unknown"


def get_services():

    return {
        "ssh": check_service("ssh"),
        "nginx": check_service("nginx"),
        "gunicorn": check_service("gunicorn")
    }
