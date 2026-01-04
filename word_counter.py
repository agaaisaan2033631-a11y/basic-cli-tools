def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            words = text.split()
            print("word count:", len(words))
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("permission denied")

if __name__ == "__main__":
    target = input("enter file path: ")
    count_words(target)
