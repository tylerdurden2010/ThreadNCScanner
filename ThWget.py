import threading,os,time
def GetSome(IP):
    command = "wget "+IP+" --wait=0.7 --max-redirect=0 --user-agent=\"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)\" -O index.html."+IP+""
    f = os.system(command)
    

IPHandle = open("IP","r")
test = IPHandle.readline()
test = test.strip('\n')
while test:
    for i in range(5):
        t = threading.Thread(target=GetSome,args=(test,))
        t.start()
        test = IPHandle.readline()
        test = test.strip('\n')
    time.sleep(5)
    test = IPHandle.readline()
    test = test.strip('\n')
exit(0)
