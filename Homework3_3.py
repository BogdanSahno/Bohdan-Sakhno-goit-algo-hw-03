import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if cleaned_number.startswith('+'):
        return cleaned_number
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    else:
        return '+38' + cleaned_number
    

numbers =["    +38(050)123ва-32-34", "     0503451234", "(050)8в п88п 9900", "38050-11о а  1-22-22", "38050 1  рм11 22 11   "]    
sanitized_numbers = [normalize_phone(num) for num in numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)