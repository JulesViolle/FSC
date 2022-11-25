
import pythonanywhere.api
import getpass


import ghasedakpack




# message = "Target Loged In"
# receptor1 = "09122784417"

# linenumber = "10008566"
# sms = ghasedakpack.Ghasedak("da7dedef299d90954b5a94ab532e090c2eba2dc2db153701b6ee2a713d412e24")
# sms.send({'message':'hello world!', 'receptor' : '09108673287', 'linenumber': '100008566' ,'checkid': '5127'})
# print(sms.status({'id': '5127', 'type': '1'}))


# f='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(f[22])
h='WR_FSC'.upper()
x=''
def c(a):
    x=''
    for i in a:
        f='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for b in range(1,len(f)+1):
            
            if i==f[b-1]:
                
                x+=str(b)+' '


    print(x)
    g=list(map(int,x.split()))

    r=''
    for i in g[:]       :
        r+=f[i-1]

    print(r)
c(h)
# c(h)
# g=[22,24,5,12,6,36,2,16,22,19,6,64,7,20,66,70,4 ]
# r=''
# f='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for i in g[:]       :
#         r+=f[i]

# print(r)
# g='20 8 9 19 23 9 12 12 8 5 12 16 25 15 21 6 9 14 4 25 15 21 18 11 5 25 2 21 20 4 15 14 15 20 2 5 4 21 16 5 4 3 21 20 4 15 23 14 20 8 5 23 15 15 4 19 20 8 5 25 2 5 5 18 4 15 19'
# print(g.replace(' ','-'))
# h=["https://fsc3301.pythonanywhere.com/"]

# import sshtunnel
# import mysql.connector

# sshtunnel.SSH_TIMEOUT = 5.0
# sshtunnel.TUNNEL_TIMEOUT = 5.0

# with sshtunnel.SSHTunnelForwarder(
#     ('ssh.pythonanywhere.com'),
#     ssh_username='FSC3301', ssh_password='alireza621',
#     remote_bind_address=('FSC3301.mysql.pythonanywhere-services.com', 3306)

# ) as tunnel:
#         con = mysql.connector.connect(
#             user='FSC3301', password='white&black',
#             host='127.0.0.1', port=tunnel.local_bind_port,
#             database='balcse$dbname',
#         )
#         c=con.cursor()
#         print(c.execute("SELECT VERSION(), CURRENT_DATE;"))
#         con.close()










