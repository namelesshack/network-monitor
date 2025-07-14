import os
import platform
from notifier import send_notification

SERVERS = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1"
}

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    response = os.system(f"ping {param} 1 {host} > /dev/null 2>&1")
    return response == 0

def get_server_status():
    status = {}
    for name, ip in SERVERS.items():
        is_up = ping(ip)
        status[name] = "UP" if is_up else "DOWN"
        if not is_up:
            send_notification(f"{name} ({ip}) is DOWN!")
    return status
