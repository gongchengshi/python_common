from titlecase import titlecase

standard_country_names = {
    'brasil': 'Brazil',
    'usa': 'USA',
    'united states of america': 'USA',
    'us': 'USA',
    'united states': 'USA'
}


def normalize_country(name):
    return standard_country_names.get(name.lower(), titlecase(name))
