num = []
while True:
    us_input = input("Введите число (или 'end' для завершения): ")
    if us_input == "end":
        break
    try:
        num.append(int(us_input))
    except ValueError:
        print("Пожалуйста, введите корректное число или 'end'.")

print("Список введенных чисел:", numb)

greater_than_previous = [num[i] for i in range(1, len(num)) if num[i] > num[i - 1]]
print("Элементы списка, которые больше предыдущего:", greater_than_previous)