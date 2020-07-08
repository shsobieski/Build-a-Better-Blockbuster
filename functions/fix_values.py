def fix_values(df, col):
    """Convert strings with , and $ to integers."""
    broken_values = [value for value in df[col]]
    fixed_values = []
    for value in broken_values:
        fixed_values.append(int(value.replace(',','')
                                .replace('$','')))
    df[col] = fixed_values