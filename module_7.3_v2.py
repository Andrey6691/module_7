class WordsFinder:

    def __init__(self, *files_):
        self.file_names = []
        for file in files_:
            self.file_names.append(file)
        print(self.file_names)

    def get_all_words(self):
        all_words = {}

        for file_ in self.file_names:
            a = []
            with open(file_, encoding = 'utf-8') as file_name:
                for line in file_name:
                    line = line.lower()
                    chars_to_remove = [',', '.', '=', '!', '?', ';', ':', '-']
                    for char in chars_to_remove:
                        line = line.replace(char, '')
                    line = line.split()
                    a += line
                    all_words[file_] = a
        return all_words

    def find(self, word):
        finder_ ={}
        word = word.lower()
        for name, words in self.get_all_words().items():
            if word in words:
                f = words.index(word) + 1
                finder_[name] = f
        return finder_

    def count(self, words):
        finder_2 = {}
        words = words.lower()
        for name, word in self.get_all_words().items():
            count_word = word.count(words)
            finder_2[name] = count_word
        return finder_2


finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'file2.txt')
print(finder2.get_all_words()) # Все слова//
print(finder2.find('captain')) # 3 слово по счёту
print(finder2.count('captain')) # 4 слова teXT в тексте всего