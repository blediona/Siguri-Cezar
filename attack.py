from caesar_cipher import decrypt_caesar


def score_text(text, known_words):
    words = text.lower().split()
    score = 0
    matched_words = []

    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word in known_words:
            score += 1
            matched_words.append(cleaned_word)

    return score, matched_words


def attack_caesar(ciphertext, known_words):
    best_shift = None
    best_text = ""
    best_score = -1
    best_matches = []

    all_attempts = []

    for shift in range(1, 26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        score, matches = score_text(decrypted_text, known_words)

        attempt = {
            "shift": shift,
            "text": decrypted_text,
            "score": score,
            "matches": matches
        }
        all_attempts.append(attempt)

        if score > best_score:
            best_score = score
            best_shift = shift
            best_text = decrypted_text
            best_matches = matches

    return {
        "best_shift": best_shift,
        "best_text": best_text,
        "best_score": best_score,
        "best_matches": best_matches,
        "all_attempts": all_attempts
    }