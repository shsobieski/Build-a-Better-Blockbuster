def simple_rate(df,group,bin_label, measure, threshold,
               save=(False,0)):
    """Draw a plot of success rate given a particular
    threshold."""
    successdf = simple_successdf(df,group, measure, threshold)
    print('Overall Success Rate is: {}'
          .format(round(df['success'].sum()/
                        df['count'].sum(),2)))
    display(successdf[['winrate','lossrate']])

    f, ax = plt.subplots(figsize=(14, 7))

    sns.set_color_codes('colorblind')
    sns.barplot(x='total', y='bin', data=successdf,
                label='Failure', color='r')

    sns.barplot(x='winrate', y='bin', data=successdf,
                label='Success', color='g')

    ax.legend(ncol=2, loc='upper center', frameon=True, 
              framealpha=1, fontsize='small')
    ax.set_title('% of Films Making Over ${} Profit By {}'
                 .format(threshold, bin_label))
    ax.set(ylabel='', xlabel='')
    ax.set_xlim(right=1)
    ax.set_xticks(ticks=[.2, .4, .6, .8, 1])
    ax.set_xticklabels(labels=['20%', '40%', '60%', 
                               '80%', '100%']);
    sns.despine(top=True, right=True, bottom=True)
    if save[0]==True:
        plt.savefig(save[1], bbox_inches='tight', transparent=True)