# Import Libraries
from web3 import Web3
import time

# Sets web3 and provider
ethW3 = Web3(Web3.HTTPProvider('Add Infura Key Here'))

# Gets latest block details and number
startBlockDetails = ethW3.eth.get_block("latest")
startBlock = ethW3.eth.block_number

# Runs indefinitely
while True:
    # Prints new section, block number, and waits 60 seconds
    print("*----------------------*")
    print("Start Block: " + str(startBlock))
    time.sleep(60)
    
    # Gets the latest block and compares it to the old block to find the number of blocks that have since occured
    blockDetails = ethW3.eth.get_block("latest")
    blockNumber = ethW3.eth.block_number
    blockDistance = blockNumber - startBlock

    # Prints the most recent block and the block distance (number of blocks that have since occured)
    print("Latest Block: " + str(blockNumber))
    print("Block Distance: " + str(blockDistance))
    
    # Loop to get all of the burnt ethereum from the old block to the latest block
    for block in range(blockDistance):
        # Getting the block data
        currentBlock = ethW3.eth.get_block(startBlock + block)

        # Parsing the block data
        baseFee = int(currentBlock['baseFeePerGas'])
        gasUsed = currentBlock['gasUsed']
        
        # Getting the total amount of wei burnt
        totalBurnt = gasUsed * baseFee

        # Converting wei to ether
        ethTotalBurnt = ethW3.fromWei(totalBurnt, 'ether')

        # Rounding the number to 5 decimal places
        ethTotalBurnt = round(ethTotalBurnt, 5)

        # Printing out the results
        print("Block Number: " + str(startBlock + block) + " | " + "Amount Burned: " + str(ethTotalBurnt))
        
    # Setting new start block as the latest block
    startBlock = startBlock + blockDistance