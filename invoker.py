from random import choice,randint,shuffle
from select import select
import sys
qwe = dict(q='Quas',w='Wex',e='Exort')
dic = {1:'q',2:'w',3:'e'}
spells = dict(qwe='DEAFENINGBLAST',qqq='COLDSNAP', qqe='ICEWALL', qee='FORGESPIRIT', eee='SUNSTRIKE', qqw='GHOSTWALK', wee='CHAOSMETEOR', qww='TORNADO', wwe='ALACRITY', www='EMP')

#Loop random 500 - 400 time
for x in range(randint(50,400)):

    #random key for dic
    c1 = randint(1,3)
    c2 = randint(1,3)
    c3 = randint(1,3)
    cf = [c1,c2,c3]

    #sort 
    cf.sort()

    #choose dic #choose q-w-e 
    d1 = dic[cf[0]]
    d2 = dic[cf[1]]
    d3 = dic[cf[2]]


    #final dic for key spells 
	#key for spelss is ready 
    dd = d1+d2+d3
    
    #for output
    #qwe in array to randomize
    da = [d1,d2,d3]

    #shuffle the output spell
    shuffle(da)

    #selected spells
    sc = spells[dd]
    
    #Set up Quas Wex Exort
    ow = qwe[da[0]]+" "+qwe[da[1]]+" "+qwe[da[2]]+"\n"
    
    sys.stdout.write("\n")
    sys.stdout.write(ow)
    sys.stdout.flush()
    sys.stdout.write("\nWhat spells invoker cast: ")
    sys.stdout.flush()

    #input here
    ip = sys.stdin.readline().rstrip().lstrip()
    
    #check the input
    if(str(ip) == str(sc)):
    	continue
    else:
    	print("Dont Play Mobile Legend to Much Kiddo")
    	sys.exit()

print("Flag{As_Indeed_Iam_First_In_Everything}")
