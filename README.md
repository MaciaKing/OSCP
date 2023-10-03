# OSCP
This repository is a cheat.

# Privilage Escalation
- `hostname`: The hostname command will return the hostname of the target machine. Although this value can easily be changed or have a relatively meaningless string (e.g. Ubuntu-3487340239), in some cases, it can provide information about the target system’s role within the corporate network (e.g. SQL-PROD-01 for a production SQL server).

- `uname -a`: Will print system information giving us additional detail about the kernel used by the system. This will be useful when searching for any potential kernel vulnerabilities that could lead to privilege escalation.

- `/proc/version`: The proc filesystem (procfs) provides information about the target system processes. You will find proc on many different Linux flavours, making it an essential tool to have in your arsenal.
Looking at `/proc/version` may give you information on the kernel version and additional data such as whether a compiler (e.g. GCC) is installed.

- `/etc/issue`: Systems can also be identified by looking at the /etc/issue file. This file usually contains some information about the operating system but can easily be customized or changed. While on the subject, any file containing system information can be customized or changed. For a clearer understanding of the system, it is always good to look at all of these.

- `ps` Command: The `ps` command is an effective way to see the running processes on a Linux system. Typing `ps` on your terminal will show processes for the current shell.

    The output of the `p` (Process Status) will show the following;
    - PID: The process ID (unique to the process)
    - TTY: Terminal type used by the user
    - Time: Amount of CPU time used by the process (this is NOT the time this process has been running for)
    - CMD: The command or executable running (will NOT display any command line parameter)

    The “ps” command provides a few useful options.
    - `ps -A`: View all running processes
    - `ps axjf`: View process tree (see the tree formation until `ps axjf` is run below)
    - `ps aux`: The `aux` option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.

- `env`: The `env` command will show environmental variables. The PATH variable may have a compiler or a scripting language (e.g. Python) that could be used to run code on the target system or leveraged for privilege escalation.

- `sudo -l`: The target system may be configured to allow users to run some (or all) commands with root privileges. The `sudo -l` command can be used to list all commands your user can run using `sudo`.

- `id`: The `id` command will provide a general overview of the user’s privilege level and group memberships.
It is worth remembering that the `id` command can also be used to obtain the same information for another user as seen below.

- `/etc/passwd`: Reading the `/etc/passwd` file can be an easy way to discover users on the system. Interesting view: `cat /etc/passwd | cut -d ":" -f 1`.
Remember that this will return all users, some of which are system or service users that would not be very useful. Another approach could be to grep for “home” as real users will most likely have their folders under the “home” directory: `cat /etc/passwd | grep home`.

- `history`: Looking at earlier commands with the `history` command can give us some idea about the target system and, albeit rarely, have stored information such as passwords or usernames.