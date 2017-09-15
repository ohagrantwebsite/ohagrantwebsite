import pandas

def parse_excel(filename, query):
    fn = "data/" + filename
    df = pandas.read_excel(open(fn, 'rb'))
    split_query = query.split('@')

    if split_query[1] == 'range':
        split_query[2] = split_query[2].split('-')

    result = filter_by_param(df, param=split_query[0], operator=split_query[1], value=split_query[2])
    print(result)
    return result.to_json()

def filter_by_param(df, param=None, operator=None, value=None):

    if param == None or operator == None or value == None:
        return df
    if operator=='like':
        return df[df[param].str.contains(value)]
    elif operator=='range':
        lower = None
        upper = None
        try:
            lower = float(value[0])
        except:
            lower = None
        try:
            upper = float(value[1])
        except:
            upper = None
        if upper == None and lower == None:
            return df
        elif upper == None and lower != None:
            return df[df[param] >= lower]
        elif upper != None and lower == None:
            return df[df[param] <= upper]
        elif upper != None and lower != None:
            temp_df = df[df[param] <= upper]
            return temp_df[df[param] >= lower]


parse_excel('OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx', 'Fiscal Year@range@2013-2014')
