class SMS_store:

    def __init__(self):
        self.messages = list()

    def __str__(self):
        text = ""
        for number, (_, from_number, time_arrived, text_of_sms) in enumerate(self.messages):
            text += "{0}: {1} ({2})\n{3}\n".format(number, from_number, time_arrived, text_of_sms)
        return text

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        self.messages.append((False, from_number, time_arrived, text_of_sms))

    def message_count(self):
        return len(self.messages)
    def get_unread_indexes(self):
        unread = []
        for index, (read, _, _, _) in enumerate(self.messages):
            if not read:
                unread.append(index)
        return unread

    def get_message(self, index):
        _, from_number, time_arrived, text_of_sms = self.messages[index]
        return from_number, time_arrived, text_of_sms

    def delete(self, index):
        self.messages.pop(index)

    def clear(self):
        self.messages = list()