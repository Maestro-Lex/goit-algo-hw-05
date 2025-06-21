import timeit
import gdown
import matplotlib.pyplot as plt
from algs import kmp_search, boyer_moore_search, rabin_karp_search


def read_data(file_id, encoding: str) -> str:
    '''
    Функція зчитування даних з ресурсу
    '''
    output_file = "article.txt"
    gdown.download(f'https://drive.google.com/uc?id={file_id}', output_file, quiet=False)
    with open(output_file, "r", newline = "", encoding = encoding) as article:
        text = article.read()
    return text

def measure_search(text: str, patterns: list[str], search_alg) -> float:
    '''
    Шукаємо дані та рахуємо час виконання
    '''
    end_time = 0
    for pattern in patterns:        
        sart_time = timeit.default_timer()
        search_alg(text, pattern)
        end_time += timeit.default_timer() - sart_time
    return end_time / len(patterns)


def print_table(data: dict):
    '''
    Табличний вивід фінальних даних
    '''
    columns = (
        "Cтаття 1 реальні, мс",
        'Cтаття 1 вигадані, мс',
        "Cтаття 2 реальні, мс",
        'Cтаття 2 вигадані, мс'
    )
    rows = list(data.keys())
    
    data = [value for value in data.values()]

    fig, ax = plt.subplots(figsize=(16, 2))
    ax.axis('off')
    table = ax.table(cellText=data,
                    rowLabels=rows,
                    colLabels=columns,
                    loc='center')
    plt.show()


def main():
    methods = {
        "Кнута-Морріса-Пратта": kmp_search,
        "Боєра-Мура": boyer_moore_search,
        "Рабіна-Карпа": rabin_karp_search
    }

    article_1 = read_data("18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh", "cp1251")
    article_2 = read_data("18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w", "utf-8")  

    true_patterns_1 = [
        "int firstIndex = 0;",
        "рідко використовується через свою неефективність,"
        "призводять до вирішення поставленої задачі",
        "у відсортованому масиві",
        "startIndex = pos + 1;",
        "жадібним",
        "Жадібний алгоритм – метод розв'язання оптимізаційних задач, заснований на тому, що процес прийняття рішення можна розбити на елементарні кроки, на кожному з яких приймається окреме рішення. Рішення, прийняте на кожному кроці, має бути оптимальним тільки на поточному кроці та повинне прийматися без врахування попередніх або наступних рішень"
    ]

    true_patterns_2 = [
        "дослідження та програмна реалізація методів і структур даних для побудови бази даних рекомендаційної системи",
        "Рекомендаційні системи"
        "Визначаються усі предмети, які належать до контрольної сесії",
        "кількість агентів 65536",
        "Editors Ricci F.",
        "Міхав В.В.",
        "Профілювання показало, що 75% часу роботи тесту варіанту з розгорнутим списком зайняло генерування випадкових даних для програмного імітаційного моделювання агентів та предметів рекомендаційної системи, тож, саме сховище даних має високі показники ефективності. Профілювання варіанту із інвертованим списком показало, що доступ до випадкових"
    ]

    false_parrarns = [
        "Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами.",
        "Другим елементом має бути",
        "вибір підрядків за вашим бажанням",
        "Створіть публічний репозиторій goit-algo-hw-05",
        "goit-algo-hw-05",
        "Критерії прийняття домашнього завдання є обов’язковою умовою оцінювання домашнього завдання ментором. Якщо якийсь з критеріїв не виконано, ДЗ відправляється ментором на доопрацювання без оцінювання.",
        "Прикріплені посилання на репозиторій"
    ]

    table_data = {}    
    for name, method in methods.items():
        a_1_true = round(measure_search(article_1, true_patterns_1, method) * 1000, 3)
        a_1_false = round(measure_search(article_1, false_parrarns, method) * 1000, 3)
        a_2_true = round(measure_search(article_2, true_patterns_2, method) * 1000, 3)
        a_2_false = round(measure_search(article_2, false_parrarns, method) * 1000, 3)

        print("Стаття 1:")
        print(f"Середній час пошуку за алгоритмом {name} для реальних підрядків - {a_1_true} мс")
        print(f"Середній час пошуку за алгоритмом {name} для вигаданих підрядків - {a_1_false} мс")
        print("Стаття 2:")
        print(f"Середній час пошуку за алгоритмом {name} для реальних підрядків - {a_2_true} мс")
        print(f"Середній час пошуку за алгоритмом {name} для вигаданих підрядків - {a_2_false} мс")
        print("---------------------------------------")
        
        table_data[name] = (a_1_true, a_1_false, a_2_true, a_2_false)

    print_table(table_data)


if __name__ == "__main__":
    main()