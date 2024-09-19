"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
  with open('/Users/nikitaraikov/referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()

    length_of_stroki = len(content)
    print(f"Длина строки: {length_of_stroki}")

    words_count = len(content.split())
    print("Количество слов в тексте: ", words_count)

    change_symbols = content.replace(".", "!")

    with open('/Users/nikitaraikov/referat2.txt', 'w', encoding='utf-8') as f:
       f.write(change_symbols)
     

if __name__ == "__main__":
    main()
