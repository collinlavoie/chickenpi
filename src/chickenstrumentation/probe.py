from subprocess import check_output
import urllib2
import json

class Reader(object):

    PROBE_BIN="../bin/get_temp.sh"

    @classmethod
    def get_data(cls):
        return cls.read_probes()

    @classmethod
    def read_probes(cls):
        try:
            return check_output([cls.PROBE_BIN])
        except:
            return []

class WebReader(Reader):

    @classmethod
    def get_web_resource(cls):
        content = urllib2.urlopen("http://chickenstrumentation/1h").read()
        # get data for desired probe
        data = [x for x in json.loads(content)]
        return data

    @classmethod
    def get_data(cls):
        return cls.read_probes()

    @classmethod
    def read_probes(cls):
         return cls.get_web_resource()
#        try:
#        except:
#            return []

