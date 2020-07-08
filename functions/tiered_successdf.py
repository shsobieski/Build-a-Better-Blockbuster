def tiered_successdf(df,group):
    """Create a dataframe for success by profit tier."""
    df['count']=1
    
#Create columns that track success.
    df.loc[df.loc[:,'profit']
            >= 100000000, 'BB']=True
    df.loc[(df.loc[:,'profit']
            >= 10000000)
            &(df.loc[:,'profit']
            <100000000), 'HT']=True
    df.loc[(df.loc[:,'profit']
            > 0)
            &(df.loc[:,'profit']
            <10000000), 'FP']=True
    df.loc[df.loc[:,'profit']
            <= 0, 'FL']=True
    df.fillna(False, inplace=True)
        
#Create columns with a rate of each success level.
    successdf = (df[['BB', 'HT', 'FP', 
                    'FL', group, 'count']]
                    .groupby(group).sum())
    successdf['blockrate'] = round(successdf['BB']
                                   /successdf['count'],2)
    successdf['hitrate'] = round(successdf['HT']
                                    /successdf['count'],2)
    successdf['floprate'] = round(successdf['FP']
                                    /successdf['count'],2)
    successdf['failrate'] = round(successdf['FL']
                                    /successdf['count'],2)
    
#Add columns for the graph.
    successdf['bin']=sorted(df[group].unique())
    successdf['fail']= 1
    successdf['flop']= (successdf.loc[:,'hitrate']
                        +successdf.loc[:,'floprate']
                        +successdf.loc[:,'blockrate'])
    successdf['hit']= (successdf.loc[:,'hitrate']
                        +successdf.loc[:,'blockrate'])
    successdf['block']= successdf.loc[:,'blockrate']
    successdf.sort_values('blockrate', axis=0, 
                            ascending=False, inplace=True)
    return successdf