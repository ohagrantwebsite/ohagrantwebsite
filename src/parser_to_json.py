import pandas

def parse_excel(filename, query):
    fn = "data/" + filename
    df = pandas.read_excel(open(fn, 'rb'))
    return df.to_json()
