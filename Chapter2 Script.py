from collections import Counter

# Ciphertext provided by the user
ciphertext = """
Wry zp vs przuviy ls zay wlilzvc wyqvuzhysz vz zay QTC rsljyunlzx gpccyiy zay dlbl syzdpum eygvhy rsvjvlcvecy.
Spz v nlsicy qyunps gprcw rny zay lszyusyz vsw spepwx avw vggynn zp Ecvgmepvuw. Zaln dvn v wlnvnzyu eygvrny nzrwyszn
dyuys'z vecy zp rqcpvw zaylu nygrulzx ynnyszlvcn uyqpuzn. Crgmlcx pru nzrwyszn vuy uynprugybrcc vsw zayx vcc dysz zp
zay Hgwpsvcwn zp rny zay qreclg syzdpum zp rqcpvw zaylu gpruny dpum. Vbzyudvuwn zayx gycyeuvzyw dlza v slgy Avqqx Hyvc
vsw sriiyzn. QTC{AvqqxHyvc}
"""

# Remove spaces and newlines for accurate frequency analysis
ciphertext_cleaned = ''.join(filter(str.isalpha, ciphertext.upper()))

# Count the frequency of each letter
letter_frequency = Counter(ciphertext_cleaned)

# Display the most common letters in the ciphertext
letter_frequency.most_common()

# Display the most common letters in the ciphertext
print("Most common letters in the ciphertext and their frequencies:")
for letter, freq in letter_frequency.most_common():
    print(f"{letter}: {freq}")

# English letter frequency from most to least common
english_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

# Adjusting substitutions based on feedback
adjusted_substitutions = {

    #Lowercase letters

    'y': 'E',  # High frequency, likely 'E'
    'z': 'T',  # High frequency, possibly 'T'
    'v': 'A',  # Next likely substitution based on frequency ('v' is very common in the ciphertext)
    'p': 'O',
    's': 'N',
    'r': 'U',
    'n': 'S',
    'u': 'R',
    'l': 'I',
    'w': 'D',
    'g': 'C',
    'c': 'L',
    'q': 'P',
    'd': 'W',
    'x': 'Y',
    'e': 'B',
    'a': 'H',
    'i': 'G',
    'm': 'K',
    'h': 'M',
    'b': 'F',
    'j': 'V',

    #Uppercase letters

    'Q': 'P',
    'T': 'X',
    'C': 'L',
    'W': 'D',
    'S': 'N',
    'E': 'B',
    'H': 'M',
    'V': 'A',
    'A': 'H',
}


# Perform the adjusted substitution
fully_deciphered_text_adjusted = "".join(adjusted_substitutions.get(c, c) for c in ciphertext)

# Display the adjusted fully deciphered text for analysis
print("\nDeciphered text: \n" + fully_deciphered_text_adjusted)

