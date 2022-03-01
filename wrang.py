from functions import str_into_list
from functions import build_df
import re

with open('../scraper/days/days'+str(1)+'.txt') as file:
    days = file.read()
with open('../scraper/horas/horas'+str(1)+'.txt') as file:
    horas = file.read()
with open('../scraper/names/names'+str(1)+'.txt') as file:
    names = file.read()
with open('../scraper/price/price'+str(1)+'.txt') as file:
    price = file.read()
with open('../scraper/winner/winner'+str(1)+'.txt') as file:
    winner = file.read()





def remove_outter_str(str):
    return str.strip('\'')

#days_list = list(map(remove_outter_str,str_into_list(days)[:-1]))
#hours_list = list(map(remove_outter_str,str_into_list(horas)[:-1]))
#names_list = list(map(remove_outter_str,str_into_list(names)[:-1]))
#price_list = list(map(remove_outter_str,str_into_list(price)[:-1]))
#winner_list = list(map(remove_outter_str,str_into_list(winner)[:-1]))




if __name__ == '__main__':

    #print(remove_outter_str(price))
    #print(price)
    #print(type(remove_outter_str(price)))
    #print(len(winner_list))
    #print(type(price_lista_lista))
    build_df(1)
