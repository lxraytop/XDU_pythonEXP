import argparse
import chardet


def guesscoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(100)
        encoding = chardet.detect(raw_data)['encoding']
    return encoding


def convert_to_utf8(input_file, output_file, encoding=None):
    if not encoding:
        encoding = guesscoding(input_file)
        print(f"编码可能是: {encoding}")

    with open(input_file, 'r', encoding=encoding, errors='ignore') as f:
        content = f.read()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"文件已转换为UTF-8编码并保存至: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='将文件从指定编码转换为UTF-8.')
    parser.add_argument('input_file', type=str, help='文件读取路径.')
    parser.add_argument('output_file', type=str, help='文件保存路径.')
    parser.add_argument('--encoding', type=str,
                        help='指定编码')
    args = parser.parse_args()

    convert_to_utf8(args.input_file, args.output_file, args.encoding)


if __name__ == "__main__":
    main()
