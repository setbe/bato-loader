from batoparser import *

comic_title = "Місяць над Прірвою (eng)"

parser = Parser()
parser.parse('https://bato.to/series/117782/moonrise-by-the-cliff')

for i, value in enumerate(parser.chapters):
    value.parse()
    value.save(comic_title)