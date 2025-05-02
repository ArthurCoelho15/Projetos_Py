"""

HackerRank: https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

Faça um programa que leia um horário no formato 0-12AM/PM e tranforme para o formato 24h
    - Ex: Input -> 07:01:00PM
        - Output -> 19:01:00

"""

dict_pm = {'01': '03', '02': '14', '03': '15', '04': '16', '05': '17', '06': '18', '07': '19', '08': '20', '09': '21', '10': '22', '11': '23', '12': '12', }
dict_am = {'12': '00', '13': '01', '14': '02', '15': '03', '16': '04', '17': '05', '18': '06', '19': '07', '20': '08', '21': '09', '22': '10', '23': '11', }

time = list(map(str,input().split(':')))

def conversor(time):
    if 'PM' in time[2]:
        time[0] = dict_pm.get(time[0])
        print(f'{time[0]}:{time[1]}:{time[2][0:2]}')
    else:
        if time[0] in dict_am.keys():
            time[0] = dict_am.get(time[0])
            print(f'{time[0]}:{time[1]}:{time[2][0:2]}')
        else:
            print(f'{time[0]}:{time[1]}:{time[2][0:2]}')

conversor(time)