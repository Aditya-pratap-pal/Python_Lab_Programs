# To demnonstrate the use of File writing and reading in text files, we
with open("file1.txt","w")as f:
    while(1==1):
        line=input("Enter the lines : ")
        f.write(line)
        f.wirte("\n")
        choice=input("are you done(Y/N) : ")
        if(choice.lower()=="y"):
            break
        else:
            pass
    f.close()
    print("Written in file Successfully")

with open("file1.txt","r")as g:
    print("Reading the file\n")
    print(g.read())