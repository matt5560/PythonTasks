message_ = input("введите сообщение: ")
message_len = len(message_)

message_cost = message_len * 40

rub = message_cost // 100
kop = message_cost % 100

print (rub,"p.",kop,"к.")


