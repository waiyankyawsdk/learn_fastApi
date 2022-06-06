import sys
try:
   untrusted.execute()
except: # catch *all* exceptions
   e = sys.exc_info()[0]
print( "<p>Error: %s</p>" % e )