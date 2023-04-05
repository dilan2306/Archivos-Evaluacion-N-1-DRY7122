ACLNum = int(input("Cual es el número IPV4 ACL? "))
if ACLNum >= 1 and ACLNum <= 99:
    print("Este es un ACL IPv4 estándar.")
elif ACLNum >=100 and ACLNum <= 199:
    print("Este es una ACL IPv4 extendida")
else:
    print("Esta ACL IPv4 no es extendida o estandar .")

