from textblob import TextBlob as tb

class DataHandler:
    def __init__(self, base, data_file):
        self.base = base
        self.topics = {}
        self.default_action = ""
        self.read_file(data_file)

    def read_file(self, data_file):
        """ Read and parse the data file.
        """
        with open(data_file, "r") as the_file:
            data = the_file.readlines()

        self.topics = {}
        current_topic_key = {}
        current_topic = ""
        current_action = ""
        for line in data:
            line = line.lower()
            if line.strip().startswith("#"):
                continue
            elif line.strip().startswith("default_action"):
                self.default_action = line.split("=")[1].strip()
            elif line.strip().startswith("<") and not line.strip().startswith("</"):
                current_topic = self.base.find_substring(line, "<", ">").strip()
                self.topics[current_topic] = None
            elif line.strip().startswith("</"):
                self.topics[current_topic] = {"keywords" : current_topic_key,
                                              "action" : current_action}
                current_topic = ""
            elif line.strip().startswith("keywords") and current_topic:
                current_topic_key = tb(self.base.find_substring(line, "{", "}"))
            elif line.strip().startswith("actionfile") and current_topic:
                current_action = line.split("=")[1].strip()

    def get_doc_list(self):
        doc_list = []
        for topic in self.topics.keys():
            doc_list.append(self.topics[topic]["keywords"])
        return doc_list
    
    def get_default_action(self):
        return self.default_action
    