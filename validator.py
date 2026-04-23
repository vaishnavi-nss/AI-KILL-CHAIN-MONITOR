def assign_severity(port, service, state):
    if state != "open":
        return "Low"

    # High risk ports
    if port in [21, 23, 445, 3389]:
        return "High"

    # Medium risk
    if port in [22, 25, 53, 80]:
        return "Medium"

    # Default
    return "Low"


def validate_results(scan_data):
    seen = set()
    validated = []

    for item in scan_data.get("results", []):
        key = (item["port"], item["service"])

        # Remove duplicates
        if key in seen:
            continue
        seen.add(key)

        severity = assign_severity(
            item["port"],
            item["service"],
            item["state"]
        )

        validated.append({
            **item,
            "severity": severity
        })

    return {
        "target": scan_data["target"],
        "validated_results": validated
    }
