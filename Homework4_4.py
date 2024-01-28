from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    list_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday2024 = birthday.replace(year=today.year)
        if birthday2024 < today:
            birthday2024 = birthday2024.replace(year=today.year + 1)
        days_do_birthday = (birthday2024 - today).days
        if days_do_birthday >= 0 and days_do_birthday <= 7:
            if birthday2024.weekday() in [5, 6]:
                congratulation_date = birthday2024 + timedelta(days=(7 - birthday2024.weekday()))
            else:
                congratulation_date = birthday2024
            list_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return list_birthdays


users = [{"name": "John Doe", "birthday": "1985.02.01"}, {"name": "Jane Smith", "birthday": "1990.02.03"}]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)