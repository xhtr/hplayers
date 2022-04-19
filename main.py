"""
leer el archivo
pasarlo a un diccionarios
sumar la altura de dos jugadores y luego compararla con la entradas

"""

import json


def open_file(file_name):
    with open(file_name) as player_list:
        player_dic = json.load(player_list)

    return player_dic


def pair_of_players_heights(sum_height, file_name):
    player_dict = open_file(file_name)
    list_height = [int(height['h_in']) for height in player_dict['values']]
    for index, p_height in enumerate(list_height):
        lookup_height = sum_height - p_height
        try:
            second_index = list_height.index(lookup_height)
            first_player = player_dict['values'][second_index]['first_name'] \
                           + ' ' \
                           + player_dict['values'][second_index]['last_name']
            second_player = player_dict['values'][index]['first_name'] \
                            + ' ' \
                            + player_dict['values'][index]['last_name']
            print(f'{ first_player }, { second_player }')
        except:
            pass


if __name__ == '__main__':
    pair_of_players_heights(155, 'playerlist.json')
