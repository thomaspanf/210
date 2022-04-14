#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("EuCitiesTemperatures.csv", header=0)
df
# %%
#Preprocessing/Analysis
#1
df[['latitude', 'longitude']] = df.groupby(['country'], sort=False)[['latitude', 'longitude']].apply(lambda x: x.fillna(round(x.mean(axis=0),2))).droplevel('country')
df
# %%
#2
df.loc[(df['latitude'] >=40) & (df['latitude'] <=60) & (df['longitude'] >=15) & (df['longitude'] <=30)]['city']
# %%
#2
filtered_series = df.loc[(df['latitude'] >=40) & (df['latitude'] <=60) & (df['longitude'] >=15) & (df['longitude'] <=30)].groupby(['country']).apply(lambda x: len(x))
filtered_series.loc[filtered_series == filtered_series.max()]
# %%
#3
df.loc[(df['EU'] == 'yes') & (df['coastline'] == 'yes'), ['region_type']] = 'Coastal EU Country'
df.loc[(df['EU'] == 'yes') & (df['coastline'] == 'no'), ['region_type']] = 'Non-Coastal EU Country'
df.loc[(df['EU'] == 'no') & (df['coastline'] == 'no'), ['region_type']] = 'Non-Coastal Non-EU Country'
df.loc[(df['EU'] == 'no') & (df['coastline'] == 'yes'), ['region_type']] = 'Coastal Non-EU Country'
df['temperature'] = df.groupby(['region_type'], sort = False)['temperature'].apply(lambda x: x.fillna(x.mean(axis=0)))
df.drop(['region_type'], axis = 1)
# %%
#Visualization
#1
df.groupby(['region_type'], sort = True)['city'].apply(lambda x: len(x)).plot(kind='bar')
#df = df.drop(['region_type'], axis = 1)
plt.show()
# %%
#2
color_map = df['country'].drop_duplicates().to_frame()
color_map['color'] = [np.random.rand(3) for country in df['country'].drop_duplicates()]
color_map.set_index('country', inplace=True)
df.plot(x='longitude', y='latitude', kind='scatter', c=pd.merge(df, color_map, left_on='country', right_index=True)['color'])
plt.show()
# %%
#3
df['population'].drop_duplicates().plot(kind='hist',bins=5)
plt.show()
#do we need to show each group's label
# %%
#4
fig, axes = plt.subplots(2,2)
fig.tight_layout(pad=3.0)

df.loc[df['temperature'] > 10, 'color'] = 'red'
df.loc[df['temperature'] < 6, 'color'] = 'blue'
df.loc[(df['temperature'] >= 6) & (df['temperature'] <= 10), 'color'] = 'orange'

regions = list(df['region_type'].drop_duplicates())
cnt = 0
for i in range(0, 2):
    for j in range(0, 2):
        region_df = df.loc[df['region_type'] == regions[cnt]]
        axes[i,j].scatter(region_df['latitude'], region_df['longitude'], color = region_df['color'])
        axes[i,j].set_title(regions[cnt])
        cnt +=1

plt.show()
# %%
