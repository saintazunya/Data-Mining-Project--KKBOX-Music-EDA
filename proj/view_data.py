import pandas as pd
cleaned=pd.read_csv(r'D:\Learning\Graduate\isye412\p\cleaned.csv')## for test
cleaned.info()
print(cleaned.head())
print('---------------------phase one done-------------------------')
import seaborn as sns
#from test import plot_heatmap_null
from sklearn.preprocessing import LabelEncoder
#plot_heatmap_null(cleaned)
songname=pd.read_csv(r'D:\Learning\Graduate\isye412\p\song_extra_info_2.csv')
songname.info()
print(songname.head())
new=pd.merge(cleaned, songname, on='song_id',how='left')
new.info()
print(new.head())
print('----------phase two done -----------')
user=pd.read_csv(r'D:\Learning\Graduate\isye412\p\members.csv')
all=pd.merge(new,user,on='msno',how='left')
all.to_csv(r'D:\Learning\Graduate\isye412\p\merged.csv',encoding ='utf-8')
all.info()
print(all.head())
pass