def read_text_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Gabim: fajlli '{filename}' nuk u gjet.")
        return ""

def write_text_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def load_known_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words=[line.strip().lower() for line in file if line.strip()]
        return set(words)
    except FileNotFoundError:
        print(f"Gabim: fajlli '{filename}' nuk u gjet.")
        return set()