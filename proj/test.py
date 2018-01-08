import pandas

import seaborn as sns
import matplotlib.pyplot as plt
def plot_heatmap_null(meta,savepath='cleaned_heat_map.jpg'):
    heat_map=sns.heatmap(meta.isnull(), yticklabels=False, xticklabels=True,cbar=False)
    plt.xticks(rotation='horizontal', size=8)
    heat_map.get_figure().savefig(savepath)
def fill_nan(meta,row,groupbycolumn):
    #plot_heatmap_null(meta)
    #for x in meta['source_screen_name'].isnull():
    #    print(x.index)
    #meta['source_screen_name'].iloc[a.loc[a][0]]
    tempdf=meta[[row, groupbycolumn]].dropna()
    fill_in_values = tempdf.groupby(groupbycolumn).apply(lambda x: x.mode()).dropna()
    print('Fill in Value computation done')
    nullcount=meta[row].isnull()
    index_null=meta[groupbycolumn][nullcount.loc[nullcount]._index._data]._index._data
    print('Finding nan index done')
    key_null=list(meta[groupbycolumn].iloc[index_null]._values)
    #meta['source_screen_name'].iloc[index_null] = meta['msno'][nullcount.loc[nullcount]._index._data]._index._data
    #print(fill_in_values['msno'])
    l=len(index_null)
    delidx=[]
    cnt2=0
    print('Start looping to fill in the values')
    for i in index_null:
        cnt2+=1
        if meta[groupbycolumn].iloc[i] not in fill_in_values._values[:,1]:
            #meta=meta.drop(i)
            delidx.append(i)
            pass
        else:
            meta[row].iloc[i]=fill_in_values.loc[meta[groupbycolumn].iloc[i]][row].real[0]
        if not cnt2%100:
            print('This is the ',cnt2,' th nan element being processed','total: ', l, 'process: ',cnt2/l*100, '%')
    #'yp6A/uxyh/0D2+D177JVzWcruMfNzVr6l19bsssb3XY='
    #deta=meta.drop(delidx)
    meta.drop(delidx, inplace=True)
    meta.reset_index(inplace=True)
    meta.drop(['index'], axis=1, inplace=True)
    return meta
    #fill_in_values=meta[['source_screen_name','msno']].groupby('msno').agg(lambda x:x.value_counts().index[0])
if __name__=='main':
    meta=pandas.read_csv(r'D:\Learning\Graduate\isye412\p\train.csv')## for test
    #meta.info()
    print(meta.head())
    #from sklearn.preprocessing import LabelEncoder
    #le=LabelEncoder()
    rev_row_list=['source_screen_name','source_system_tab','source_type']
    #delidx=[]
    cnt=0
    for i in rev_row_list:
        cnt+=1
        print('This is currently ',i,' the ',cnt ,'th cloumn, total 3' )
        meta=fill_nan(meta,i,'msno')
    meta.to_csv('clean_train.csv')
    plot_heatmap_null(meta)
    plt.show()
    pass
'''https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.mode.html
Note that there could be multiple values returned for the selected axis (when more than one item share the maximum frequency),
which is the reason why a dataframe is returned. If you want to impute missing values with the mode in a dataframe df,
you can just do this: df.fillna(df.mode().iloc[0])'''