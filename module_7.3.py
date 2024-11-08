class WordsFinder:

    def __init__(self, *files_):
        self.file_names = []
        for file in files_:
            self.file_names.append(file)
        print(self.file_names)

    def get_all_words(self):
        all_words = {}
        for file_ in self.file_names:
            with (open(file_, encoding = 'utf-8') as file_name):
                content = file_name.read()
                lower_content = content.lower()
                clear_file = lower_content.replace(',','').replace('.','').\
                replace('=','').replace('!', '').replace('?', '').\
                    replace(';', '').replace(':', '').replace('-', '')
                split_file = clear_file.split()
                a = []
                a +=  split_file
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

finder1 = WordsFinder('file2.txt', 'file1.txt')
print(finder1.get_all_words())
print(finder1.find('для'))
print(finder1.count('captain'))