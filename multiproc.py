# 
# This module is written to test a hypothesis on the behaviour of the ready()
# and successful() function on Pool objects in the multiprocessing module.
#  
import os
import multiprocessing 
# 
# Define the maximum number of concurrent processes
# 
MAX_PROCS = 50
# 
# Some data in a list form
# 
list = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5]]
# 
# The method on which we'll apply asynchronous processing
# 
def proofOfConcept( someList ):
    someList.append( someList[0] + str( someList[1] ) )
    someList.append( True )
    return someList
    # End of proofOfConcept
# 
# The prototype
# 
pool = multiprocessing.Pool(None)
# 
inLoop = True
curProcs = 0
curListRow = 0
result = []
# 
# 
# 
while inLoop and curListRow < len( list ):
    # 
    # The Process Spawning Loop
    # 
    if curProcs < MAX_PROCS :
        # 
        # Spawn new processes
        # 
        # reslist = ['Alphabet', <Number>, 'Alphanumeric']
        resList = pool.apply_async( proofOfConcept, list[curListRow] )
        # result = [['Alphabet', <Number>, 'Alphanumeric', False],
        #           ['Alphabet', <Number>, 'Alphanumeric', False], ...]
        result.append( resList )
        # 
        # It is necessary to increment the number of processes
        # 
        curProcs += 1
        curListRow += 1
        # 
        # End if
        # 
    else:
        break
        # 
        # End else
        # 
    if curListRow == len( list ):
        # 
        # If the last row in the list has been reached, the multiprocessing
        # part in this while loop has to be ommitted. So "inLoop" has been set
        # to False to force fail one half of the if check for multiprocessing.
        # 
        inLoop = False
    # 
    # The Processing Loop
    # 
    if inLoop and not result[3]:
        if result[2].ready():
            result[3] = True
    
    #
    # End of first while
    #
# 
# second while loop
# 

# close / join / write queues (and block while doing so)
pool.close()
pool.join()

# Print the result
os.system( 'echo ' + str( result ) )
