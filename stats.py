def get_num_words(text: str) -> int:
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
            continue
        char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]
    
def sorted_word_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    list_dict = []
    for key, value in char_counts.items():
       list_dict.append({"char":key, "num":value})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict