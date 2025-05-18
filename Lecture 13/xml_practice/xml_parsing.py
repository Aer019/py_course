import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)

print("My books:\n")
for book in root:
    print('Title: ', book.attrib['title'])
    print('Author: ', book[0].text)
    print('Year: ', book[1].text, '\n')

for author in root.iter('author'):
    print(author.text)

for book in root.findall('book'):
    print(book.get('title'))

print(root.find('book').get('title'))
