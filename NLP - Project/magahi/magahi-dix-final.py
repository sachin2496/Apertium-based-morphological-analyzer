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

e1.text = ""

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

pardef5 = ET.SubElement(pardefs,'pardef',n='laiki')
func_noun_entry_wleft(pardef5, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef5, '',"no", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef5, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef5, '',"no", 'n','f','pl','p3','o')

pardef6 = ET.SubElement(pardefs,'pardef',n='mAi')
func_noun_entry_wleft(pardef6, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef6, '',"no", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef6, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef6, '',"no", 'n','f','pl','p3','o')

pardef7 = ET.SubElement(pardefs,'pardef',n='r')
func_noun_entry_wleft(pardef7, '',"Awo", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef7, '',"Awo", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef7, '',"Awo", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef7, '',"awano", 'n','f','pl','p3','o')

pardef8 = ET.SubElement(pardefs,'pardef',n='rawi')
func_noun_entry_wleft(pardef8, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef8, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef8, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef8, '',"nao", 'n','f','pl','p3','o')

pardef9 = ET.SubElement(pardefs,'pardef',n='Oraw')
func_noun_entry_wleft(pardef9, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef9, '',"anao", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef9, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef9, '',"anao", 'n','f','pl','p3','o')

pardef10 = ET.SubElement(pardefs,'pardef',n='BAs')
func_noun_entry_wleft(pardef10, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef10, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef10, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef10, '',"ano", 'n','f','pl','p3','o')

pardef11 = ET.SubElement(pardefs,'pardef',n='gudZiy')
func_noun_entry_wleft(pardef11, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef11, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef11, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef11, '',"ano", 'n','f','pl','p3','o')

pardef12 = ET.SubElement(pardefs,'pardef',n='sakwi')
func_noun_entry_wleft(pardef12, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef12, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef12, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef12, '',"no", 'n','f','pl','p3','o')

pardef13 = ET.SubElement(pardefs,'pardef',n='qwu')
func_noun_entry_wleft(pardef13, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef13, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef13, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef13, '',"no", 'n','f','pl','p3','o')

pardef14 = ET.SubElement(pardefs,'pardef',n='bahu')
func_noun_entry_wleft(pardef14, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef14, '',"no", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef14, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef14, '',"no", 'n','f','pl','p3','o')

pardef15 = ET.SubElement(pardefs,'pardef',n='l')
func_noun_entry_wleft(pardef15, '',"Ovo", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef15, '',"avano", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef15, '',"Ovo", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef15, '',"avano", 'n','f','pl','p3','o')

pardef16 = ET.SubElement(pardefs,'pardef',n='mAz')
func_noun_entry_wleft(pardef16, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef16, '',"ano", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef16, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef16, '',"ano", 'n','f','pl','p3','o')

pardef17 = ET.SubElement(pardefs,'pardef',n='PotoM')
func_noun_entry_wleft(pardef17, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef17, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef17, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef17, '',"no", 'n','f','pl','p3','o')

pardef18 = ET.SubElement(pardefs,'pardef',n='BUiM')
func_noun_entry_wleft(pardef18, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef18, '',"ano", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef18, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef18, '',"ano", 'n','f','pl','p3','o')

pardef19 = ET.SubElement(pardefs,'pardef',n='BOM')
func_noun_entry_wleft(pardef19, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef19, '',"ano", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef19, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef19, '',"ano", 'n','f','pl','p3','o')

pardef20 = ET.SubElement(pardefs,'pardef',n='BarasaiM')
func_noun_entry_wleft(pardef20, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef20, '',"no", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef20, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef20, '',"no", 'n','f','pl','p3','o')

pardef21 = ET.SubElement(pardefs,'pardef',n='Bor')
func_noun_entry_wleft(pardef21, '',"o", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef21, '',"o", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef21, '',"o", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef21, '',"ano", 'n','f','pl','p3','o')

pardef22 = ET.SubElement(pardefs,'pardef',n='Poto')
func_noun_entry_wleft(pardef22, '',"O", 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef22, '',"O", 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef22, '',"O", 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef22, '',"no", 'n','f','pl','p3','o')

pardef23 = ET.SubElement(pardefs,'pardef',n='laik')
func_noun_entry_wleft(pardef23, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef23, '',"ane", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef23, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef23, '',"ane", 'n','m','pl','p3','o')

