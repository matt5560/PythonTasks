lines = int(input())
for i in range(lines):
    message = input()
    if message.find("%%") == 0:
        newmsg = message[2:]
        print(newmsg)
    elif message.find("####") == 0:
        pass
    else:
        print(message)