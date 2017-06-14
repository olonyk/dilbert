from time import gmtime, strftime
import re

class Base:
    """ The base object handles simple tasks that all other instanses can use.
    """
    def __init__(self, **kwargs):
        """ Read the input arguments. If a non default log file is set then use that one. If
        the user has set the warning levels then adjust it.
        """
        if "logfile" in kwargs:
            self.log_file = kwargs["log"]
        else:
            self.log_file = "log.txt"

        # The on_error flag has four values: stop, log, log and print and ignore
        if "on_error" in kwargs:
            self.on_error = kwargs["on_error"]
        else:
            self.on_error = "log"

        # The on_log flag has three values: print, log, or ignore
        if "on_log" in kwargs:
            self.on_log = kwargs["on_error"]
        else:
            self.on_log = "log"

    def log(self, msg):
        """ Print message to the log file
        """
        if "ignore" in self.on_log:
            return
        msg = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " " + msg
        if "print" in self.on_log:
            print(msg)
        if "log" in self.on_log:
            with open(self.log_file, "a") as log_file:
                log_file.write(msg+"\n")

    def err_log(self, msg):
        """ Print error to the log file
        """
        if "ignore" in self.on_error:
            return
        msg = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " ERROR " + msg
        if "log" in self.on_error:
            with open(self.log_file, "a") as log_file:
                log_file.write(msg+"\n")
        if "print" in self.on_error:
            print(msg)
        if "stop" in self.on_error:
            raise ValueError('Base stoped on error')

    def find_substring(self, input_str, start, end):
        """ Help function which returns the substring between the start and end which are also
            strings
        """
        try:
            start = input_str.find(start)
            end = input_str.find(end, start)
            if start < end:
                return input_str[start+1: end]
            else:
                return input_str[start, :]
        except ValueError:
            return ""

    def read_file(self, file_name):
        with open(file_name, "r") as the_file:
            data = the_file.readlines()
        return data
