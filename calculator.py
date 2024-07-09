import calc_operations as co

def main():
    print("Добро пожаловать в программу калькулятор.")
    while True:
        print("\nОпции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")


        choice = input("Выберите операцию (1/2/3/4): ")


        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == '1':
                    result = co.add(num1, num2)
                elif choice == '2':
                    result = co.subtract(num1, num2)
                elif choice == '3':
                    result = co.multiply(num1, num2)
                elif choice == '4':
                    result = co.divide(num1, num2)

                print(f"Результат: {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        else:
            print("Недопустимый выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
