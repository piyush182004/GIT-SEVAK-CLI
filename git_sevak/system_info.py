import platform
import psutil
import json

def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU": platform.processor(),
        "Total RAM": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
    }
    return json.dumps(info, indent=4)
