#module for aid functions
from datetime import datetime
import pandas as pd
from datetime import datetime
import re

def remove_outter_str(str):
    return str.strip('\'')

def str_into_list(file):
    """ reads a str from a csv file and returns a list of strs"""
    n_file = file.replace('[','')
    n_file = n_file.replace(']','')
    n_file = n_file.replace('\n',',')
    lista = n_file.split(sep=',')
    return [x.strip() for x in lista]

def two_into_one(list1, list2):
    """return two lists into one concatenated"""
    ziped_list = zip(list1,list2)
    return [x.replace("'",'')+' '+y.replace("'",'') for x, y in ziped_list]


def build_df(number):
    #load the history files and return a dataframe from them
    with open('../scraper/days/days'+str(number)+'.txt') as file:
        days = file.read()
    with open('../scraper/horas/horas'+str(number)+'.txt') as file:
        horas = file.read()
    with open('../scraper/names/names'+str(number)+'.txt') as file:
        names = file.read()
    with open('../scraper/price/price'+str(number)+'.txt') as file:
        price = file.read()
    with open('../scraper/winner/winner'+str(number)+'.txt') as file:
        winner = file.read()

    regex = re.compile(r'R\$ \d+,\d{2}')

    days_list = list(map(remove_outter_str,str_into_list(days)[:-1]))
    hours_list = list(map(remove_outter_str,str_into_list(horas)[:-1]))
    names_list = list(map(remove_outter_str,str_into_list(names)[:-1]))
    price_list = re.findall(regex, price)
    winner_list = list(map(remove_outter_str,str_into_list(winner)[:-1]))

    before_datetime = two_into_one(days_list, hours_list)
    df_datetimes = [datetime.strptime(x, '%d/%m/%Y %H:%M:%S') for x in before_datetime]
    starts_list = []
    finish_list = []
    for i, x in enumerate(df_datetimes):
        if i%2 == 0:
            starts_list.append(x)
        else:
            finish_list.append(x)

    df_dict = {'product':names_list,
            'started':starts_list,
            'closed':finish_list,
            'winner':winner_list,
            'price':price_list}

    df = pd.DataFrame(df_dict)
    df.to_csv('./lance_df/lance_df'+str(number)+'.csv')

def wrangling(df_number):
    """takes the csv number adn wrangles the dataframe"""
    df = pd.read_csv('lance_df'+str(df_number)+'.csv') #open df.csv
    del df['Unnamed: 0'] #deletes irrelevant column
    #filters irrelevant products with little data
    common_ser = df['product'].value_counts()[:15]
    df1 = df.set_index('product')
    df2 = df1.join(common_ser, how='inner')
    df2 = df2.reset_index()
    del df2['product']
    #converting strs to datetime object
    df2['started'] = pd.to_datetime(df2['started'])
    df2['closed'] = pd.to_datetime(df2['closed'])
    #time for selling products
    df2['sell_time'] = df2['closed']-df2['started']
    func = lambda x: x.seconds//60
    df2['sell_mins'] = df2['sell_time'].apply(func)
    #adding day pf the week column
    func2 = lambda x: x.strftime('%A')
    df2['day'] = df2.started.apply(func2)
    return df2




def hello():
    print('hello')
