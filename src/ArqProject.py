from operator import delitem
import pandas as pd
import numpy as np


class NetflixVideos(object):
    def __init__(self, nd=0, data=[]):
        self.nd = nd
        self.id_title = data[0]
        self.id_languages = data[1]
        self.id_styear = data[2]
        self.id_type = data[3]
        self.id_country = data[4]
        self.id_rankpop = data[5]

    def __repr__(self):
        return ("%s\t%d\t%d\t%d\t%d\t%d\t" %  (str(self.id_title), (self.id_languages), (self.id_styear), (self.id_type), (self.id_country), (self.id_rankpop)))

class TitleCPD(object):
    def __init__(self, nd1=0, data=[]):
        self.nd1 = nd1
        self.id_title = data[0]
        self.title = data[1]
    
    def __repr__(self):
        return ("%d\t%s\t" % (self.id_title), (str(self.title)))

class LanguageCPD(object):
    def __init__(self, nd2=0, data=[]):
        self.nd2 = nd2
        self.id_language = data[0]
        self.language = data[1]

    def __repr__(self):
        return ("%d\t%s\t" % (self.id_language), (str(self.language)))

class StartYearCPD(object):
    def __init__(self, nd3=0, data=[]):
        self.nd3 = nd3
        self.id_styear = data[0]
        self.styear = data[1]

    def __repr__(self):
        return ("%d\t%s\t" % (self.id_year), (str(self.year)))

class TypeCPD(object):
    def __init__(self, nd4=0, data=[]):
        self.nd4 = nd4
        self.id_type = data[0]
        self.type = data[1]

    def __repr__(self):
        return ("%d\t%s\t" % (self.id_type), (str(self.type)))

class CountryOriginCPD(object):
    def __init__(self, nd5=0, data=[]):
        self.nd5 = nd5
        self.id_country = data[0]
        self.country = data[1]

    def __repr__(self):
        return ("%d\t%s\t" % (self.id_country), (str(self.country)))        

class PopularRankCPD(object):
    def __init__(self, nd6=0, data=[]):
        self.nd6 = nd6
        self.id_rankpop = data[0]
        self.rankpop = data[1]

    def __repr__(self):
        return ("%d\t%s\t" % (self.id_rankpop), (str(self.rankpop)))   
        

