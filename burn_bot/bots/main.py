import tweepy
import logging
from config import create_api
import time

from web3 import Web3
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

##  Any functions can go here   ##
def burnWatch(api):
    ethW3 = Web3(Web3.HTTPProvider('Infura Key Goes Here'))

    # Gets latest block details and number
    startBlock = ethW3.eth.block_number

    blockList = []

    while True:
        blockNumber = ethW3.eth.block_number
        blockDistance = blockNumber - startBlock

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

            # Tweeting when a large amount of ether is burned
            if(ethTotalBurnt > 4.99):
                api.update_status("In block " + str(currentBlock['number']) + " over " + str(round(ethTotalBurnt, 2)) + " ether was burned!" + " \U0001F525")

            blockList.append(ethTotalBurnt)

        # Setting new start block as the latest block
        startBlock = startBlock + blockDistance

        # Tweeting the average and total amount of ether burned over 1000 blocks, roughly 3 hours or 8 times a day
        if(len(blockList) > 1000):
            blockListAvg = round(sum(blockList)/len(blockList), 4)
            api.update_status("Over the last " + str(len(blockList)) + " blocks " + str(round(blockListAvg, 4)) + " ether was burned on average, and over " + str(round(sum(blockList), 4)) + " ether was burned in total! " + " \U0001F525")

            blockList = []

        time.sleep(120)

def main():
    api = create_api()
    burnWatch(api)
    #api.update_status("hello there!")

if __name__ == "__main__":
    main()
