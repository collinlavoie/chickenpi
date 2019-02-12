from subprocess import check_output
import json
import re

class Reader(object):

    PROBE_BIN="../bin/get_temp.sh"
    SAMPLE_PATTERN=r'\d{4}(-\d\d){2} (\d\d:){2}\d\d,[0-9a-fA-F]{2}-[0-9a-fA-F]{12},-?\d*\.\d\d'

    @classmethod
    def get_data(cls):
        probe_data = cls.read_probes()
        data = []
        for sample in probe_data.splitlines():
            if re.match(cls.SAMPLE_PATTERN, sample):
                ( time, sensor, temp ) = sample.split(',')
                data.append({'sensor': sensor, 'time':time, 'temp':temp})
        return data

    @classmethod
    def read_probes(cls):
        try:
            import os
            current_dir = os.path.dirname(os.path.abspath(__file__))
            fullpath = os.path.join(current_dir, cls.PROBE_BIN)
            return check_output([fullpath])
        except Exception, e:
            print e
            return ""
