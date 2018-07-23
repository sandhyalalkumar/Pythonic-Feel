import json

with open("/home/modak/Codebase/Modak/Testing/continuous-testing-ws/config/dev.json") as config_obj:
    config_json = json.load(config_obj)
    print config_json