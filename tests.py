from caesar_cipher import encrypt_caesar, decrypt_caesar
from attack import attack_caesar

def run_tests():
    print("=" * 50)
    print("TESTIMI I PROJEKTIT")
    print("=" * 50)

    original_text = "Projekti jane nje prime ne python"
    shift = 3

    encrypted = encrypt_caesar(original_text, shift)
    decrypted = decrypt_caesar(encrypted, shift)

    print("\n[TEST 1] Enkriptim / Dekriptim")
    print("Teksti origjinal :", original_text)
    print("Teksti i enkriptuar :", encrypted)
    print("Teksti i dekriptuar :", decrypted)

    if original_text == decrypted:
        print("TEST 1 KALOI")
    else:
        print("TEST 1 DESHTOI")
        
    known_words = {
        "projekti", "jane", "nje", "ne", "python", "prime"
    }

    result = attack_caesar(encrypted, known_words)

    print("\n[TEST 2] Sulmi ndaj Caesar Cipher")
    print("Qelesi i gjetur :", result["best_shift"])
    print("Teksti i gjetur :", result["best_text"])
    print("Piket :", result["best_score"])
    print("Fjalet e gjetura :", result["best_matches"])


if __name__ == "__main__":
    run_tests()