import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from caesar_cipher import encrypt_caesar, decrypt_caesar
from attack import attack_caesar

def run_tests():
    print("=" * 60)
    print("TESTIMI I PROJEKTIT: SIGURIA E TË DHËNAVE")
    print("=" * 60)

    original_text = "Ky eshte nje projekt i rendesishem per lenden e sigurise se dhenave"
    shift = 5  
    
    encrypted = encrypt_caesar(original_text, shift)
    decrypted = decrypt_caesar(encrypted, shift)

    print("\n[TEST 1] Enkriptim / Dekriptim")
    print("Teksti origjinal    :", original_text)
    print("Teksti i enkriptuar :", encrypted)
    print("Teksti i dekriptuar :", decrypted)

    if original_text == decrypted:
        print("STATUSI: TESTI 1 KALOI ME SUKSES")
    else:
        print("STATUSI: TESTI 1 DËSHTOI")
        
    known_words = {
        "projekt", "rendesishem", "lenden", "sigurise", "dhenave", "eshte"
    }

    result = attack_caesar(encrypted, known_words)
    
    print("\n[TEST 2] Sulmi ndaj Caesar Cipher (Brute Force)")
    print("Çelësi i zbuluar:", result["best_shift"])
    print("Teksti i gjetur:", result["best_text"])

    if result["best_shift"] == shift:
        print("STATUSI: SULMI ISHTE I SUKSESSHËM!")
    else:
        print("STATUSI: SULMI DËSHTOI! Nuk u gjetën mjaftueshëm fjalë.")

if __name__ == "__main__":
    run_tests() 