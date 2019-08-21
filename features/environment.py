from shouty.api import Api

def before_all(context):
  print('before all')
  context.shouty =  Api()
