import os

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '/': ' ',
    # '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    # '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    # '----.': '9',
    # Punctuation and special characters (commented out)
    # '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!',
    # '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
    # '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
    # '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
    # '.--.-.': '@', '...---...': 'SOS'
}


def read_text(encrypted_text_path: str) -> str:
    with open(encrypted_text_path, "r") as file:
        text = file.read()
    return text


def check_and_fix_write_file(plain_text_path):
    try:
        if os.path.getsize(plain_text_path):  # Cleans the solution file if it's been already used
            with open(plain_text_path, 'w'):
                pass
    except FileNotFoundError as e:
        print("File NOT found")
        print(f"File {plain_text_path} will be created!")


class MorseCodeSolver:
    def __init__(self, encrypted_text_path: str, plain_text_path: str):
        self.encrypted_text = read_text(encrypted_text_path)
        self.encrypted_text = self.encrypted_text.replace("!", "")  # Clean up the text
        self.encrypted_words = self.encrypted_text.split()  # Break it into words

        self.plain_text_path = plain_text_path

        check_and_fix_write_file(self.plain_text_path)

    def decode_morse_text(self, candidate_words, current_word, word_index):
        current_word_idx = len(candidate_words)
        if current_word_idx >= len(self.encrypted_words):
            self.write_plain_text(candidate_words)
        else:
            encrypted_word = self.encrypted_words[current_word_idx]
            for morse_signal, character in morse_code_dict.items():
                if (len(encrypted_word[word_index:]) >= len(morse_signal) and
                        encrypted_word[word_index:].startswith(morse_signal)):
                    word_index += len(morse_signal)
                    current_word += character
                    if word_index == len(encrypted_word):
                        candidate_words.append(current_word)
                        self.decode_morse_text(candidate_words, "", 0)
                        candidate_words.pop()
                    else:
                        self.decode_morse_text(candidate_words, current_word, word_index)
                        word_index -= len(morse_signal)
                        current_word = current_word[:-1]

    def write_plain_text(self, words):
        print("Writing solution")
        with open(self.plain_text_path, "a") as file:
            for word in words:
                file.write(word)
            file.write("\n")
