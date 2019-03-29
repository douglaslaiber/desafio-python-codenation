# -*- coding: utf-8 -*-
import collections
import csv

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.


with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    csv_dataset = list(csv_reader)


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
def q_1():
    nationality_column_index = csv_header.index('nationality')
    nationality_list = []

    for row in csv_dataset:
        if row[nationality_column_index] not in nationality_list:
            nationality_list.append(row[nationality_column_index])

    return len(nationality_list)


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    club_column_index = csv_header.index('club')
    club_list = []

    for row in csv_dataset:
        if row[club_column_index] not in club_list:
            club_list.append(row[club_column_index])

    return len(club_list)


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    full_name_column_index = csv_header.index('full_name')
    players_list = [row[full_name_column_index] for row in csv_dataset[:20]]

    return players_list


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    full_name_column_index = csv_header.index('full_name')
    eur_wage_column_index = csv_header.index('eur_wage')
    csv_dataset.sort(key=lambda x: float(x[eur_wage_column_index]), reverse=True)

    players_list = [row[full_name_column_index] for row in csv_dataset[:10]]
    return players_list


# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    full_name_column_index = csv_header.index('full_name')
    age_column_index = csv_header.index('age')
    csv_dataset.sort(key=lambda x: float(x[age_column_index]), reverse=True)

    players_list = [row[full_name_column_index] for row in csv_dataset[:10]]
    return players_list


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    age_column_index = csv_header.index('age')

    age_list = [row[age_column_index] for row in csv_dataset]

    count_ages_dict = {}
    for key, value in collections.Counter(age_list).items():
        count_ages_dict[int(key)] = value

    return count_ages_dict
