import pandas
import json
import math

def parse_excel(filename, filters, page, per_page):
    fn = "data/" + filename
    df = pandas.read_excel(open(fn, 'rb'))

    result = df
    for fil in filters:
        result = filter_by_param(result, param=fil['column'],
                                operator=fil['operator'], value=fil['value'])

    h_lim = get_page(page, len(result), per_page)
    l_lim = get_page(page - 1, len(result), per_page)

    extra_data = {'Elements': len(result),
                  'Pages': math.ceil(len(result)/per_page),
                  'h_lim': h_lim,
                  'l_lim': l_lim}

    result_page = result[l_lim : h_lim]
    result_dict = json.loads(result_page.to_json(orient='table'))
    result_dict.update(extra_data)
    result_json = json.dumps(result_dict)
    return result_json

def get_page(page, length, per_page):
    if page * per_page <= length:
        return page * per_page
    else:
        return length

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

def get_dropdowns(filename):
    fn = "data/" + filename
    df = pandas.read_excel(open(fn, 'rb'))
    """
    Fiscal Year    -> List of years
    Grant Type     -> Types of grants
    Organization   -> List of orgs
    Project        -> (no dropdown)
    Amount         -> (not a dropdown)
    Location       -> List of locations
    Stategic Priority -> List of priorities
    Strategic Results -> List of results
    TOTAL # SERVED -> (not a dropdown)
    # NH SERVED -> (not a dropdown)
    GrantStatusId -> list of statuses
    """
    ret_dict = {}
    ret_dict['Fiscal Year'] = sorted(df['Fiscal Year'].unique())
    ret_dict['Grant Type']  = sorted(df['Grant Type'].unique())
    ret_dict['Organization']  = sorted(df['Organization'].unique())
    ret_dict['Location']  = sorted(df['Location'].unique())
    ret_dict['Strategic Priority']  = sorted(df['Strategic Priority'].unique())
    ret_dict['Strategic Results']  = sorted(df['Strategic Results'].unique())
    ret_dict['GrantStatusId'] = sorted(df['GrantStatusId'].unique())

    return json.dumps(ret_dict)
