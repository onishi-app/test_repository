from django import template


register = template.Library()

@register.filter(name="status_to_string")
def convert_status_to_string(status, name):
    if status == 10:
        return f"Success {name}"
    elif status == 20:
        return f"Error {name}"
    elif status == 30:
        return "Pending"
    elif status == 40:
        return "Failed"
    else:
        return "Unknown"