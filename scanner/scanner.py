# scanner.py
from utils import normalize_url, get_domain
from checks.headers import check_headers
from checks.directories import check_directories
from checks.robots import check_robots
from checks.cms import detect_cms
from checks.ports import check_ports
from report import print_report

def main():
    target = input("Nhập website cần kiểm tra: ")
    url = normalize_url(target)
    domain = get_domain(url)

    results = []
    results += check_headers(url)
    results += check_directories(url)
    results += check_robots(url)
    results += detect_cms(url)
    results += check_ports(domain)

    print_report(results)

if __name__ == "__main__":
    main()
