def tiered_rates(df,group,bin_label, save=(False,None)):
    """Draw a plot of tiered success dataframe."""
    successdf = tiered_successdf(df,group)

    f, ax = plt.subplots(figsize=(14, 7))

    sns.set_color_codes('colorblind')
    sns.barplot(x='fail', y='bin', data=successdf,
                label='Failure', color='r')
    
    sns.barplot(x='flop', y='bin', data=successdf,
                label='Flop', color='orange')
    
    sns.barplot(x='hit', y='bin', data=successdf,
                label='Hit', color='b')

    sns.barplot(x='block', y='bin', data=successdf,
                label='Blockbuster', color='g')
    
    ax.set_title('Profit Outcomes by {}'.format(bin_label))
    ax.set_xlim(right=1)
    ax.legend(ncol=4, loc='upper center', 
              frameon=True, framealpha=1, fontsize='x-small')
    ax.set(ylabel='', xlabel='')
    ax.set_xticks(ticks=[.2, .4, .6, .8, 1])
    ax.set_xticklabels(labels=['20%', '40%', '60%', 
                               '80%', '100%']);
    sns.despine(top=True, right=True, bottom=True)
    if save[0]==True:
        plt.savefig(save[1], bbox_inches='tight', transparent=True)