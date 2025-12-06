import difflib

def load_dictionary(filename="words.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        return {word.strip().lower() for word in f}
# Load dictionary
words = load_dictionary()
word_list = list(words)   # difflib needs a list

print("Dictionary Loaded ✓")
print("Total words:", len(words))
print("--------------------------------")

while True:
    word = input("Enter a word (or type exit): ").lower()

    if word == "exit":
        break

    if word in words:
        print("✔ Correct word!")
    else:
        print("❌ Word not found.")

        # Auto-Correct suggestions
        suggestions = difflib.get_close_matches(word, word_list, n=3, cutoff=0.75)

        if suggestions:
            print("✨ Did you mean:")
            for s in suggestions:
                print("  →", s)
        else:
            print("No suggestions found.")
    
    print("--------------------------------")

