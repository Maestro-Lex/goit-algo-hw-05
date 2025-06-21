import random


def bin_search(data: list, x: float) -> tuple:
    low = 0
    high = len(data) - 1
    mid = 0
    count = 0
    nearest_high = 0
 
    while low <= high: 
        mid = (high + low) // 2 
        count += 1
        
        if data[mid] < x:
            low = mid + 1 
        else:
            high = mid - 1
            # Перевизначаємо білше за пошуковане доки не отримаємо найближче
            nearest_high = data[mid]

    return count, nearest_high


if __name__ == "__main__":
    # Формуємо список випадкових дробових даних заданої величини
    size = 10
    data = [] or sorted([round(random.random(), 2) + random.randint(0, size) for _ in range(size)])
    print(f"Наш набір даних:\n{data}")
    
    try:
        result = bin_search(data, float(input("Ведіть число для пошуку (за замовченням 0.5): ").replace(",", ".") or 0.5))
    except ValueError:
        print("Ви ввели некоректне значення для пошуку. Введіть валідне число.")

    print(f"Кількість ітерацій пошуку: {result[0]}.",
          f"\nПошукове значення або найближче більше дорівнює - {result[1]}")