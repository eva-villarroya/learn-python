from xml.dom import minidom
import csv

# parse an xml file by name
mydoc = minidom.parse('mapa-pared.xml')

entries = mydoc.getElementsByTagName('entry')

print('Items found: ')
print(entries.length)

count = 1

rows = []

for entry in entries:
    categories = entry.getElementsByTagName('category')

    for category in categories:

        print("Category: ")
        print(category.getAttribute('term'))

        if category.getAttribute('term') == 'http://schemas.google.com' \
                                            '/blogger/2008/kind#post':

            value = entry.getElementsByTagName('title').item(0)\
             .firstChild.nodeValue

            print('Post found:')
            print(value)

            row = [count, value]
            rows.append(row)
            count = count + 1


csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
with open('export.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in rows:
        writer.writerow(row)

f.close()
