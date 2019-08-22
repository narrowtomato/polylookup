import os

print("Enter lookups.  Type 'exit' to exit, or 'edit' to edit the servers.")

while True:

    userinput = input("polylookup> ")

    if userinput == "exit":
        break

    elif userinput == "edit":
        os.system("vi servers.txt")

    else:
        f = open("servers.txt")
        for serverip in f:
            #run nslookup using each server
            os.system("nslookup " + userinput + ' ' + serverip)
        f.close()
