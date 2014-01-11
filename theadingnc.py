import threading,os,time
def ncDetect(IP):
    command = "nc -v -z " + IP +" 21-9000 2>&1| grep succeed"
    f = os.system(command)
    

IPHandle = open("IP","r")
test = IPHandle.readline()
test = test.strip('\n')
while test:
    for i in range(5):
        t = threading.Thread(target=ncDetect,args=(test,))
        t.start()
        test = IPHandle.readline()
        test = test.strip('\n')
    time.sleep(5)
    test = IPHandle.readline()
    test = test.strip('\n')
