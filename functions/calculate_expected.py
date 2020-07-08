def calculate_expected(df, group, bin_label, show_rates=True,
                      save=(False,None)):
    """Draw a plot of expected profit.
    
    kwargs=
    showrates= boolean. if True also shows simplerate function
    output with $0 threshold. default True"""
    if show_rates==True:
        simple_rate(df,group,bin_label, 'profit', 0)

    successdf = simple_successdf(df,group, 'profit', 0)

#Create failed movies and successful movies dataframes.
    losers = df[df['profit']<=0].groupby(group).median()
    winners = df[df['profit']>0].groupby(group).median()
    successdf['medl']=losers['profit']
    successdf['medp']=winners['profit']
    
#Weight the losses and successes by their liklihood.
    successdf['expectedprofit']=((successdf['medl']
                                 *successdf['lossrate'])
                                 +(successdf['medp']
                                   *successdf['winrate']))
    successdf.sort_values('expectedprofit', axis=0, 
                          inplace=True, ascending=False)
    display(successdf[['winrate','lossrate',
                       'expectedprofit']])
    
#Draw the barplot.
    fig, ax2 = plt.subplots(figsize=(14, 7))
    sns.barplot(y='bin', x='expectedprofit', 
                data=successdf, ax=ax2, palette='colorblind')
    sns.despine(top=True, right=True)
    ax2.set_title('Expected Profit by {}'.format(bin_label))
    ax2.set(ylabel='', xlabel='')
    ax2.set_xticks(ticks=[25000000, 75000000, 
                          125000000, 175000000, 225000000])
    ax2.set_xticklabels(labels=['$25 Million', '$75 Million', 
                                '$125 Million', '$175 Million',
                                '$225 Million']);
    if save[0]==True:
        plt.savefig(save[1])