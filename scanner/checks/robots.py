# checks/robots.py
import requests

def check_robots(url):
    results = []
    try:
        r = requests.get(url + "/robots.txt", timeout=5)
        if r.status_code == 200 and "Disallow" in r.text:
            results.append({
                "name": "Lộ thông tin qua robots.txt",
                "severity": "Thấp",
                "description": "robots.txt tiết lộ các đường dẫn bị hạn chế truy cập",
                "fix": "Tránh liệt kê các đường dẫn nhạy cảm trong robots.txt"
            })
    except:
        pass
    return results
