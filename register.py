#!/usr/bin/python
# Tommy Shiou

from BeautifulSoup import BeautifulSoup
import sys
import re
"""
def is_open(filename, section):
  f = open(filename, 'rU')
  text = f.readlines()

  found = False

  for line in text:
    if line.find(section) != -1:
      foundIndex = text.index(line)
      found = True

  if(not found):
    sys.stderr.write('Invalid Section\n')
    sys.exit(1)

  index = text.index('<TR>\n' , foundIndex-10, foundIndex)
  if text[index + 1].find('dddefault') != -1:
    if text[index + 1].find('Closed') == -1:
      return True
    else:
      return False
  
  f.close()

"""
def is_open(filename, section):
  
  f = open(filename, 'rU')
  text = f.read()

  soup = BeautifulSoup(text)
  found = False
  isOpen = False
  entries = soup.findAll('tr')
  for entry in entries:
    for text in entry.findAll(text=True):
      txt = unicode(text).encode("utf-8")
      if txt.find(section) != -1:
        found = True
        if entry.find(title="Closed") == None:
          isOpen = True
  if (not found):
    sys.stderr.write('Invalid Section\n')
    sys.exit(1)
  return isOpen

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 3:
    print 'usage: ./register.py {section} file'
    sys.exit(1)

  section = sys.argv[1]
  filename = sys.argv[2]

  if(is_open(filename, section)):
    print 'Section ' + section + ' is open'
  else:
    print 'Section ' + section + ' is closed'

if __name__== '__main__':
  main()
