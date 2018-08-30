import os
import yaml


class Datastore:
    ''' A class to manage job data storage on the cluster.

    '''
    store_name = 'datastore.yaml'

    def __init__(self, connection):
        self.connection = connection

    def write(self, basedir, data):
        path = os.path.join(basedir, self.store_name)
        content = yaml.dump(data)
        self.connection.put_file_content(content, path)

    def read(self, basedir):
        path = os.path.join(basedir, self.store_name)
        content = self.connection.get_file_content(path)
        return yaml.load(content)

    def read_multiple(self, basedict):
        '''
        Accepts a dict where the values are base directories
        of a run, and replaces the value with the content of
        the datastore for that run, leaving the keys untouched.

        '''
        return {key: self.read(dir) for key, dir in basedict.items()}

    def all_job_ids(self, basedir):
        return self.connection.list_dir(basedir)
