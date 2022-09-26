import subprocess
import os

def system(cmd):
    os.system(cmd)

proc = subprocess.Popen(['bitcoin-cli getblockcount'], stdout=subprocess.PIPE, shell=True)
out = proc.communicate()
out = out[0]
end = out.decode()
end = int(str(end).rstrip('\n'))

print('Current block count = '+str(end)+'.')
# int(input('Current block count = '+str(end)+', starting block?'))
start=int(input('Starting block? '))
end = int(input('Ending block? '))
iterate = int(start)

lastblock=0
diff=[int(iterate),int(lastblock)]

while iterate<end:
    proc = subprocess.Popen(['bitcoin-cli getblockstats '+str(iterate)+' | jq .mediantime'], stdout=subprocess.PIPE, shell=True)
    out = proc.communicate()
    out = out[0]
    out = out.decode()

    if lastblock != 0:
        currentblock=int(out)
        if currentblock-lastblock > diff[1]:
            diff[0]=iterate
            diff[1]=currentblock-lastblock
            # system('clear')
            print('Block range '+str(start)+' to '+str(end)+', as of block '+str(iterate)+', the longest block interval is block '+str(diff[0])+' with '+str(diff[1])+' seconds.')
        else:
            # system('clear')
            print('Block range '+str(start)+' to '+str(end)+', as of block '+str(iterate)+', the longest block interval is block '+str(diff[0])+' with '+str(diff[1])+' seconds.')
        lastblock=int(currentblock)
    else:
        lastblock = int(out)
    iterate +=1