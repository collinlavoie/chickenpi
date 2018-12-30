from subprocess import check_output

class Reader(object):

    PROBE_BIN="bin/get_temp.sh"

    @classmethod
    def get_data(cls):
        return cls.read_probes()

    @classmethod
    def read_probes(cls):
        try:
            return check_output([PROBE_BIN])
        except:
            pass

