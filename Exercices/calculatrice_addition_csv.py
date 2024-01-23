import os
import pandas as pd

def add_to_csv(nb_1, nb_2, doc_result='result_addition.csv'):
    """..."""
    result = nb_1 + nb_2
    data = {'Nombre_n1': [nb_1], 'Nombre_n2': [nb_2], 'Resultat': [result]}
    if os.path.isfile(doc_result):
        df_existante = pd.read_csv(doc_result)
    else:
        df_existante = pd.DataFrame(columns=['Nombre_n1', 'Nombre_n2', 'Resultat'])
    df = pd.concat([df_existante, pd.DataFrame(data)])
    df.to_csv(doc_result, index=False)


add_to_csv(25,16)
