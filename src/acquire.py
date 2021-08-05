import pandas as pd
import requests
import json
import os


def load_champion_base_stats():
    '''
    League of Legends champion base stats: Patch 11.15

    Parameters
    ----------
    None

    Returns
    -------
    dataset :  pandas.core.DataFrame
        A dataframe of champion base stats from League of Legends
    '''
    filename = './data/champ_stats.csv'

    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        lol = requests.get('http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion.json')

        stats = json.loads(lol.text).get('data', None)
        champion_names = list(stats.keys())
        dataset = pd.DataFrame()

        for champion in champion_names:

            champ_stats = pd.Series(stats[champion]['stats']).to_frame(name=champion)
            dataset = pd.concat([dataset, champ_stats], axis=1)

        dataset = dataset.T
        dataset = dataset.reset_index().rename(columns={'index': 'champion'})
        dataset.to_csv(filename, index=False)
        return dataset