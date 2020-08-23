import numpy as np
import pandas as pd
from preprocessing import clean

data = pd.read_csv('../scrapping/raw_data/evaluation_data.csv')
data = data.drop(data.columns[0], axis=1).drop_duplicates(subset='ArtText').dropna().reset_index(drop=True)
data = data[~data['ArtText'].str.contains('Please enable cookies on your web browser in order to continue.')].reset_index(drop=True)
data['label'] = np.where((data['Democrat_Vote'] == 'Neutral') & (data['Republican_Vote'] == 'Neutral'), 0, 1)
data['Text'] = data['ArtTitle'] + ' ' + data['ArtText'] + ' ' + data['ArtSummary']

with open('./evaluation_data.csv', 'w') as f:
    f.write('text,label\n')
    for i, line in enumerate(data['Text']):
        f.write('{},{}\n'.format(clean(line), data['label'][i]))
f.close()
