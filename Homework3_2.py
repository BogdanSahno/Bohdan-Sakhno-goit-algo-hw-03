import random

def get_numbers_ticket(min: int, max: int, quantity: int):
        if min < 1 or min > max or max > 1000 or quantity < 1 or quantity > (max - min):
            return []
        numbers_set = set()
        while len(numbers_set) < quantity:
            numbers_set.add(random.randint(min, max))
        return sorted(list(numbers_set))
    


lottery_numbers = get_numbers_ticket(1, 1000, 10)
    
print("Ваші лотерейні числа:", lottery_numbers)
       