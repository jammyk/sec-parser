import os

# need to feed data files to this class somehow
#   for now fed through downloading to local -> under root/data


def main():
    for file in os.listdir('data'):
        if file.endswith('.tsv'):
            pass


if __name__ == '__main__':
    main()