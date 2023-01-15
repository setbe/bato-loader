from batoparser import *

parser = Parser()
parser.parse('https://bato.to/series/117782/moonrise-by-the-cliff')

for i, value in enumerate(parser.chapters):
    print(value.name, "\t\t", value.link)