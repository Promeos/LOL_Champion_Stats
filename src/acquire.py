



lol = requests.get('http://ddragon.leagueoflegends.com/cdn/11.15.1/data/en_US/champion.json')

data = json.loads(lol.text).get('data', None)
champion_names = list(data.keys())

df_stats = pd.DataFrame()

for champion in champion_names:

    champ_stats = pd.Series(data[champion]['stats']).to_frame(name=champion)
    df_stats = pd.concat([df_stats, champ_stats], axis=1)

df_stats = df_stats.T
df_stats.reset_index().rename(columns={'index': 'champion'}, inplace=True)