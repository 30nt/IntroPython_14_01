
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых
# будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string


class PlayFolder:
    def __init__(self, dir_name):
        self._dir_name = dir_name
        self._create_dir()

    @property  # lesson15_2
    def dir_name(self):
        return self._dir_name

    def _create_dir(self):
        if not os.path.isdir(self._dir_name):
            os.mkdir(self._dir_name)

    def _create_file(self, symbol):
        filename = os.path.join(self._dir_name, f"{symbol}.txt")
        with open(filename, "w") as file:
            file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))

    def create_all_files(self):
        for symbol in string.ascii_lowercase:
            self._create_file(symbol)

    def tanos_click(self):
        files = list(set(os.listdir(self._dir_name)))
        for file in files[:len(files) // 2]:
            os.remove(os.path.join(self._dir_name, file))

    # @staticmethod  # lesson15
    # def _create_file(symbol, dir_name):
    #     filename = os.path.join(dir_name, f"{symbol}.txt")
    #     with open(filename, "w") as file:
    #         file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))
    #
    # def create_all_files(self):
    #     for symbol in string.ascii_lowercase:
    #         self._create_file(symbol, self._dir_name)

play_folder = PlayFolder("alphabet")
play_folder.create_all_files()
play_folder.tanos_click()


# print(play_folder.dir_name)
# play_folder.dir_name = 10