# checks/cms.py
import requests

def detect_cms(url):
    results = []
    try:
        if requests.get(url + "/wp-login.php").status_code == 200:
            results.append({
                "name": "Phát hiện WordPress",
                "severity": "Thông tin",
                "description": "Website sử dụng hệ quản trị nội dung WordPress",
                "fix": "Cập nhật WordPress và các plugin thường xuyên"
            })

        if requests.get(url + "/administrator/").status_code == 200:
            results.append({
                "name": "Phát hiện Joomla",
                "severity": "Thông tin",
                "description": "Website sử dụng hệ quản trị nội dung Joomla",
                "fix": "Cập nhật Joomla thường xuyên"
            })
    except:
        pass

    return results
