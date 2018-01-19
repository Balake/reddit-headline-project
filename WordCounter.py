"""
Blake Bryant
"""
# import datetime
import os.path
import csv


class WordCounter:

    def __init__(self):
        self.WORDS_DATES = {}
        self.main_df = {}

    # Assumes the title words have already been cleaned up
    # Stores the words in a dictionary of the following format:
    # Key:      WORD, String
    # Values:   COUNT: Int
    #           OCCURRENCE: Int
    def add_title_to_word_dict(self, title_words):
        l = set()
        words = {}
        for s in title_words:
            if s in words.keys():
                words[s]['Count'] += 1
            else:
                words[s] = {'Count': 1, 'Occurrences': 0}
            # if s in self.WORDS_DATES.keys() and datetime.date.today() not in self.WORDS_DATES[s]:
            #     self.WORDS_DATES[s].append(datetime.date.today())
            # else:
            #     self.WORDS_DATES[s] = [datetime.date.today()]
            l.add(s)
        for word in l:
            words[word]['Occurrences'] += 1
        self.organize_df(words)




    # Cleans up the title passed in (string). Splits by white space into a list, then coverts to all lower case and
    # removes all punctuation. Adds cleaned up word to the word dictionary or updates the count.
    # TODO possible regular expression use
    def clean_up_title(self, s):
        s = s.lower()
        s = s.split()
        title_words = []
        for dirty_word in s:
            cleaned_word = dirty_word.replace('.', '')
            cleaned_word = cleaned_word.replace(';', '')
            cleaned_word = cleaned_word.replace(':', '')
            cleaned_word = cleaned_word.replace('?', '')
            cleaned_word = cleaned_word.replace('!', '')
            cleaned_word = cleaned_word.replace(',', '')
            cleaned_word = cleaned_word.strip('“')
            cleaned_word = cleaned_word.strip('"')
            cleaned_word = cleaned_word.strip('(')
            cleaned_word = cleaned_word.strip(')')
            cleaned_word = cleaned_word.strip("'")
            cleaned_word = cleaned_word.strip('’')
            cleaned_word = cleaned_word.strip('”')
            cleaned_word = cleaned_word.strip(']')
            cleaned_word = cleaned_word.strip('[')
            title_words.append(cleaned_word)
        self.add_title_to_word_dict(title_words)

    def count_words(self, headlines):
        for title in headlines:
            self.clean_up_title(title)

    def organize_df(self, words):
        for word in words:
            if word in self.main_df.keys():
                self.main_df[word]['Count'] += words[word]['Count']
                self.main_df[word]['Occurrences'] += words[word]['Occurrences']
            else:
                self.main_df[word] = words[word]

    def save_df(self, filename):
        """
        :param filename:
        :return:
        PSEUDOCODE:

        if filename exists:
            load existing file
        else:
            create new file

        iterate dataframe and write to file
        """
        if os.path.isfile(filename):
            pass
        else:
            with open(filename, 'w') as csv_file:
                writer = csv.writer(csv_file)
                for key, value in self.main_df.items():
                    writer.writerow([key, value['Count'], value['Occurrences']])

    def print_df(self, t):
        top = dict(sorted(self.main_df.items(), key=lambda xt: xt[1]['Count'], reverse=True)[:t])
        print(" Word                   Count       Occurrences")
        print("+----------------------------------------------+")
        for word in top.keys():
            line = '| ' + word
            for x in range(24 - len(line)):
                line += ' '
            line += str(top[word]['Count'])
            for x in range(35 - len(line)):
                line += ' '
            line += str(top[word]['Occurrences'])
            for x in range(47 - len(line)):
                line += ' '
            line += '|'
            print(line)
        print("+----------------------------------------------+\n")






