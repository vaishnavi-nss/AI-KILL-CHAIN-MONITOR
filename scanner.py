import nmap
import json

def get_risk(port, service):
    # Simple rule-based risk tagging
    risky_ports = {
        21: "FTP - insecure file transfer",
        22: "SSH - possible brute force",
        23: "Telnet - insecure protocol",
        25: "SMTP - spam/misuse risk",
        53: "DNS - amplification attacks",
        80: "HTTP - web vulnerabilities",
        443: "HTTPS - SSL/TLS issues",
        3306: "MySQL - database exposure"
    }

    if port in risky_ports:
        return risky_ports[port]
    
    if service:
        return f"Check service: {service}"
    
    return "Unknown risk"


def run_scan(target: str):
    scanner = nmap.PortScanner()

    try:
        # 🔥 Upgrade: Service detection added
        scanner.scan(target, arguments='-F -sV')

        results = []

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()

                for port in ports:
                    service = scanner[host][proto][port].get('name', 'unknown')

                    results.append({
                        "host": host,
                        "protocol": proto,
                        "port": port,
                        "state": scanner[host][proto][port]['state'],
                        "service": service,
                        "risk": get_risk(port, service)
                    })

        return {
            "target": target,
            "results": results
        }

    except Exception as e:
        return {"error": str(e)}


def save_results(data):
    with open("data/scan_results.json", "w") as f:
        json.dump(data, f, indent=4)
