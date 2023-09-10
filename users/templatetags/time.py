from datetime import datetime, timezone

from django import template

register = template.Library()


@register.filter
def days_until(date):
    date = date
    now = datetime.now(timezone.utc)

    print(date)
    print(now)

    difference = now - date

    seconds = difference.total_seconds()

    if seconds < 60:
        return f'{int(seconds)} seconds'
    elif seconds < 3600:
        minutes = seconds / 60
        return f'{int(minutes)} minutes'
    elif seconds < 86400:
        hours = seconds / 3600
        return f'{int(hours)} hours'
    elif seconds < 2629800:
        days = seconds / 86400
        return f'{int(days)} days'
    else:
        months = seconds / 2629800
        return f'{int(months)} months'
