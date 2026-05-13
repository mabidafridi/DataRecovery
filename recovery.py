drive = "\\\\.\\G:"  #Open Drive as raw bytes
fileD=open(drive, "rb")
size = 512
byte = fileD.read(size)
offs=0
drec = False
rcvd = 0
while byte:
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >=0:
        drec = True
        print("Found JPG at location:" +str(hex(found+(size*offs)))+ "======")
        fileN = open ('1\\' + str(hex(found+(size*offs))), 'wb')
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
        if byte.find(b'\xff\xd9') != -1:
            fileN.write(byte[:byte.find(b'\xff\xd9')+2])
            fileN.close()
            print("End of JPG at location:" +str(hex(found+(size*offs)))+ "======")
            drec = False
        else:
            fileN.write(byte)
    byte = fileD.read(size)
    offs+=1
    
fileD.close()
        
