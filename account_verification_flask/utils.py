def ensure_utf(s):
  try:
      if type(s) == unicode:
        return s.encode('utf8', 'ignore')
  except: 
    return str(s)