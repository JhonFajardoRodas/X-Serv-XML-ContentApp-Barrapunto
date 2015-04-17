#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Simple XML parser for the RSS channel from BarraPunto
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the news (and urls) in BarraPunto.com,
#  after reading the corresponding RSS channel.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.htmlOut = ""

    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True
            
    def endElement (self, name):
        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
               
                htmlOut = "<li><b>Titular: " + self.theContent + "</b></li>"
                fich.write(htmlOut.encode('utf-8'))
                self.inContent = False
                self.theContent = ""
            elif name == 'link':
            
                fich.write("<li>Link: <a href='" + self.theContent + "'>" + self.theContent + "</a><li>")
                self.inContent = False
                self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars
            
# --- Main prog

#fich = open("barrapunto.html", "w")


#if len(sys.argv)<2:
#   print "Usage: python xml-parser-barrapunto.py <document>"
#    print
#    print " <document>: file name of the document to parse"
#    sys.exit(1)
    
# Load parser and driver
def get_bp(xmlFile):
    theParser = make_parser()
    theHandler = myContentHandler()
    theParser.setContentHandler(theHandler)

# Ready, set, go!

#xmlFile = open(sys.argv[1],"r")
    return theParser.parse(xmlFile)

#print "Parse complete"