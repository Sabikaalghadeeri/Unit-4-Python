# Lab 1:
# movies = [{
#   'movie': 'harry poter',
#   'duration': 120,
#   'stars': 'Daniel Radcliffe, '+'Rubert Grint, '+'Emma Watson'
# },
# {
#   'movie': 'Titanic',
#   'duration': 180,
#   'stars': 'Leonardo Dicaprio, '+'Kate Winslet, '+'Billy Zane'
# },
# {
#   'movie': 'Black Panther',
#   'duration': 120,
#   'stars': 'Chadwick Boseman, '+'Lupita Nyong, '+'Michael B.Jordan'
# }]

# for idx, m in enumerate(movies):
#     print(f"{movies[idx]['movie']} lasts for {movies[idx]['duration']} minutes. Stars: {movies[idx]['stars']}.")




# Lab 2:

dictionaries = [
    {
        'title': 'The True Life',
        'author': 'Sabika',
        'Readed': True
    },
   {
        'title': 'Dreams Falling',
        'author': 'Layla',
        'Readed': True
    },
	{
        'title': 'Hope',
        'author': 'Ranya',
        'Readed': False
    },
]
for book in dictionaries:
	print(f"{book['title']} by {book['author']}")
	if book['Readed'] == True:
		print(f"You already read {book['title']} by {book['author']}")
	else:
		print("not readed yet!")