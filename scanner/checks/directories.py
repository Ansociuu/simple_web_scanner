# checks/directories.py
import requests

SENSITIVE_PATHS = [
    "/admin",
    "/login",
    "/phpinfo.php",
    "/.git/",
    "/.env"
]

def check_directories(url):
    results = []
    for path in SENSITIVE_PATHS:
        try:
            r = requests.get(url + path, timeout=5)
            if r.status_code == 200:
                results.append({
                    "name": "Lộ đường dẫn nhạy cảm",
                    "severity": "Cao",
                    "description": f"Phát hiện đường dẫn có thể truy cập: {path}",
                    "fix": "Hạn chế truy cập hoặc loại bỏ các file/thư mục nhạy cảm"
                })
        except:
            pass
    return results
