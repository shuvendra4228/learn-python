ip_str = """192.168.0.1
192.168.1.1
192.168.2.1
192.168.0.2
192.168.0.3
192.168.1.4
192.168.2.1"""
ip_list = [ip for ip in ip_str.split("\n")]
user_input = int(input("enter a user group: "))
flag = False
for ip in ip_list:
    ip_grps =[int(grp) for grp in ip.split(".")]
    if user_input ==  ip_grps[2]:
        flag = True
        print(ip)
if not flag:
    print("not found")
