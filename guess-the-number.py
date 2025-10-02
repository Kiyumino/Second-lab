import random

def guess_number():
    print("=== Игра 'Угадай число' ===")
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1
            
            if guess < secret_number:
                print("Слишком маленькое число! Попробуй еще раз.")
            elif guess > secret_number:
                print("Слишком большое число! Попробуй еще раз.")
            else:
                print(f"🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break
                
        except ValueError:
            print("Пожалуйста, вводи только цифры!")

if __name__ == "__main__":
    guess_number()