import pandas as pd
mobilier = pd.read_json('./mobiliers_et_emprises_au_sol_de_signalisation_routiere_et_pietonne_-_donnees_geo.json', 'r')


feux = pd_items.loc[(pd_items['libelle_ft_style'] == 24) | (pd_items['libelle_ft_style'] == 25) | (pd_items['libelle_ft_style'] == 0) | (pd_items['libelle_ft_style'] == 5), :]

def parse_geometry(geo):
    # We take the 4th couple to avoid xml markup characters.
    str_couple = geo.split(',0')[4]
    return tuple([float(long_or_lat) for long_or_lat in str_couple.split(',')])

feux.geometry.apply(parse_geometry)
cleaned_feux = feux.copy(deep=True)
cleaned_feux['longitude'] = cleaned_feux.geometry.apply(lambda x: parse_geometry(x)[0])
cleaned_feux['latitude'] = cleaned_feux.geometry.apply(lambda x: parse_geometry(x)[1])

cleaned_feux.get(['longitude', 'latitude']).to_csv('./feux.csv')

