from Advanced_track.Week_1.Class_SMSfile import SMS_store

my_inbox =  SMS_store()

my_inbox.add_new_arrival(1234, 12, "Hello")
my_inbox.add_new_arrival(4512, 15, "test")
my_inbox.add_new_arrival(1234, 16, "Text")

print(my_inbox)
print(my_inbox.message_count())

print(my_inbox.get_message(1))

print(my_inbox.get_unread_indexes())

my_inbox.delete(0)
print(my_inbox)

my_inbox.clear()
print(my_inbox.message_count())