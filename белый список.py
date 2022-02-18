whitelist_len = int(input())
set_wl = []
set_sh = []
for i in range(whitelist_len):
    whitelist = input()
    set_wl.append(whitelist)
searchhistory_len = int(input())
for j in range(searchhistory_len):
    searchhistory = input()
    set_sh.append(searchhistory)

print(set_sh - set_wl)