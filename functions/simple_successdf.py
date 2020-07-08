def simple_successdf(df,group, measure, threshold):
    """Create a dataframe containing success and failure
    rate given a threshold for success."""
    df.loc[df[measure]> threshold, 'success']=True
    df.loc[df[measure]<= threshold, 'success']=False
    df['count']=1
    successdf = (df[['success', group, 'count']]
                 .groupby(group).sum())
    successdf['winrate'] = round(successdf['success']
                                 /successdf['count'],2)
    successdf['lossrate'] = 1 - successdf['winrate']
    
#Add columns for the graph.
    successdf['bin']=sorted(df[group].unique())
    successdf['total']=(successdf['winrate']
                        +successdf['lossrate'])
    successdf.sort_values('winrate', axis=0, 
                          ascending=False, inplace=True)
    return successdf