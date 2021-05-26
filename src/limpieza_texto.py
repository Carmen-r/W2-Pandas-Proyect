def replace(datafr, regex_countries, to_change, new_colum, old_column):
    datafr[new_column] = datafr[old_column].str.lower().replace(regex_countries, to_change, regex=True)
    return datafr


def create(df,column,list_):
    return df[df[column].isin(list_)]
    
def months(patron, string):
    import re
    try:
        return re.search(patron, string).group().lower()
    except:
        return f"Error"
