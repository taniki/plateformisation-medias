import pandas as pd

def format_table(df):
    return (
        df
        .style
        .format_index(lambda siren: f'<a href="https://annuaire-entreprises.data.gouv.fr/entreprise/{siren}">{siren}</a>')
        .format(thousands = " ", precision = 0)
    )