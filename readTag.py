import yaml;
yaml.SafeLoader.yaml_implicit_resolvers.pop('=')
with open('Tags.yaml', 'r') as file:
    data = yaml.safe_load(file);