import pandas as pd
import os

def add_function(nb_1, nb_2, docR='result_addition.csv'):
    """..."""
    result = nb_1 + nb_2
    data = {'Nombre_n1': [nb_1], 'Nombre_n2': [nb_2], 'Resultat': [result]}
    if os.path.isfile(docR):
        df_existante = pd.read_csv(docR)
    else:
        df_existante = pd.DataFrame(columns=['Nombre_n1', 'Nombre_n2', 'Resultat'])
    df = pd.concat([df_existante, pd.DataFrame(data)])
    df.to_csv(docR, index=False)


add_function(25,16)
