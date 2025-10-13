from lib.text import normalize,tokenize,count_freq,top_n
import sys


def main():
    text = sys.stdin.read()

    if not text.strip():
        print("Нет входных данных")
        return


    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)


    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    if top_words:
        max_word_length = max(len(word) for word, count in top_words)
        column_width = max(max_word_length, 8)

        print("\nТоп-5:")
        print("слово".ljust(column_width) + " | частота")
        print("-" * column_width + "-|---------")

        for word, count in top_words:
            print(word.ljust(column_width) + f" | {count}")
    else:
        print("\nТоп-5: нет слов для отображения")






if __name__ == "__main__":
    main()