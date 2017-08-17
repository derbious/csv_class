# csvread.py: Read a csv file & print every line.
# csvspacer.py: read a csv file. print each line with 4 spaces instread of the comma  "thing    sku    $price"
# csvsum.py: read the csv file. sum up the $price amount - print the sum   Around 25000???
# csvpopular.py Find the most popular "department" (department == first 2 digits) (print all first place in case of tie)


# Pro tips. you can use the python csv module.
# https://docs.python.org/3/library/csv.html
import csv

with open('data.csv', newline='') as data_file:  ### FILE OPEN REQUEST => File
    reader = csv.reader(data_file)               ### Feed the raw bytes of the file into a csv reader
    for row in reader:
        print(row)      # <<< type(row) is a list
