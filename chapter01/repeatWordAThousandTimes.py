#!/usr/bin/env python

def main():
  word = raw_input("Say a word and I will repeat it a thousand times: ").strip()
  
  if (word.count(" ") > 0):
    print "More than one word!! Please try again."
    main()
    return
  
  print " ".join([word for x in range(0, 100)])

main()
