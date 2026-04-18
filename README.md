# Sulmi ndaj Kodit te Cezarit
Sulmi permes kerkimit te fjaleve te njohura ne ndonje tekst fajll

----

## Pershkrimi i Projektit
Ky projekt implementon nje sulm ndaj algoritmit te enkriptimit Caesar Cipher duke perdorur tekniken e kerkimit te fjaleve te njohura (known words attack).

Programi merr nje tekst te enkriptuar nga nje fajll dhe provon te gjitha zhvendosjet e mundshme (1-25). Per secilin rezultat, kontrollon sa fjale te njohura gjenden ne tekst dhe zgjedh dekriptimin me te mundshem.

---

## Qellimi
- Te demonstrohet dobesia e Caesar Cipher
- Te implementohet nje sulm praktik (brute force + known words)

---

## Si funksionon
1. Lexohet teksti i enkriptuar nga `encrypted_text.txt`
2. Lexohen fjalet e njohura nga `known_words.txt`
3. Programi provon te gjitha zhvendosjet (1-25)
4. Per secilen zhvendosje:
   - behet dekriptimi
   - numerohen fjalet qe perputhen
5. Zgjidhet rezultati me numrin me te madh te perputhjeve

---

## Si te ekzekutohet
1. Sigurohu qe ke Python te instaluar
2. Vendos tekstin e enkriptuar ne `encrypted_text.txt`
3. Vendos fjalet e njohura ne `known_words.txt`
4. Ekzekuto komanden:

```bash
python main.py
```
---

#### Punuar nga:
- Aurela Kajtazi
- Bledar Morina
- Blediona Aliu
- Elma Ademi
