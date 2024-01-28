from datetime import datetime


def get_days_from_today(date):
    try:
        user_date = datetime.strptime(date, '%Y-%m-%d')
    except:
        print(f"Помилка: Невірний формат дати - {date}, введіть дату у форматі 'РРРР-ММ-ДД'")
        return None
    else:   
        current_date = datetime.now()
        delta = current_date.toordinal() - user_date.toordinal()
        return delta
    
    
input_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
result = get_days_from_today(input_date)
if result is not None:
    print(f'Різниця у днях між {input_date} та поточною датою: {result} днів.')


