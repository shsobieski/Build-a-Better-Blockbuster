def get_prop(yrlist):
    """Print proportion of foreign/wide gross 
    for 5 year span"""
    frn = trends[(trends['year']==yrlist[0])|
                 (trends['year']==yrlist[1])|
                 (trends['year']==yrlist[2])|
                 (trends['year']==yrlist[3])|
                 (trends['year']==yrlist[4])][
        'adj_frn_gross'].mean()
    wide = trends[(trends['year']==yrlist[0])|
                  (trends['year']==yrlist[1])|
                  (trends['year']==yrlist[2])|
                  (trends['year']==yrlist[3])|
                  (trends['year']==yrlist[4])][
    'adj_wide_gross'].mean()
    print('{}-{} proportion wide gross from frn box: {}'
          .format(yrlist[0], yrlist[4], round(frn/wide,2)))