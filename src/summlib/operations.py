import numpy as np
import pkgutil
import xml.etree.ElementTree as ET


def cumsum(array):
    return np.cumsum(array)

def sum(array):
    return np.sum(array)

def readfile():
    data = pkgutil.get_data(__name__,'testfile.xml')
    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    for child in root:
        print(child.tag,child.attrib)
        for subchild in child:
            print(subchild.tag,subchild.text)

