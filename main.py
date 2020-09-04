from dataset.tag import Tag

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
        ds = Tag()
        return ds.parse_dataset(file)


if __name__ == '__main__':
    print(read_tsv('./data/tag.tsv'))
