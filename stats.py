def sort_on(dict):
	return dict["num"]

def  dict_sort(dict):
	result = []
	for char, count in dict.items():
		char_dict = {"char": char, "num": count}
		result.append(char_dict)
	result.sort(reverse=True, key=sort_on)
	return result

def convert_text(text):
	char_counts = {}
	for char in text:
		char = char.lower()
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def get_word_count(text):
        num_words = text.split()
        return len(num_words)

