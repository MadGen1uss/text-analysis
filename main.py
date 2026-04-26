text = input("Введите текст: ")

words = text.lower().split()

word_count = len(words)
print(f"Количество слов: {word_count}")

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("\nПовторяющиеся слова:")
for word, count in sorted(word_frequency.items(), key=lambda x: x[1], reverse=True):
    if count > 1:
        print(f"'{word}': {count} раз(а)")
