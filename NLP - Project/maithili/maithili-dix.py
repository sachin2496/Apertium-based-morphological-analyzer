import xml.etree.ElementTree as ET
root = ET.Element('dictionary')

sdef_section = '''
    <sdefs>
    <sdef n="n"       c="Noun"/>
    <sdef n="sg"       c="Singular"/>
    <sdef n="pl"       c="Plural"/>
    <sdef n="m"       c="Masculine"/>   
    <sdef n="f"       c="Feminine"/>   
    <sdef n="o"       c="Oblique"/>
    <sdef n="d"       c="Direct"/>
    <sdef n="p3"       c="Third Person"/>
    <sdef n="p2"       c="Second Person"/>
    <sdef n="p1"       c="First Person"/>
    <sdef n="adj"       c="Adjective"/>
  </sdefs>
'''
e1 = ET.SubElement(root,'alphabet')

e1.text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

e2 = ET.fromstring(sdef_section)
root.append(e2)
pardefs = ET.SubElement(root,'pardefs')
def func_noun_entry_wleft(x,l_text,r_text,n1,n2,n3,n4,n5):
    e1 = ET.SubElement(x,'e')
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    l.text = l_text
    r = ET.SubElement(p1,'r')
    r.text = r_text
    s1 = ET.SubElement(r,'s',n=n1)
    s2 = ET.SubElement(r,'s',n=n2)
    s3 = ET.SubElement(r,'s',n=n3)
    s4 = ET.SubElement(r,'s',n=n4)
    s5 = ET.SubElement(r,'s',n=n5)

def func_noun_entry_left(x,l_text,r_text,n1,n2,n3,n4,n5,n6):
    e1 = ET.SubElement(x,'e')
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    l.text = l_text
    r = ET.SubElement(p1,'r')
    r.text = r_text
    s1 = ET.SubElement(r,'s',n=n1)
    s2 = ET.SubElement(r,'s',n=n2)
    s3 = ET.SubElement(r,'s',n=n3)
    s4 = ET.SubElement(r,'s',n=n4)
    s5 = ET.SubElement(r,'s',n=n5)
    s6 = ET.SubElement(r,'s',n=n6)
    
def func_adj_entry(x,l_text,r_text,n1,n2,n3,n4,n5):
    e1 = ET.SubElement(x,'e')
    p1 = ET.SubElement(e1,'p')
    l = ET.SubElement(p1,'l')
    l.text = l_text
    r = ET.SubElement(p1,'r')
    r.text = r_text
    s1 = ET.SubElement(r,'s',n=n1)
    s2 = ET.SubElement(r,'s',n=n2)
    s3 = ET.SubElement(r,'s',n=n3)
    s4 = ET.SubElement(r,'s',n=n4)
    s5 = ET.SubElement(r,'s',n=n5)

pardef5 = ET.SubElement(pardefs,'pardef',n='')
func_adj_entry(pardef5, '',"bAlikA", 'n','f','sg','p3','d')
func_adj_entry(pardef5, '',"", 'n','f','pl','p3','d')

pardef6 = ET.SubElement(pardefs,'pardef',n='')
func_noun_entry_wleft(pardef6, '',"ladZikio", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef6, '',"ladZikiosaBa", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef6, '',"ladZikio", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef6, '',"", 'n','f','pl','p3','o')

pardef7 = ET.SubElement(pardefs,'pardef',n='')
func_adj_entry(pardef7, '',"bAlaka", 'adj','m','sg','p3','d')
func_adj_entry(pardef7, '',"", 'adj','m','pl','p3','d')

pardef8 = ET.SubElement(pardefs,'pardef',n='Gare')
func_noun_entry_wleft(pardef8, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef8, '',"Msaba", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef8, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef8, '',"Msaba", 'n','m','pl','p3','o')

pardef9 = ET.SubElement(pardefs,'pardef',n='ladZikahi')
func_noun_entry_wleft(pardef9, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef9, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef9, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef9, '',"saBa", 'n','m','pl','p3','o')