pardef24 = ET.SubElement(pardefs,'pardef',n='r')
func_noun_entry_wleft(pardef24, '',"Aje", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef24, '',"Aje", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef24, '',"Aje", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef24, '',"ajanai", 'n','m','pl','p3','o')

pardef25 = ET.SubElement(pardefs,'pardef',n='Gar')
func_noun_entry_wleft(pardef25, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef25, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef25, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef25, '',"anai", 'n','m','pl','p3','o')

pardef26 = ET.SubElement(pardefs,'pardef',n='Karc')
func_noun_entry_wleft(pardef26, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef26, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef26, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef26, '',"anai", 'n','m','pl','p3','o')

pardef27 = ET.SubElement(pardefs,'pardef',n='kavi')
func_noun_entry_wleft(pardef27, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef27, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef27, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef27, '',"ne", 'n','m','pl','p3','o')

pardef28 = ET.SubElement(pardefs,'pardef',n='Axami')
func_noun_entry_wleft(pardef28, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef28, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef28, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef28, '',"ne", 'n','m','pl','p3','o')

pardef29 = ET.SubElement(pardefs,'pardef',n='sonar')
func_noun_entry_wleft(pardef29, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef29, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef29, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef29, '',"anai", 'n','m','pl','p3','o')

pardef30 = ET.SubElement(pardefs,'pardef',n='sawru')
func_noun_entry_wleft(pardef30, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef30, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef30, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef30, '',"ne", 'n','m','pl','p3','o')

pardef31 = ET.SubElement(pardefs,'pardef',n='Alu')
func_noun_entry_wleft(pardef31, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef31, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef31, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef31, '',"ne", 'n','m','pl','p3','o')

pardef32 = ET.SubElement(pardefs,'pardef',n='kuv')
func_noun_entry_wleft(pardef32, '',"eM", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef32, '',"eM", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef32, '',"eM", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef32, '',"aznai", 'n','m','pl','p3','o')

pardef33 = ET.SubElement(pardefs,'pardef',n='gehuz')
func_noun_entry_wleft(pardef33, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef33, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef33, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef33, '',"ne", 'n','m','pl','p3','o')

pardef34 = ET.SubElement(pardefs,'pardef',n='kroXe')
func_noun_entry_wleft(pardef34, '',"", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef34, '',"", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef34, '',"", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef34, '',"", 'n','m','pl','p3','o')

pardef35 = ET.SubElement(pardefs,'pardef',n='lakaTo')
func_noun_entry_wleft(pardef35, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef35, '',"ne", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef35, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef35, '',"ne", 'n','m','pl','p3','o')

pardef36 = ET.SubElement(pardefs,'pardef',n='sarasoM')
func_noun_entry_wleft(pardef36, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef36, '',"ne", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef36, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef36, '',"ne", 'n','m','pl','p3','o')

pardef37 = ET.SubElement(pardefs,'pardef',n='gosaiM')
func_noun_entry_wleft(pardef37, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef37, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef37, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef37, '',"ne", 'n','m','pl','p3','o')

pardef38 = ET.SubElement(pardefs,'pardef',n='laikav')
func_noun_entry_wleft(pardef38, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef38, '',"ane", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef38, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef38, '',"ane", 'n','m','pl','p3','o')

pardef39 = ET.SubElement(pardefs,'pardef',n='rajav')
func_noun_entry_wleft(pardef39, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef39, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef39, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef39, '',"anai", 'n','m','pl','p3','o')

pardef40 = ET.SubElement(pardefs,'pardef',n='Garav')
func_noun_entry_wleft(pardef40, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef40, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef40, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef40, '',"anai", 'n','m','pl','p3','o')

pardef41 = ET.SubElement(pardefs,'pardef',n='Karacav')
func_noun_entry_wleft(pardef41, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef41, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef41, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef41, '',"anai", 'n','m','pl','p3','o')

pardef42 = ET.SubElement(pardefs,'pardef',n='kaviy')
func_noun_entry_wleft(pardef42, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef42, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef42, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef42, '',"anai", 'n','m','pl','p3','o')

pardef43 = ET.SubElement(pardefs,'pardef',n='axamiy')
func_noun_entry_wleft(pardef43, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef43, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef43, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef43, '',"anai", 'n','m','pl','p3','o')

pardef44 = ET.SubElement(pardefs,'pardef',n='sawruv')
func_noun_entry_wleft(pardef44, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef44, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef44, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef44, '',"anai", 'n','m','pl','p3','o')

