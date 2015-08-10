from shouty.api import Api

def before_scenario(context, scenario):
    context.automation = Api()