pardef10 = ET.SubElement(pardefs,'pardef',n='rAj')
func_noun_entry_wleft(pardef10, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef10, '',"ahisaBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef10, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef10, '',"ahisaBa", 'n','m','pl','p3','o')

pardef11 = ET.SubElement(pardefs,'pardef',n='Karce')
func_noun_entry_wleft(pardef11, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef11, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef11, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef11, '',"saBa", 'n','m','pl','p3','o')

pardef12 = ET.SubElement(pardefs,'pardef',n='sonare')
func_noun_entry_wleft(pardef12, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef12, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef12, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef12, '',"saBa", 'n','m','pl','p3','o')

pardef13 = ET.SubElement(pardefs,'pardef',n='kuve')
func_noun_entry_wleft(pardef13, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef13, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef13, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef13, '',"saBa", 'n','m','pl','p3','o')

pardef14 = ET.SubElement(pardefs,'pardef',n='kavie')
func_noun_entry_wleft(pardef14, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef14, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef14, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef14, '',"saBa", 'n','m','pl','p3','o')

pardef15 = ET.SubElement(pardefs,'pardef',n='Axamie')
func_noun_entry_wleft(pardef15, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef15, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef15, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef15, '',"saBa", 'n','m','pl','p3','o')

pardef16 = ET.SubElement(pardefs,'pardef',n='sawrue')
func_noun_entry_wleft(pardef16, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef16, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef16, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef16, '',"saBa", 'n','m','pl','p3','o')

pardef17 = ET.SubElement(pardefs,'pardef',n='allue')
func_noun_entry_wleft(pardef17, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef17, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef17, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef17, '',"saBa", 'n','m','pl','p3','o')

pardef18 = ET.SubElement(pardefs,'pardef',n='suve')
func_noun_entry_wleft(pardef18, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef18, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef18, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef18, '',"saBa", 'n','m','pl','p3','o')

pardef19 = ET.SubElement(pardefs,'pardef',n='harahuze')
func_noun_entry_wleft(pardef19, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef19, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef19, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef19, '',"saBa", 'n','m','pl','p3','o')

pardef20 = ET.SubElement(pardefs,'pardef',n='kroXe/kroXahi/kroXahiz')
func_noun_entry_wleft(pardef20, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef20, '',"", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef20, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef20, '',"", 'n','m','pl','p3','o')

pardef21 = ET.SubElement(pardefs,'pardef',n='sarisoMe')
func_noun_entry_wleft(pardef21, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef21, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef21, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef21, '',"saBa", 'n','m','pl','p3','o')

pardef22 = ET.SubElement(pardefs,'pardef',n='lakaToe')
func_noun_entry_wleft(pardef22, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef22, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef22, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef22, '',"saBa", 'n','m','pl','p3','o')

pardef23 = ET.SubElement(pardefs,'pardef',n='gosaiMe')
func_noun_entry_wleft(pardef23, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef23, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef23, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef23, '',"saBa", 'n','m','pl','p3','o')

pardef24 = ET.SubElement(pardefs,'pardef',n='Garave')
func_noun_entry_wleft(pardef24, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef24, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef24, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef24, '',"saBa", 'n','m','pl','p3','o')

pardef25 = ET.SubElement(pardefs,'pardef',n='ladZikabe')
func_noun_entry_wleft(pardef25, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef25, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef25, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef25, '',"saBa", 'n','m','pl','p3','o')

pardef26 = ET.SubElement(pardefs,'pardef',n='rajave')
func_noun_entry_wleft(pardef26, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef26, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef26, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef26, '',"saBa", 'n','m','pl','p3','o')

pardef27 = ET.SubElement(pardefs,'pardef',n='Karcave')
func_noun_entry_wleft(pardef27, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef27, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef27, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef27, '',"saBa", 'n','m','pl','p3','o')

pardef28 = ET.SubElement(pardefs,'pardef',n='kaviye')
func_noun_entry_wleft(pardef28, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef28, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef28, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef28, '',"saBa", 'n','m','pl','p3','o')

pardef29 = ET.SubElement(pardefs,'pardef',n='axamiye')
func_noun_entry_wleft(pardef29, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef29, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef29, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef29, '',"saBa", 'n','m','pl','p3','o')

pardef30 = ET.SubElement(pardefs,'pardef',n='sonarave')
func_noun_entry_wleft(pardef30, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef30, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef30, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef30, '',"saBa", 'n','m','pl','p3','o')

pardef31 = ET.SubElement(pardefs,'pardef',n='sawruve')
func_noun_entry_wleft(pardef31, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef31, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef31, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef31, '',"saBa", 'n','m','pl','p3','o')

pardef32 = ET.SubElement(pardefs,'pardef',n='allUbe')
func_noun_entry_wleft(pardef32, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef32, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef32, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef32, '',"saBa", 'n','m','pl','p3','o')

pardef33 = ET.SubElement(pardefs,'pardef',n='kuvazve')
func_noun_entry_wleft(pardef33, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef33, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef33, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef33, '',"saBa", 'n','m','pl','p3','o')

pardef34 = ET.SubElement(pardefs,'pardef',n='gehuzve')
func_noun_entry_wleft(pardef34, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef34, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef34, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef34, '',"saBa", 'n','m','pl','p3','o')

pardef35 = ET.SubElement(pardefs,'pardef',n='kroXave/kroXavahi/kroXavahiz')
func_noun_entry_wleft(pardef35, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef35, '',"", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef35, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef35, '',"", 'n','m','pl','p3','o')

pardef36 = ET.SubElement(pardefs,'pardef',n='suwave')
func_noun_entry_wleft(pardef36, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef36, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef36, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef36, '',"saBa", 'n','m','pl','p3','o')

pardef37 = ET.SubElement(pardefs,'pardef',n='gosaiMyahi')
func_noun_entry_wleft(pardef37, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef37, '',"Msaba", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef37, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef37, '',"Msaba", 'n','m','pl','p3','o')

pardef38 = ET.SubElement(pardefs,'pardef',n='sarisoMbe')
func_noun_entry_wleft(pardef38, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef38, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef38, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef38, '',"saBa", 'n','m','pl','p3','o')

pardef39 = ET.SubElement(pardefs,'pardef',n='Garavo')
func_noun_entry_wleft(pardef39, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef39, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef39, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef39, '',"saBa", 'n','m','pl','p3','o')

pardef40 = ET.SubElement(pardefs,'pardef',n='ladZikavo')
func_noun_entry_wleft(pardef40, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef40, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef40, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef40, '',"saBa", 'n','m','pl','p3','o')

pardef41 = ET.SubElement(pardefs,'pardef',n='rajavo')
func_noun_entry_wleft(pardef41, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef41, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef41, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef41, '',"saBa", 'n','m','pl','p3','o')

pardef42 = ET.SubElement(pardefs,'pardef',n='Karcavo')
func_noun_entry_wleft(pardef42, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef42, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef42, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef42, '',"saBa", 'n','m','pl','p3','o')

pardef43 = ET.SubElement(pardefs,'pardef',n='kaviyo')
func_noun_entry_wleft(pardef43, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef43, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef43, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef43, '',"saBa", 'n','m','pl','p3','o')

pardef44 = ET.SubElement(pardefs,'pardef',n='axamiyo')
func_noun_entry_wleft(pardef44, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef44, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef44, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef44, '',"saBa", 'n','m','pl','p3','o')

pardef45 = ET.SubElement(pardefs,'pardef',n='sonaravo')
func_noun_entry_wleft(pardef45, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef45, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef45, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef45, '',"saBa", 'n','m','pl','p3','o')

pardef46 = ET.SubElement(pardefs,'pardef',n='sawruvo')
func_noun_entry_wleft(pardef46, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef46, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef46, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef46, '',"saBa", 'n','m','pl','p3','o')

pardef47 = ET.SubElement(pardefs,'pardef',n='allUbo')
func_noun_entry_wleft(pardef47, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef47, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef47, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef47, '',"saBa", 'n','m','pl','p3','o')

pardef48 = ET.SubElement(pardefs,'pardef',n='kuvazvo')
func_noun_entry_wleft(pardef48, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef48, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef48, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef48, '',"saBa", 'n','m','pl','p3','o')

pardef49 = ET.SubElement(pardefs,'pardef',n='gehuzvo')
func_noun_entry_wleft(pardef49, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef49, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef49, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef49, '',"saBa", 'n','m','pl','p3','o')

pardef50 = ET.SubElement(pardefs,'pardef',n='kroXavo/kroXavahu/kroXavAZWNJseho/kroXavahuz')
func_noun_entry_wleft(pardef50, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef50, '',"", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef50, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef50, '',"", 'n','m','pl','p3','o')

pardef51 = ET.SubElement(pardefs,'pardef',n='suwazvo')
func_noun_entry_wleft(pardef51, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef51, '',"saBa", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef51, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef51, '',"saBa", 'n','m','pl','p3','o')

pardef52 = ET.SubElement(pardefs,'pardef',n='gosaiMyahoM')
func_noun_entry_wleft(pardef52, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef52, '',"saba", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef52, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef52, '',"saba", 'n','m','pl','p3','o')

pardef53 = ET.SubElement(pardefs,'pardef',n='sarisoMbo')
func_noun_entry_wleft(pardef53, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef53, '',"saba", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef53, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef53, '',"saba", 'n','m','pl','p3','o')

pardef54 = ET.SubElement(pardefs,'pardef',n='kariya')
func_adj_entry(pardef54, '',"kko", 'adj','m','sg','p3','d')
func_adj_entry(pardef54, '',"vA", 'adj','m','pl','p3','d')

tree = ET.ElementTree(root)

# Write the XML content to a file
with open("new_file", "w", encoding="utf-8") as file:
    # file.write(sdef_dec)
    tree.write(file, encoding="unicode")