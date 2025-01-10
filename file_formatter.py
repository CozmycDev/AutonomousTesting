class File:
    NAME = 'file'
    PATH_FORMAT = '{os.getcwd()}/{name}'
    CONTENT = None
    EXIST_ERROR_MSG = f'File {path} already exists'

    def __init__(self):
        self.config = {
            'name': None,
            'content': '',
            'path': ''
        }

    def create(self, name, content=None):
        if not self.name:
            raise ValueError('Name is required')
        self.path = self.PATH_FORMAT.format(os.getcwd(), name)
        if os.path.exists(self.path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=self.path))
        self.config['name'] = name
        self.config['content'] = content or ''
        with open(self.path, 'w') as file:
            file.write(self.config['content'])

    def update(self, name=None, content=None):
        if not self.name:
            raise ValueError('Name is required')
        new_name = name or self.config.get('name')
        path = f'{self.path}/{new_name}' if new_name else self.path
        if os.path.exists(path):
            raise FileExistsError(self.EXIST_ERROR_MSG.format(path=path))
        self.config['name'] = new_name
        self.config['content'] = content or ''
        with open(self.path, 'w') as file:
            file.write(self.config['content'])

    def delete(self):
        if not self.path:
            raise ValueError('File does not exist')
        import os
        os.remove(self.path)