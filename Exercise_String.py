#personal message 2.3
name = input()
print(f"Hello {name}")

# NameCase 2.4
print(name.lower(),name.upper(),name.title())

#Famous Quote 2.5
print('Albert Einstein once said, "A person who never made a mistake never tried anything new"')

#Famous Quote2 2.6
famous_person = input()
print(f'{famous_person} once said, "A person who never made a mistake never tried anything new"')

#Stripping Name 2.7 it removes space in start and end of sentence
person_Name = "\tmahdieh\t\nwellcome"
print(person_Name.strip())
print(person_Name.lstrip())
print(person_Name.rstrip())

#File Extension 2.8
file_name = 'sample.txt'
url_name = 'https://www.google.com'
print(file_name.removesuffix(".txt"))
print(url_name.removeprefix('https://'))