import pandas



def parse_excel(filename):
    df = pandas.read_excel(open(filename, 'rb'))

    print(df)


fn = "data/OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"

parse_excel(fn)
