def unpack_df(filename, tsv=False, encoding=False):
    """Display the head and info from a csv file.

    Kwargs:
    tsv -- if True sets delimiter to tabs
    encoding --  if True sets encoding to 'latin'"""
    if encoding==True:
        temp_df = pd.read_csv(filename, delimiter='\t', 
                              encoding='latin')
    elif tsv==True:
        temp_df = pd.read_csv(filename, delimiter='\t')
    else:
        temp_df = pd.read_csv(filename)
    print('Info from {}'.format(filename))
    display(temp_df.head())
    display(temp_df.info())
    print('\n\n\n')