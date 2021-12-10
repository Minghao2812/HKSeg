"""
Author: Wang Minghao (19454414@life.hkbu.edu.hk)
According to the current version of [jieba](https://github.com/fxsjy/jieba) (jieba3k 0.35.1), 
every line in a user-defined dictionary should be like:
word(mandantory) frequency(optional) part_of_speech(optional)
Three parts are joined by a space character.
However, after testing with only a word in every line, it will come up with an error.
That's a bug in the jieba source code,
it requires additional word frequency in every line of user-defined dictionary using function jieba.load_userdict().
(I've submitted an issue on this.)
To solve this quickly, we can simply append an additional space character to every line.
That's what this script does.
"""
from os import listdir
from os.path import isfile, join


def main():
    dictPath = './userdict'  # The folder stores all user-defined dictionary.
    files = [
        join(dictPath, f) for f in listdir(dictPath)
        if isfile(join(dictPath, f)) and ".txt" in f
    ]

    for file in files:
        with open(file, encoding='utf-8', mode='r') as f:
            lines = f.readlines()

        # Remove single '\n' line if it exists.
        if lines[-1] == '\n':
            lines.pop()

        # Append a ' ' to every line. The last line won't have additional '\n'.
        idx = 0
        while idx < len(lines) - 1:
            lines[idx] = lines[idx].strip('\n') + ' ' + '\n'
            idx += 1
        lines[idx] = lines[idx].strip('\n') + ' '

        with open(file, encoding='utf-8', mode='w') as f:
            f.writelines(lines)


if __name__ == '__main__':
    main()