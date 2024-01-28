import re

def normalize_phone(phone_num): 
    cleaned_number  = r"[\d\+]+"                  
    phone_num = "".join(re.findall(cleaned_number, phone_num))
    if len(phone_num) == 10:                          
        phone_num = "+38" + phone_num                
    elif len(phone_num) == 12:
        phone_num = "+" + phone_num
    return phone_num 
    

numbers =["    432 11 222 22 22", "     +123456789012 ", "(050)8в п88п 9900", "38050-11о а  1-22-22", "38050 1  рм11 22 11   "]    
sanitized_numbers = [normalize_phone(num) for num in numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)