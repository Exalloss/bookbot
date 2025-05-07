import sys
from stats import get_word_count, convert_text, dict_sort

def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents
def main():
	if len(sys.argv) < 2:
		print(f"Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	book_text = get_book_text(book_path)
	word_count = get_word_count(book_text)
	char_count = convert_text(book_text)
	sorted_count = dict_sort(char_count)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for item in sorted_count:
		char = item["char"]
		count = item["num"]
		if char.isalpha():
			print(f"{char}: {count}")
	print("============= END ===============")
main()


