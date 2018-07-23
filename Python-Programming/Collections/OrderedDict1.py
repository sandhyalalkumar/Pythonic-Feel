from collections import OrderedDict

roll_no = OrderedDict()

list_roll_no = [
    (11, 'Shubham'),
    (9, 'Pankaj'),
    (17, 'JournalDev')
]

roll_no.update(list_roll_no)

print roll_no

for key, value in roll_no.items():
    print key, value
