import csv

def copy_lines_with_countries(source_file, destination_file):
    countries_to_check = ['Kyrgyzstan', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan', 'Tajikistan']

    with open(source_file, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        with open(destination_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers)
            writer.writeheader()

            for row in reader:
                if row['Country'] in countries_to_check:
                    writer.writerow(row)

    print("Lines with specified countries copied successfully.")

# Usage example
source_file_path = 'literacy1.csv'
destination_file_path = 'literacy2.csv'

copy_lines_with_countries(source_file_path, destination_file_path)


