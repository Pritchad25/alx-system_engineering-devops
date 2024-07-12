# Project Title: Web stack debugging #0

## Table of Contents
1. About
2. Learning Objectives
3. Requirements
4. Getting Started
5. Contributing
6. License

## About <a name="about"></a>
This project is part of the curriculum of the ALX Software Engineering program. The main objective of this project is to understand and implement Web Stack Debugging.
### Background Context
- The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

- Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

- In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

- Let’s start with a very simple example. My server must:
have a copy of the `/etc/passwd` file in `/tmp`
have a file named `/tmp/isworking` containing the string `OK`

- Let’s pretend that without these 2 elements, my web application cannot work.

- Let’s go through this example and fix the server.
```
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
```
Then my answer file would contain:
```
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
```
Note that as you cannot use interactive software such as `emacs` or `vi` in your Bash script, everything needs to be done from the command line (including file edition).

## Learning Objectives <a name="learning-objectives"></a>
- Web stack debugging

## Requirements <a name="requirements"></a>
- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- A `README.md` file, at the root of the folder of the project, describing what each script is doing
- Your Bash script must pass `Shellcheck` (version `0.7.0`) without any error
- All your files must be executable
- Your Bash scripts must run without error

## Getting Started <a name="getting-started"></a>
1. Clone this repository: `git clone https://github.com/Pritchad25/alx-system_engineering-devops.git`
2. Access the project directory: `cd 0x0D-web_stack_debugging_0`
3. Run any executable script within the directory

## Contributing <a name="contributing"></a>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License <a name="license"></a>
ALX 2024 - [alxafrica](https://www.alxafrica.com)
