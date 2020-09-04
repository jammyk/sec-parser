from dataset.number import Number
from database.number_repository import NumberRepository
file_to_table_name_map = {
    'cal.tsv': 'calculations',
    'dim.tsv': 'dimensions',
    'num.tsv': 'numbers',
    'pre.tsv': 'presentation',
    'ren.tsv': 'rendering',
    'sub.tsv': 'submissions',
    'tag.tsv': 'tags',
    'txt.tsv': 'text'
}


def read_tsv(file_name):
    with open(file_name) as file:
        ds = Number()
        data = ds.parse_dataset(file)
        number_repo = NumberRepository()
        number_repo.insert_numbers(data)


if __name__ == '__main__':
    print(read_tsv('./data/num.tsv'))
