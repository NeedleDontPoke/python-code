"""用于修复文件"""


class FixFile:
    __slots__ = ('__filename', '__word_list')

    def __init__(self, filename):
        self.__filename = filename
        self.__word_list = {
            'word_list_easy.txt': ['apple', 'banana', 'elephant', 'fish', 'grape', 'house', 'ice', 'jazz', 'kite',
                                   'lion', 'moon', 'nest', 'orange', 'pear', 'queen', 'rose', 'tree', 'umbrella',
                                   'violet', 'water', 'yellow', 'bell', 'cloud', 'info', 'duck'],

            'word_list_hard.txt': ['Perspicacious', 'Sesquipedalian', 'Obfuscate', 'Mellifluous', 'Disparate',
                                   'Discombobulate', 'Quixotic', 'Cacophony', 'Ineffable', 'Serendipity',
                                   'Supercilious', 'Inscrutable', 'Grandiloquent', 'Rambunctious', 'Penultimate',
                                   'Nebulous', 'Quizzical', 'Ambiguous', 'Diaphanous', 'Epistemology', 'Misanthropic',
                                   'Ostentatious', 'Capitulate', 'Garrulous', 'Jeopardize'],

            'word_list_dead.txt': ['Adventureous', 'Ambivalentize', 'Apprehensively', 'Accidentally', 'Aromaticality',
                                   'Authoritarian', 'Abbreviatively', 'Aggressiveness', 'Anachronistic',
                                   'Authenticator', 'Amalgamations', 'Acquaintances', 'Anticipations', 'Antecedential',
                                   'Acrimoniously', 'Agglutinative', 'Adjudications', 'Applicability', 'Augmentation',
                                   'Aphrodisiacal', 'Abominations', 'Asymptotically', 'Absorptivity', 'Adjudicatory',
                                   'Auspiciously']
        }

    def __fix(self, filename):
        with open(filename, 'w') as file:
            for element in self.__word_list[filename]:
                file.write(f'{element}\n')
            return True

    def fix(self):
        return self.__fix(self.__filename)

    def get_list(self, filename):
        return self.__word_list[filename]
