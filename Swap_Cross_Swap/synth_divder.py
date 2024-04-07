# This program opens a subprocess module for a script to run

import subprocess,time
print('updated 1')
take_action =  True
while take_action:
    subprocess.Popen(['python3','mainSynth.py','arbitrumBot_1'])
    time.sleep(5)
    #subprocess.Popen(['python3','mainSynth.py','arbitrumBot_2'])
    #time.sleep(10)
    #subprocess.Popen(['python3','mainSynth.py','arbitrumBot_3'])
    #time.sleep(10)
    #subprocess.Popen(['python3','mainSynth.py','arbitrumBot_4'])
    print('WAITING FOR THE NEXT 30 MINUTE')
    time.sleep(1800)
