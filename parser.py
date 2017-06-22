import yaml

def open_yaml (filename):
    with open(filename, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print exc

def create_task_dict(parsed_yaml):
    task_dict = {}
    for task in parsed_yaml:
        task_dict[task] = get_all_operations(parsed_yaml, task)
    return task_dict

def get_all_operations(parsed_yaml, task):
    operation_list = []
    for operation in parsed_yaml[task]:
        operation_list.append(get_operation_dict(operation))

    return operation_list

def get_operation_dict(operation):
    if type(operation) == dict:
        return operation
    if type(operation) == str:
        return get_click_type_and_value(operation)

def get_click_type_and_value(operation):
    prefix_suffix_list = operation.split("=")

    if len(prefix_suffix_list) == 1:
        return {'text_value':prefix_suffix_list[0]}
    elif len(prefix_suffix_list) == 2:
        return {prefix_suffix_list[0]:prefix_suffix_list[1]}
    else:
        raise Exception("Prefix suffix list is too long, there must be an extra =")

parsed_yaml = open_yaml("test.yaml")
task_dict = create_task_dict(parsed_yaml)

for task, value in task_dict.iteritems():
    print str(task_dict[task]) + '\n'

