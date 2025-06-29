# Searching HomeWork Module 5 Neoversity

<h3>HomeWork_5_1.py</h3>
<p>Додайте метод <b>delete</b> для видалення пар ключ-значення таблиці <b>HashTable</b>, яка реалізована в конспекті.</p>

<h3>HomeWork_5_2.py</h3>
<p>Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.</p>

<h3>HomeWork_5_3.py</h3>
<p>Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (<a href="https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view">стаття 1</a>, <a href="https://drive.google.com/file/d/18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w/view">стаття 2</a>). Використовуючи <b>timeit</b>, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.</p>

## Висновки

Під час виконання експерименту було проведено аналіз ефективності алгоритмів пошуку відповідно до 3го завдання.

Було створено списки підрядків різної довжини (як реальні так і вигадані) для обчислення середнього часу х пошуку по текстах.

<b><i>Внаслідок отримано наступні результати:</b></i>
| Назва алгоритму     | Cтаття 1 реальні, мс | Cтаття 1 вигадані, мс | Cтаття 2 реальні, мс | Cтаття 2 вигадані, мс |
|---------------------|----------------------|-----------------------|----------------------|-----------------------|
| Кнута-Морріса-Пратта|        0.501 мс      |        0.771 мс       |       0.619 мс       |       1.099 мс        |
| Боєра-Мура          |        0.116 мс      |        0.120 мс       |       0.089 мс       |       0.142 мс        |
| Рабіна-Карпа        |        1.235 мс      |        1.800 мс       |       1.545 мс       |       2.551 мс        |

Бачимо наступне:

- пошук вигаданих (відсутніх) даних займає більше часу у всіх алгоритмах в обох статтях;
- найкращим є алгоритм Боєра-Мура, пошук за яким виконується в рази швидше за конкурентів.

Таким чином, для пошука підрядків в звичайних текстах краще користуватися саме алгоритмом Боєра-Мура. Найгірше себе показує алгоритм Кнута-Морріса-Пратта.