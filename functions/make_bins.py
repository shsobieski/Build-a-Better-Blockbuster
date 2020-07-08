def make_bins(df, col, cat, bin_names=[]):
    """Create 5 categorical bins based on quantile.
    
    kwargs= 
    bin_names= list of names for each category from highest
    rating to lowest"""
    df.loc[df.loc[:,col] > (round(df.loc[:,col]
                                 .quantile(.8),2)),
           cat]=bin_names[0]
    df.loc[(df.loc[:,col] > (round(df.loc[:,col]
                                  .quantile(.6),2))) 
                 &(df.loc[:,col]<=(round(df.loc[:,col]
                                         .quantile(.8),2))),
           cat]= bin_names[1]
    df.loc[(df.loc[:,col] > round(df.loc[:,col]
                                  .quantile(.4),2)) 
                 &(df.loc[:,col]<=round(df.loc[:,col]
                                        .quantile(.6),2)), 
           cat]= bin_names[2]
    df.loc[(df.loc[:,col] > round(df.loc[:,col]
                                  .quantile(.2),2)) 
                 &(df.loc[:,col]<=round(df.loc[:,col]
                                        .quantile(.4),2)), 
           cat]= bin_names[3]
    df.loc[df.loc[:,col] < round(df.loc[:,col]
                                 .quantile(.2),2),
           cat]=bin_names[4]