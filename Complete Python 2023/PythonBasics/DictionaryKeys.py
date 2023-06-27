# Dictionary

# Dictionary keys must have unique properties and are immutable
# Keys are usually something descriptive like a string


dictionary = {
  123: [1,2,3],
  123: 'hello',
  '[100]': True
}

print(dictionary['[100]'])

print(dictionary[123]) # not a unique key! This actually overwrites the first key.