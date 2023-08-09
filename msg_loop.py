def MsgLoopSender(msgs, qnt):
    import pynput, random, time
    from pynput.keyboard import Key, Controller
    import math
    
    keyboard = Controller()
    print("Iniciando em 5s")
    time.sleep(1)
    print("Iniciando em 4s")
    time.sleep(1)
    print("Iniciando em 3s")
    time.sleep(1)
    print("Iniciando em 2s")
    time.sleep(1)
    print("Iniciando em 1s")
    time.sleep(1)
    print("Iniciado !")    
    for i in range(0, qnt):
        W = random.randint(0, len(msgs)-1)
        for c in msgs[W]:
            keyboard.press(c)
            keyboard.release(c)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)

msg = ["Je t’aime", "Eu te amo","Ti voglio bene","Ti amo","Te quiero","I love you","Seni seviyorum","Te dua","Ek het jou liefe or Ek is lief vir jou","Wo ai ni","S’agapo","Ana behibek","Volim te","Mahal kita"]
qnt = 140 

for i in f:
    msg.append(i.split("=")[1][1::].replace("\n",""))'''
msgreal = []
for i in range(0, len(msg)):
    msgreal.append(msg[i])


MsgLoopSender(msgreal, qnt)
