# report.py
def print_report(results):
    if not results:
        print("No vulnerabilities found.")
        return

    for r in results:
        print("\n[+] Vulnerability Found")
        print(f"Name       : {r['name']}")
        print(f"Severity   : {r['severity']}")
        print(f"Description: {r['description']}")
        print(f"Fix        : {r['fix']}")
