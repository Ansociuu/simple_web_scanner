# checks/headers.py
import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Strict-Transport-Security"
]

def check_headers(url):
    results = []
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers

        if "Server" in headers:
            results.append({
                "name": "Lộ thông tin máy chủ",
                "severity": "Thấp",
                "description": f"Header Server bị lộ: {headers['Server']}",
                "fix": "Ẩn hoặc làm mờ thông tin header Server"
            })

        for h in SECURITY_HEADERS:
            if h not in headers:
                results.append({
                    "name": f"Thiếu header {h}",
                    "severity": "Trung bình",
                    "description": f"Header bảo mật {h} chưa được cấu hình",
                    "fix": f"Cấu hình web server để bổ sung header {h}"
                })

    except Exception as e:
        pass

    return results
