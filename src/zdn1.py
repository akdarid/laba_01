import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
        if yo2e:
            text = text.replace("ё","е")
            text = text.replace("Ё","Е")
            text = text.replace("\t"," ").replace("\n"," ").replace("\r"," ")
            text = text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))

def tokenize(text: str) -> list[str]:
    return re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq_dict = {}
    for token in tokens:
        freq_dict[token] = freq_dict.get(token, 0) + 1
    return freq_dict


def top_n(tokens: list[str], n: int = 5) -> list[tuple[str, int]]:
    # Используем count_freq для подсчета частот
    freq = count_freq(tokens)

    # Сортируем по убыванию частоты и по алфавиту
    items = list(freq.items())
    items.sort(key=lambda item: (-item[1], item[0]))

    return items[:n]
