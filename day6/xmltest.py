import xml.etree.ElementTree as ET

tree = ET.parse("test1.xml")
root = tree.getroot()
# for child in root:
#     print(child.tag, child.attrib,child.text)
#     for i in child:
#         print(i.tag,i.attrib,i.text)
for node in root.iter('neighbor'):
    print(node.tag,node.attrib,node.text)
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
#
# tree.write('output.xml')