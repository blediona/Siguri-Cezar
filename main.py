from attack import attack_caesar
from file_handler import read_text_file, load_known_words, write_text_file


def main():
    print("=" * 50)
    print("SULMI I KODIT TE CEZARIT ME FJALE TE NJOHURA")
    print("=" * 50)

    ciphertext = read_text_file("encrypted_text.txt")
    known_words = load_known_words("known_words.txt")

    if not ciphertext:
        print("Nuk ka tekst te enkriptuar per analizim.")
        return

    if not known_words:
        print("Lista e fjaleve te njohura eshte bosh.")
        return

    result = attack_caesar(ciphertext, known_words)

    print("\n--- REZULTATI ME I MUNDSHEM ---")
    print(f"Qelesi me i mundshem: {result['best_shift']}")
    print(f"Piket: {result['best_score']}")
    print(f"Fjalet e gjetura: {result['best_matches']}")
    print("\nTeksti i dekriptuar:")
    write_text_file("decrypted_text.txt", result["best_text"])
    print(result["best_text"])

    print("\n--- TE GJITHA PROVAT ---")
    for attempt in result["all_attempts"]:
        print("-" * 50)
        print(f"Qelesi: {attempt['shift']}")
        print(f"Piket: {attempt['score']}")
        print(f"Fjalet e njohura: {attempt['matches']}")
        print(f"Teksti: {attempt['text']}")


if __name__ == "__main__":
    main()