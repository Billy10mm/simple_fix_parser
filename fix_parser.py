class FIXParser(object):
    def __init__(self, fix_log, call_back):
        self.fix_log = fix_log
        self.call_back = call_back

        with open(self.fix_log) as f:
            for line in f:
                fix_data = {}
                kv_pairs = line.split("\1")
                for kv_pair in kv_pairs:
                    if "=" in kv_pair:
                        key, value = kv_pair.split("=")
                        fix_data[int(key)] = value
                self.call_back(fix_data)