alert_file = "alerts/sample_alerts.txt"

def classify_alert(alert):
    text = alert.lower()

    if "failed login" in text:
        return "High", "Possible brute force attack"

    if "powershell" in text:
        return "Medium", "Suspicious PowerShell execution"

    if "normal user login" in text:
        return "Low", "Likely normal activity"

    return "Unknown", "Needs investigation"


def triage():
    try:
        with open(alert_file, "r") as f:
            alerts = f.read().split("\n\n")

        print("[SOC] Alert triage started\n")

        for alert in alerts:
            severity, action = classify_alert(alert)

            print("ALERT:")
            print(alert)
            print("Severity:", severity)
            print("Action:", action)
            print("---------------------")

    except FileNotFoundError:
        print("Alert file not found")


if __name__ == "__main__":
    triage()