pardef45 = ET.SubElement(pardefs,'pardef',n='aluv')
func_noun_entry_wleft(pardef45, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef45, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef45, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef45, '',"anai", 'n','m','pl','p3','o')

pardef46 = ET.SubElement(pardefs,'pardef',n='kuvaz')
func_noun_entry_wleft(pardef46, '',"veM", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef46, '',"veM", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef46, '',"veM", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef46, '',"ne", 'n','m','pl','p3','o')

pardef47 = ET.SubElement(pardefs,'pardef',n='gehuzv')
func_noun_entry_wleft(pardef47, '',"eM", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef47, '',"eM", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef47, '',"eM", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef47, '',"anai", 'n','m','pl','p3','o')

pardef48 = ET.SubElement(pardefs,'pardef',n='sonarav')
func_noun_entry_wleft(pardef48, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef48, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef48, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef48, '',"anai", 'n','m','pl','p3','o')

pardef49 = ET.SubElement(pardefs,'pardef',n='kroXav')
func_noun_entry_wleft(pardef49, '',"e", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef49, '',"e", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef49, '',"e", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef49, '',"anai", 'n','m','pl','p3','o')

pardef50 = ET.SubElement(pardefs,'pardef',n='laikav')
func_noun_entry_wleft(pardef50, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef50, '',"ano", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef50, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef50, '',"ano", 'n','m','pl','p3','o')

pardef51 = ET.SubElement(pardefs,'pardef',n='rajav')
func_noun_entry_wleft(pardef51, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef51, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef51, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef51, '',"ano", 'n','m','pl','p3','o')

pardef52 = ET.SubElement(pardefs,'pardef',n='Garav')
func_noun_entry_wleft(pardef52, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef52, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef52, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef52, '',"anO", 'n','m','pl','p3','o')

pardef53 = ET.SubElement(pardefs,'pardef',n='Karacav')
func_noun_entry_wleft(pardef53, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef53, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef53, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef53, '',"ano", 'n','m','pl','p3','o')

pardef54 = ET.SubElement(pardefs,'pardef',n='kaviy')
func_noun_entry_wleft(pardef54, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef54, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef54, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef54, '',"ano", 'n','m','pl','p3','o')

pardef55 = ET.SubElement(pardefs,'pardef',n='axamiy')
func_noun_entry_wleft(pardef55, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef55, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef55, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef55, '',"ano", 'n','m','pl','p3','o')

pardef56 = ET.SubElement(pardefs,'pardef',n='sawruva')
func_noun_entry_wleft(pardef56, '',"u", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef56, '',"u", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef56, '',"u", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef56, '',"nao", 'n','m','pl','p3','o')

pardef57 = ET.SubElement(pardefs,'pardef',n='alu')
func_noun_entry_wleft(pardef57, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef57, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef57, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef57, '',"ano", 'n','m','pl','p3','o')

pardef58 = ET.SubElement(pardefs,'pardef',n='kuvaz')
func_noun_entry_wleft(pardef58, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef58, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef58, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef58, '',"vano", 'n','m','pl','p3','o')

pardef59 = ET.SubElement(pardefs,'pardef',n='gehuMva')
func_noun_entry_wleft(pardef59, '',"u", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef59, '',"u", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef59, '',"u", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef59, '',"nau", 'n','m','pl','p3','o')

pardef60 = ET.SubElement(pardefs,'pardef',n='sonarav')
func_noun_entry_wleft(pardef60, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef60, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef60, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef60, '',"ano", 'n','m','pl','p3','o')

pardef61 = ET.SubElement(pardefs,'pardef',n='kroXav')
func_noun_entry_wleft(pardef61, '',"o", 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef61, '',"o", 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef61, '',"o", 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef61, '',"ano", 'n','m','pl','p3','o')

pardef62 = ET.SubElement(pardefs,'pardef',n='kariya')
func_adj_entry(pardef62, '',"kko", 'adj','m','sg','p3','d')
func_adj_entry(pardef62, '',"vA", 'adj','m','pl','p3','d')


tree = ET.ElementTree(root)

# Write the XML content to a file
with open("magahi-final.dix", "w", encoding="utf-8") as file:
    # file.write(sdef_dec)
    tree.write(file, encoding="unicode")



