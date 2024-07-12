def format_finder(file_format, path):

    files_list = []
    if not file_format.startswith('.'):
        raise ValueError('Add dot at the beggining of the file_format')
    for root, dirs, files in os.walk(path):
        for file in files:
           if file_format in file:
               files_list.append(os.path.join(root,file))
    
    return files_list      