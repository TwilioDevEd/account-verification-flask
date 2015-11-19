def ensure_utf(s):
  try:
      if type(s) == unicode:
        return s.encode('utf8', 'ignore')
  except: 
    return str(s)


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
