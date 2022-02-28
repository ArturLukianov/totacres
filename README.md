# totacres
I solved more than 150 machines on TryHackMe and noticed that many of them are very similar.
This project tries to solve as much as possible TryHackMe boxes automated. It's not a pentest tool, please use it only in educational purposes.

## Tests
Machine|User|Root
-|-|-
[RootMe](https://tryhackme.com/room/rrootme)||
Simple CTF||
Basic Pentesting||

## Tools in chain
- nmap
- gobuster


## How to install
Clone this repository and install dependencies like this:
```bash
git clone https://github.com/ArturLukianov/totacres
```

## How to use
There is no usable tool for now. Click "Watch" and wait till it will be released.

## Structure
There are three main entities in this project: nodes, transformators and combinators. Nodes are representing a resource and transformators are taking a node and create new nodes from it. Combinators are used, to connect nodes, f.e. create a credential node from login and password nodes.
