def cat_box(df, col, xcol, cat, xlabel, ticks, 
            labels, bin_names=[], 
            omitfliers=True, save=(False, 0)):
    """Plot numerical data in 5 bins based on quantile.
    
    kwargs=
    bin_names= list of names for each category from highest
    rating to lowest
    
    omitfliers= boolean, if True omits outliers from plot,
    default True
    
    save= (boolean, str) if True saves figure to file"""
    make_bins(df,col,cat,bin_names)
    if omitfliers==True:
        sns.catplot(y=cat, x=xcol, data=df, kind='box', 
                    order=bin_names,height=7, aspect=2, 
                    palette='colorblind', showfliers=False)
        plt.xlabel('')
        plt.ylabel('')
        plt.xticks(ticks=ticks,labels=labels)
        plt.title(('Quartiles of {} by {}'
                  .format(xlabel,cat)));
        if save[0]==True:
            plt.savefig(save[1])
    else:
        sns.catplot(y=cat, x=xcol, data=df, kind='box', 
                    order=bin_names,height=7, aspect=2, 
                    palette='colorblind', showfliers=True)
        plt.xlabel('')
        plt.ylabel('')
        plt.xticks(ticks=ticks,labels=labels)
        plt.title(('Quartiles of {} by {}'
                  .format(xlabel,cat)));
        if save[0]==True:
            plt.savefig(save[1])