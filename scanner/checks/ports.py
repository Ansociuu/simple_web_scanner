# checks/ports.py
import socket

PORTS = [80, 443, 8080]

def check_ports(domain):
    results = []
    for port in PORTS:
        try:
            s = socket.create_connection((domain, port), timeout=2)
            s.close()
            results.append({
                "name": "Cổng dịch vụ đang mở",
                "severity": "Thông tin",
                "description": f"Cổng {port} đang mở",
                "fix": "Đóng các cổng không cần thiết"
            })
        except:
            pass
    return results
