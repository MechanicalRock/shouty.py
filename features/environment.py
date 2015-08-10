from shouty.api import Api

def before_all(context):
    context.automation = Api()
