#!/usr/bin/env python3
# command: rhizom
"""
Description:
- set (key, watch endpoints)
- disperse stegonographic messages accross platforms
method:

Send:
- use key to encrypt the message and generate endpoint list
- break up message
- hide the message parts m_i using some method s_i
- scramble the time of the message parts m_i
- run as a system process and send


Background_Recieve:
- use key to generate sync. function sync(key) = s(seeds) eg time.
    + endpoints too like at and steg inverse methods. (ei,si)
    + s(-1)i reverse steg. methods to do
- poll endpoints
- apply inverse
- append to message_parts
- if complete append to inbox

args:
- config (key and list)
- send (message, recipient, by)
- (add, list, edit, delete ) (endpoint urls, logins)
- (add, list, edit, delete ) agents


# ideas/input
- use merkle trees and some form of error correction
Merkle Trees for Steganographic Messaging

Merkle trees would help verify message integrity without revealing the full message. Here's how they'd work in your system:

 1 Break message into chunks (m1, m2, m3, m4)
 2 Hash each chunk: h1=hash(m1), h2=hash(m2), etc.
 3 Build a tree: h12=hash(h1+h2), h34=hash(h3+h4), root=hash(h12+h34)
 4 Send the root hash through a separate channel (or embed in first message part)
 5 When receiving chunks, recipient rebuilds the tree and verifies against root

- apis:
    + user assisted/playwrite.
- timing : need to randomize but embed in normal user patterns. (eg every 3rd post)


Stego methods:
- semantic stego -> vary vocab
- exif data
- platform specific (twitter, reddit, insta)
- semantic stego in GIF is probably pretty easy.
    + vary colours or something

"""

def config():
    pass

def send(msg, receiver, deadline):
    pass

def general_list():
    pass

def add_or_edit():
    pass

def delete():
    pass


async def main():
    parser = argparse.ArgumentParser(description="secure stegonographic messaging")
    args = parser.parse_args()

if __name__ == '__main__':
    asyncio.run(main())
