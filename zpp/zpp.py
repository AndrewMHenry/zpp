import argparse

VARIABLE_BASE = 'data'
DEFINE_FORMAT = '#define {} {}\n'
VARIABLE_FORMAT = '#define {{}} {} + {{}}\n'.format(VARIABLE_BASE)


def generate_file_lines(*filenames):
    for filename in filenames:
        with open(filename, 'r') as file:
            for line in file:
                yield line


def process_lines(lines, profile=None):
    yield DEFINE_FORMAT.format(VARIABLE_BASE, VARIABLE_BASE_VALUES[profile])
    offset = 0
    for line in lines:
        if line.startswith('.'):

            words = line.split()
            command = words[0]

            if command == '.variable':
                name_word = words[1]
                size_word = words[2]
                yield VARIABLE_FORMAT.format(name_word, str(offset))
                offset += int(size_word)
            else:
                raise SyntaxError('Unexpected command `{}`.'.format(command))

        else:
            yield line


PROFILES = ['ti83papp']
VARIABLE_BASE_VALUES = {
    'ti83papp': '8478h'
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('-o', '--output')
    parser.add_argument('--profile', choices=PROFILES)
    args = parser.parse_args()

    output_lines = list(process_lines(
        generate_file_lines(*args.files), args.profile))
    with open(args.output, 'w') as output_file:
        for output_line in output_lines:
            output_file.write(output_line)
