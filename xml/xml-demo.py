import xml.etree.ElementTree as ET

data = ET.parse('1.xml')
root = data.getroot()

ele = root.findall('.//branches/hudson.plugins.git.BranchSpec/name')

for e in ele:
    print(e.text)

