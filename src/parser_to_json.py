import pandas
import json
import math
import StringIO
from flask import Flask, make_response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import os

def parse_excel(filename, filters, page, per_page):
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    fn = filename
    df = pandas.read_excel(open(fn, 'rb'))

    result = df
    for fil in filters:
        result = filter_by_param(result, param=fil['column'],
                                operator=fil['operator'], value=fil['value'])

    h_lim = get_page(page, len(result), per_page)
    l_lim = get_page(page - 1, len(result), per_page)
    indices = result.index.values.tolist()

    extra_data = {'Elements': len(result),
                  'Pages': math.ceil(len(result)/per_page),
                  'h_lim': h_lim,
                  'l_lim': l_lim,
                  'indices': indices}

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
        try:
            return df[df[param].str.contains(value)]
        except:
            return df
    elif operator=='equals':
        try:
            return df[df[param] == float(value)]
        except:
            return df
        """
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
        """

def get_dropdowns(filename):
    fn = filename
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

def get_chart(filename, axis, indices, mode):


    fn = filename
    df = pandas.read_excel(open(fn, 'rb'))
    result = df
    if len(indices) > 0:
        result = df.iloc[indices]

    if mode == 'Count':
        if axis != None:
            try:
                result = result[axis].value_counts().to_frame()
            except KeyError:
                result = result['Fiscal Year'].value_counts().to_frame()
        else:
            result = result['Fiscal Year'].value_counts().to_frame()
    elif mode == 'Average':
        if axis != None:
            try:
                result = result[axis].value_counts().to_frame()
            except KeyError:
                result = result['Fiscal Year'].value_counts().to_frame()
        else:
            result = result['Fiscal Year'].value_counts().to_frame()

    plt.style.use('seaborn-white')
    ax = None
    ax = result.plot(kind='bar')
    ax.set_axisbelow(True)
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'Ubuntu'
    plt.rcParams['font.monospace'] = 'Ubuntu Mono'
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.titlesize'] = 10
    plt.rcParams['xtick.labelsize'] = 8
    plt.rcParams['ytick.labelsize'] = 8
    plt.rcParams['legend.fontsize'] = 10

    ax.legend_.remove()
    ax.grid(color='#C0C0C0', linestyle='solid', axis='y', zorder=0)
    plt.xlabel(axis)
    plt.ylabel(mode)

    #plt.rcParams['figure.titlesize'] = 12
    #plt.show()

    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'

    plt.close('all')

    return response
