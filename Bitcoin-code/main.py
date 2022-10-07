import asyncio

from bitcoinrpc.bitcoin_rpc import BitcoinRPC




async def main():
#How to check balance. This is done using a library.
    async with BitcoinRPC("http://localhost:18443", "rpcuser", "rpcpassword") as rpc:
        print(await rpc.getbalance())
#How to get a new BTC address for receiving payments, which i again done using the library.
        address = await rpc.getnewaddress()
        print(address)
#How to send an amount to the new address
        print(await rpc.sendtoaddress(address, 0.2))
#How to list unspent transaction outputs
        print(await rpc.listunspent())




if __name__ == "__main__":
    asyncio.run(main())