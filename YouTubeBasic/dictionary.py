# keys can be string or number
monthsConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}
# If key is invalid then monthsConversions['Nov']  will give error
print(monthsConversions['Nov'])

# If key is invalid then monthsConversions.get('Dec')  will give None
print(monthsConversions.get('Dec'))

# Default value for invalid key
print(monthsConversions.get('Dec2', 'Not a valid key'))
