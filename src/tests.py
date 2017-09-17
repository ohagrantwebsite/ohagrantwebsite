import parser_to_json


def get_chart_test(filename):
    #print(parser_to_json.get_chart(filename, None, [0,-1]))

    #print(parser_to_json.get_chart(filename, 'Fiscal Year', [0,-1]))

    #print(parser_to_json.get_chart(filename, 'TEST', [0,-1]))
    
    parser_to_json.get_chart(filename, 'Fiscal Year', [])

if __name__ == '__main__':
    filename = "OHA Test Data Grant_2013_2014_2015_2016_Table.xlsx"
    get_chart_test(filename)
