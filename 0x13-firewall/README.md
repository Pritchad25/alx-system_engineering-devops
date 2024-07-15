# Project Title: Firewall

## Table of Contents
1. About
2. Learning Objectives
3. Requirements
4. Getting Started
5. Contributing
6. License

## About <a name="about"></a>
This project is part of the curriculum of the ALX Software Engineering program. The main objective of this project is to understand and implement implement a firewall in a server.
<img width="30px" src="https://imgur.com/a/779yeGK" alt="Firewall"/>

## Background Context
### More Info
- `telnet` is a very good tool to check if sockets are open with `telnet IP PORT`.For example, if you want to check if port 22 is open on `web-02`:
```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
- We can see for this example that the connection is successful: `Connected to web-02.holberton.online.`
- Now let’s try connecting to port 2222:
```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
```
- We can see that the connection never succeeds, so after some time I just use `ctrl+c` to kill the process.
- This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.
- Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on `web-01`, please perform the test from outside of the school network, like from your `web-02` server. If you SSH into your `web-02` server, the traffic will be originating from `web-02` and not from the school’s network, bypassing the firewall.

## Learning Objectives <a name="learning-objectives"></a>
At the end of this project, I am expected to be able to explain to anyone, without the help of Google:
- how to implement a firewall in one or more servers.

## Requirements <a name="requirements"></a>
- Containers on demand cannot be used for this project (Docker container limitation)
- Be very careful with firewall rules! For instance, if you ever deny port `22/TCP` and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

## Getting Started <a name="getting-started"></a>
1. Clone this repository: `git clone https://github.com/Pritchad25/alx-system_engineering-devops.git`
2. Access the project directory: `cd 0x13-firewall`
3. Run any executable file within the directory.

## Contributing <a name="contributing"></a>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License <a name="license"></a>
ALX 2024 - [alxafrica](https://www.alxafrica.com)

