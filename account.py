from algosdk import account, encoding, mnemonic
import os
from dotenv import load_dotenv
load_dotenv()

private_key, address=account.generate_account()

print("Private key: ",private_key)
print("Address:",address)

mnemon=mnemonic.from_private_key(private_key)
print("Mnemonic:",mnemon)

derived_private_key=mnemonic.to_private_key(mnemon)
print("Print key derived from mnemonic:",derived_private_key)

print("Comparision between two private keys:",private_key==derived_private_key)

env_private=os.getenv("PRIVATE_KEY")
print("Private key from .env:",env_private)

print("Address from .env:",account.address_from_private_key(env_private))

print(mnemonic.from_private_key(env_private))