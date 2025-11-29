from datetime import datetime

def format_duration(hours):
    if hours < 1:
        minutes = int(hours * 60)
        return f"{minutes} minutes"
    else:
        return f"{hours:.2f} hours"

def validate_vehicle_number(vehicle_num):
    if len(vehicle_num) < 6:
        return False
    return True

def save_report_to_file(report_data, filename="reports/daily_report.txt"):
    with open(filename, 'w') as f:
        f.write(report_data)
    print(f"✅ Report saved to {filename}")