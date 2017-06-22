import yaml

with open("test.yaml", 'r') as stream:
    try:
        parsed_yaml = yaml.load(stream)
        print parsed_yaml

        for person in parsed_yaml:
            print person

            for trait in parsed_yaml[person]:
                print trait

    except yaml.YAMLError as exc:
        print exc
