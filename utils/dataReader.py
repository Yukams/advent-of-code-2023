import traceback


def read_data(path):
    calling_script_dir = traceback.extract_stack()[-2].filename
    constructed_path = "\\".join(calling_script_dir.split("\\")[:-1]) + "\\" + path
    with open(constructed_path) as f:
        data = f.read()
    return data
