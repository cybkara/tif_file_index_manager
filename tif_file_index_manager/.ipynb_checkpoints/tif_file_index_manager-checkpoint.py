def format_finder(file_format, path):

    if not file_format.startswith('.'):
        raise ValueError('Add dot at the beggining of the file_format')
    for root, dirs, files in os.walk(path):
        for file in files:
           if file_format in file:
               print(os.path.join(root,file))