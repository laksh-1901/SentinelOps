from config import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    DISK_THRESHOLD
)

from modules.logger import logger
from modules.alerts import send_email


def check_thresholds(system):

    alerts = []

    if system["cpu"] > CPU_THRESHOLD:
        alerts.append(f"⚠ CPU Usage High ({system['cpu']}%)")

    if system["memory"] > MEMORY_THRESHOLD:
        alerts.append(f"⚠ Memory Usage High ({system['memory']}%)")

    if system["disk"] > DISK_THRESHOLD:
        alerts.append(f"⚠ Disk Usage High ({system['disk']}%)")

    if alerts:

        message = "\n".join(alerts)

        logger.warning(message)

        try:
            send_email(
                "SentinelOps Alert",
                message
            )

        except Exception as e:
            logger.error(str(e))

    return alerts
