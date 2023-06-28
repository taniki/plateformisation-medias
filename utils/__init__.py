import pandas as pd

def format_index_siren(style):
    return (
        style
        .format_index(lambda siren: f'<a href="https://annuaire-entreprises.data.gouv.fr/entreprise/{siren}">{siren}</a>')        
    )

def format_table(df):
    return (
        df
        .style
        .format(thousands = " ", precision = 0)
    )

def format_percent(style):
    return (
        style
        .format('{:,.1%}'.format)
    )