pardef5 = ET.SubElement(pardefs,'pardef',n='laiki')
func_noun_entry_wleft(pardef5, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef5, 'no','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef5, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef5, 'no','', 'n','f','pl','p3','o')

pardef6 = ET.SubElement(pardefs,'pardef',n='mAi')
func_noun_entry_wleft(pardef6, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef6, 'no','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef6, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef6, 'no','', 'n','f','pl','p3','o')

pardef7 = ET.SubElement(pardefs,'pardef',n='r')
func_noun_entry_wleft(pardef7, 'Awo','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef7, 'Awo','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef7, 'Awo','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef7, 'awano','', 'n','f','pl','p3','o')

pardef8 = ET.SubElement(pardefs,'pardef',n='rawi')
func_noun_entry_wleft(pardef8, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef8, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef8, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef8, 'nao','', 'n','f','pl','p3','o')

pardef9 = ET.SubElement(pardefs,'pardef',n='Oraw')
func_noun_entry_wleft(pardef9, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef9, 'anao','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef9, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef9, 'anao','', 'n','f','pl','p3','o')

pardef10 = ET.SubElement(pardefs,'pardef',n='BAs')
func_noun_entry_wleft(pardef10, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef10, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef10, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef10, 'ano','', 'n','f','pl','p3','o')

pardef11 = ET.SubElement(pardefs,'pardef',n='gudZiy')
func_noun_entry_wleft(pardef11, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef11, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef11, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef11, 'ano','', 'n','f','pl','p3','o')

pardef12 = ET.SubElement(pardefs,'pardef',n='sakwi')
func_noun_entry_wleft(pardef12, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef12, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef12, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef12, 'no','', 'n','f','pl','p3','o')

pardef13 = ET.SubElement(pardefs,'pardef',n='qwu')
func_noun_entry_wleft(pardef13, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef13, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef13, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef13, 'no','', 'n','f','pl','p3','o')

pardef14 = ET.SubElement(pardefs,'pardef',n='bahu')
func_noun_entry_wleft(pardef14, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef14, 'no','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef14, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef14, 'no','', 'n','f','pl','p3','o')

pardef15 = ET.SubElement(pardefs,'pardef',n='l')
func_noun_entry_wleft(pardef15, 'Ovo','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef15, 'avano','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef15, 'Ovo','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef15, 'avano','', 'n','f','pl','p3','o')

pardef16 = ET.SubElement(pardefs,'pardef',n='mAz')
func_noun_entry_wleft(pardef16, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef16, 'ano','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef16, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef16, 'ano','', 'n','f','pl','p3','o')

pardef17 = ET.SubElement(pardefs,'pardef',n='PotoM')
func_noun_entry_wleft(pardef17, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef17, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef17, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef17, 'no','', 'n','f','pl','p3','o')

pardef18 = ET.SubElement(pardefs,'pardef',n='BUiM')
func_noun_entry_wleft(pardef18, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef18, 'ano','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef18, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef18, 'ano','', 'n','f','pl','p3','o')

pardef19 = ET.SubElement(pardefs,'pardef',n='BOM')
func_noun_entry_wleft(pardef19, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef19, 'ano','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef19, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef19, 'ano','', 'n','f','pl','p3','o')

pardef20 = ET.SubElement(pardefs,'pardef',n='BarasaiM')
func_noun_entry_wleft(pardef20, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef20, 'no','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef20, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef20, 'no','', 'n','f','pl','p3','o')

pardef21 = ET.SubElement(pardefs,'pardef',n='Bor')
func_noun_entry_wleft(pardef21, 'o','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef21, 'o','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef21, 'o','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef21, 'ano','', 'n','f','pl','p3','o')

pardef22 = ET.SubElement(pardefs,'pardef',n='Poto')
func_noun_entry_wleft(pardef22, 'O','', 'n','f','sg','p3','d')
func_noun_entry_wleft(pardef22, 'O','', 'n','f','pl','p3','d')
func_noun_entry_wleft(pardef22, 'O','', 'n','f','sg','p3','o')
func_noun_entry_wleft(pardef22, 'no','', 'n','f','pl','p3','o')

pardef23 = ET.SubElement(pardefs,'pardef',n='laik')
func_noun_entry_wleft(pardef23, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef23, 'ane','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef23, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef23, 'ane','', 'n','m','pl','p3','o')

pardef24 = ET.SubElement(pardefs,'pardef',n='r')
func_noun_entry_wleft(pardef24, 'Aje','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef24, 'Aje','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef24, 'Aje','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef24, 'ajanai','', 'n','m','pl','p3','o')

pardef25 = ET.SubElement(pardefs,'pardef',n='Gar')
func_noun_entry_wleft(pardef25, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef25, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef25, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef25, 'anai','', 'n','m','pl','p3','o')

pardef26 = ET.SubElement(pardefs,'pardef',n='Karc')
func_noun_entry_wleft(pardef26, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef26, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef26, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef26, 'anai','', 'n','m','pl','p3','o')

pardef27 = ET.SubElement(pardefs,'pardef',n='kavi')
func_noun_entry_wleft(pardef27, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef27, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef27, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef27, 'ne','', 'n','m','pl','p3','o')

pardef28 = ET.SubElement(pardefs,'pardef',n='Axami')
func_noun_entry_wleft(pardef28, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef28, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef28, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef28, 'ne','', 'n','m','pl','p3','o')

pardef29 = ET.SubElement(pardefs,'pardef',n='sonar')
func_noun_entry_wleft(pardef29, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef29, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef29, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef29, 'anai','', 'n','m','pl','p3','o')

pardef30 = ET.SubElement(pardefs,'pardef',n='sawru')
func_noun_entry_wleft(pardef30, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef30, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef30, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef30, 'ne','', 'n','m','pl','p3','o')

pardef31 = ET.SubElement(pardefs,'pardef',n='Alu')
func_noun_entry_wleft(pardef31, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef31, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef31, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef31, 'ne','', 'n','m','pl','p3','o')

pardef32 = ET.SubElement(pardefs,'pardef',n='kuv')
func_noun_entry_wleft(pardef32, 'eM','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef32, 'eM','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef32, 'eM','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef32, 'aznai','', 'n','m','pl','p3','o')

pardef33 = ET.SubElement(pardefs,'pardef',n='gehuz')
func_noun_entry_wleft(pardef33, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef33, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef33, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef33, 'ne','', 'n','m','pl','p3','o')

pardef34 = ET.SubElement(pardefs,'pardef',n='kroXe')
func_noun_entry_wleft(pardef34, '','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef34, '','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef34, '','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef34, '','', 'n','m','pl','p3','o')

pardef35 = ET.SubElement(pardefs,'pardef',n='lakaTo')
func_noun_entry_wleft(pardef35, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef35, 'ne','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef35, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef35, 'ne','', 'n','m','pl','p3','o')

pardef36 = ET.SubElement(pardefs,'pardef',n='sarasoM')
func_noun_entry_wleft(pardef36, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef36, 'ne','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef36, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef36, 'ne','', 'n','m','pl','p3','o')

pardef37 = ET.SubElement(pardefs,'pardef',n='gosaiM')
func_noun_entry_wleft(pardef37, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef37, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef37, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef37, 'ne','', 'n','m','pl','p3','o')

pardef38 = ET.SubElement(pardefs,'pardef',n='laikav')
func_noun_entry_wleft(pardef38, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef38, 'ane','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef38, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef38, 'ane','', 'n','m','pl','p3','o')

pardef39 = ET.SubElement(pardefs,'pardef',n='rajav')
func_noun_entry_wleft(pardef39, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef39, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef39, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef39, 'anai','', 'n','m','pl','p3','o')

pardef40 = ET.SubElement(pardefs,'pardef',n='Garav')
func_noun_entry_wleft(pardef40, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef40, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef40, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef40, 'anai','', 'n','m','pl','p3','o')

pardef41 = ET.SubElement(pardefs,'pardef',n='Karacav')
func_noun_entry_wleft(pardef41, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef41, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef41, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef41, 'anai','', 'n','m','pl','p3','o')

pardef42 = ET.SubElement(pardefs,'pardef',n='kaviy')
func_noun_entry_wleft(pardef42, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef42, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef42, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef42, 'anai','', 'n','m','pl','p3','o')

pardef43 = ET.SubElement(pardefs,'pardef',n='axamiy')
func_noun_entry_wleft(pardef43, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef43, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef43, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef43, 'anai','', 'n','m','pl','p3','o')

pardef44 = ET.SubElement(pardefs,'pardef',n='sawruv')
func_noun_entry_wleft(pardef44, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef44, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef44, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef44, 'anai','', 'n','m','pl','p3','o')

pardef45 = ET.SubElement(pardefs,'pardef',n='aluv')
func_noun_entry_wleft(pardef45, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef45, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef45, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef45, 'anai','', 'n','m','pl','p3','o')

pardef46 = ET.SubElement(pardefs,'pardef',n='kuvaz')
func_noun_entry_wleft(pardef46, 'veM','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef46, 'veM','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef46, 'veM','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef46, 'ne','', 'n','m','pl','p3','o')

pardef47 = ET.SubElement(pardefs,'pardef',n='gehuzv')
func_noun_entry_wleft(pardef47, 'eM','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef47, 'eM','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef47, 'eM','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef47, 'anai','', 'n','m','pl','p3','o')

pardef48 = ET.SubElement(pardefs,'pardef',n='sonarav')
func_noun_entry_wleft(pardef48, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef48, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef48, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef48, 'anai','', 'n','m','pl','p3','o')

pardef49 = ET.SubElement(pardefs,'pardef',n='kroXav')
func_noun_entry_wleft(pardef49, 'e','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef49, 'e','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef49, 'e','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef49, 'anai','', 'n','m','pl','p3','o')

pardef50 = ET.SubElement(pardefs,'pardef',n='laikav')
func_noun_entry_wleft(pardef50, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef50, 'ano','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef50, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef50, 'ano','', 'n','m','pl','p3','o')

pardef51 = ET.SubElement(pardefs,'pardef',n='rajav')
func_noun_entry_wleft(pardef51, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef51, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef51, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef51, 'ano','', 'n','m','pl','p3','o')

pardef52 = ET.SubElement(pardefs,'pardef',n='Garav')
func_noun_entry_wleft(pardef52, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef52, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef52, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef52, 'anO','', 'n','m','pl','p3','o')

pardef53 = ET.SubElement(pardefs,'pardef',n='Karacav')
func_noun_entry_wleft(pardef53, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef53, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef53, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef53, 'ano','', 'n','m','pl','p3','o')

pardef54 = ET.SubElement(pardefs,'pardef',n='kaviy')
func_noun_entry_wleft(pardef54, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef54, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef54, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef54, 'ano','', 'n','m','pl','p3','o')

pardef55 = ET.SubElement(pardefs,'pardef',n='axamiy')
func_noun_entry_wleft(pardef55, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef55, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef55, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef55, 'ano','', 'n','m','pl','p3','o')

pardef56 = ET.SubElement(pardefs,'pardef',n='sawruva')
func_noun_entry_wleft(pardef56, 'u','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef56, 'u','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef56, 'u','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef56, 'nao','', 'n','m','pl','p3','o')

pardef57 = ET.SubElement(pardefs,'pardef',n='alu')
func_noun_entry_wleft(pardef57, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef57, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef57, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef57, 'ano','', 'n','m','pl','p3','o')

pardef58 = ET.SubElement(pardefs,'pardef',n='kuvaz')
func_noun_entry_wleft(pardef58, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef58, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef58, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef58, 'vano','', 'n','m','pl','p3','o')

pardef59 = ET.SubElement(pardefs,'pardef',n='gehuMva')
func_noun_entry_wleft(pardef59, 'u','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef59, 'u','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef59, 'u','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef59, 'nau','', 'n','m','pl','p3','o')

pardef60 = ET.SubElement(pardefs,'pardef',n='sonarav')
func_noun_entry_wleft(pardef60, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef60, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef60, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef60, 'ano','', 'n','m','pl','p3','o')

pardef61 = ET.SubElement(pardefs,'pardef',n='kroXav')
func_noun_entry_wleft(pardef61, 'o','', 'n','m','sg','p3','d')
func_noun_entry_wleft(pardef61, 'o','', 'n','m','pl','p3','d')
func_noun_entry_wleft(pardef61, 'o','', 'n','m','sg','p3','o')
func_noun_entry_wleft(pardef61, 'ano','', 'n','m','pl','p3','o')

pardef62 = ET.SubElement(pardefs,'pardef',n='kariya')
func_adj_entry(pardef62, 'kko','', 'adj','m','sg','p3','d')
func_adj_entry(pardef62, 'vA','', 'adj','m','pl','p3','d')

tree = ET.ElementTree(root)

# Write the XML content to a file
with open("magahi-final.dix", "w", encoding="utf-8") as file:
    # file.write(sdef_dec)
    tree.write(file, encoding="unicode")
