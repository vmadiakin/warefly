import csv
import re


def process_csv(input_file, output_file, delimiter=','):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8',
                                                                     newline='') as outfile:
            reader = csv.reader(infile, delimiter=delimiter)
            writer = csv.writer(outfile, delimiter=delimiter)

            header = next(reader)
            writer.writerow(header)

            for row_number, row in enumerate(reader, start=2):
                try:
                    processed_row = [re.sub(r"'", '"', elem) for elem in row]

                    writer.writerow(processed_row)
                except Exception as ex:
                    print(f'Ошибка обработки данных в строке {row_number}: {ex}')

    except csv.Error as e:
        print(f'Ошибка CSV: {e}')
    except Exception as ex:
        print(f'Необработанная ошибка: {ex}')


input_file = 'lenta-ru-news.csv'
output_file = 'lenta-ru-news-processed.csv'
process_csv(input_file, output_file)
