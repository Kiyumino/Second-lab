def count_words(filename):
    word_count = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.lower().split()
                for word in words:
                    word = word.strip('.,!?:;()[]{}')
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

    except FileNotFoundError:
        print(f"файл {filename} не найден")
        return {}
    
    return word_count

result = count_words('test.txt')
for word, count in sorted(result.items()):
    print(f"{word}: {count}")