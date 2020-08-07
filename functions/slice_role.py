def slice_role(role, color, save=(False,None)):
    """Draw a plot of top ten people in a role in a particular
    color
    
    kwargs=
    save= (boolean,filename) if true save the plot to the
    filename. default False"""
    temp = movies[(movies['category']==role) 
                  & (movies['status']=='Working')]
     
#Create a dataframe with total box office per person.
    grouped = temp.groupby('primary_name').sum()
    
#Create average rating and profit columns to compare people.
    grouped['averagerating']=(temp.groupby('primary_name')
                              .mean()['averagerating'])
    grouped['averageprofit']=(temp.groupby('primary_name')
                              .mean()['profit'])
    
#Create a column to store people's names for the plot.    
    grouped[role] = sorted(temp['primary_name'].unique())
    
#Filter people whose average films have been 'successful'.    
    grouped = grouped.loc[grouped.loc[:,'averageprofit']
                          >10000000]
    grouped = grouped.loc[grouped.loc[:,'averagerating']
                          >6.3]
    
#Sort by profit and slice the top 10.
    grouped.sort_values('profit', axis=0, 
                        inplace=True, ascending=False)
    grouped = grouped[:10]
    grouped.sort_values('profit', axis=0, inplace=True)

#Plot the results.
    sns.relplot(y=role, x='averagerating', 
                size='averageprofit', sizes=(50,1500), 
                data=grouped, height=6, aspect=1.5, 
                color=color, legend=False)
    plt.title(('10 Most Profitable {}s'
               .format(role)).title())
    plt.xticks(ticks=[6,6.5,7,7.5,8,8.5], 
               labels=[6,6.5,7,7.5,8,8.5])
    plt.ylabel('')
    plt.xlabel('Average Film Rating')
    plt.xlim((6,8.5))
    if save[0]==True:
        plt.savefig(save[1], bbox_inches='tight', transparent=True)