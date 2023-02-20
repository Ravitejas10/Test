# Unix Commands
adduser
addgroup
cat
cd
chmod
chown
clear
cp
cut
date
deluser, delgroup, echo, find, grep, head, history, ls, man, mkdir
## 1. adduser
- Adding users on a Linux system

        sudo adduser r

        Adding user `r' ...
        Adding new group `r' (1000) ...
        Adding new user `r' (1000) with group `r' ...
        Creating home directory `/home/r' ...
        Copying files from `/etc/skel' ...
        New password: 
        Retype new password: 
        passwd: password updated successfully
        Changing the user information for r
        Enter the new value, or press ENTER for the default
            Full Name []: Ravi
	        Room Number []: 10
	        Work Phone []: 
	        Home Phone []: 
	        Other []: 
        Is the information correct? [Y/n] y

## 2. addgroup
- addgroup command in Linux is used to add a new group to your current Linux machine

        ravi@ravi-Latitude-5531:~/perfios$ sudo addgroup rt
        Adding group `rt' (GID 1002) ...
        Done.

## 3. cat
- Cat(concatenate) command is very frequently used in Linux. It reads data from the file and gives their content as output. It helps us to create, view, concatenate files.

        $cat filename

## 4. cd
- The cd command can be used to change into a subdirectory, move back into the parent directory, move all the way back to the root directory or move to any given directory.

        ravi@ravi-Latitude-5531:~/perfios$ cd
        ravi@ravi-Latitude-5531:~$ cd Desktop
        ravi@ravi-Latitude-5531:~/Desktop$ 

## 5. chmod
- the chmod command is used to change the access mode of a file

        chmod [reference][operator][mode] file... 

- r       Permission to read the file.
- w       Permission to write (or delete) the file.
- x       Permission to execute the file, or, in
        the case of a directory, search it.

## 6. chown
- chown command is used to change the file Owner or group. Whenever you want to change ownership you can use chown command.
  - To Change group ownership In our case I am using group1 as a group in the system. To change ownership we will use

        chown :group1 file1.txt
- the group permissions changes to group1 from roo

## 7. clear
- clear is a standard Unix computer operating system command that is used to clear the terminal screen

        $clear

## 8. cp
- cp stands for copy. This command is used to copy files or group of files or directory. It creates an exact image of a file on a disk with different file name. cp command require at least two filenames in its arguments.

        cp Src_file Dest_file

## 9. cut
- The cut command in UNIX is a command for cutting out the sections from each line of files and writing the result to standard output. It can be used to cut parts of a line by byte position, character and field. 

        In this, 1- indicate from 1st byte to end byte of a line
        $ cut -b 1- state.txt
        Andhra Pradesh
        Arunachal Pradesh
        Assam
        Bihar
        Chhattisgarh
        
        In this, -3 indicate from 1st byte to 3rd byte of a line
        $ cut -b -3 state.txt
        And
        Aru
        Ass
        Bih
        Chh

## 10. date
- date command is used to display the system date and time

        ravi@ravi-Latitude-5531:~$ date
        Friday 17 February 2023 11:25:45 AM IST

## 11. deluser
- this command removes the user's profile 

        sudo deluser sam

## 12. delgroup
- this command removes all user-to-group connections for the user. 

        sudo delgroup sales

## 13. echo
- Echo is a Unix/Linux command tool used for displaying lines of text or string which are passed as arguments on the command line. 

        echo -e "ravi \ntejas"

## 14. find
- The find command helps us to find a particular file within a directory

        find . -name "*.txt" 
- We can search all the files ending with the extension '.txt.' 

## 15. grep
- The 'grep' command stands for "global regular expression print". grep command filters the content of a file which makes our search easy.

        grep 9 marks.txt
- grep command filters all the data containing '9'

## 16. head
- it prints the first 10 lines of the specified files

        $ head state.txt

## 17. history
- history command is used to view the previously executed command

        $ history
## 18. ls
- ls–Lists the names of files in a particular Unix directory

        $ ls

## 19. man
- man command in Linux is used to display the user manual of any command that we can run on the terminal

        $ man printf

## 20. mkdir
-  The mkdir command in Linux/Unix allows users to create or make new directories.

        mkdir file1

#mv, passwd, shutdown, ssh, scp, rsync, ps, rm ,rmdir,tail, touch,uname,which
## 21. mv
- mv stands for move. mv is used to move one or more files or directories from one place to another in a file system

        mv geek.txt b.txt
- moving geeks.txt to b.txt

## 21. passwd
- passwd command in Linux is used to change the user account password

        sudo passwd root 
## 22. shutdown
- The shutdown command in Linux is used to shutdown the system in a safe way.

        sudo shutdown now

## 23. ssh
- The ssh command provides a secure encrypted connection between two hosts over an insecure network. This connection can also be used for terminal access, file transfers, and for tunneling other applications.
- ssh stands for “Secure Shell”. It is a protocol used to securely connect to a remote server/system. ssh is secure in the sense that it transfers the data in encrypted form between the host and the client

        ssh user_name@host(IP/Domain_name)
- ssh command consists of 3 different parts:

  - ssh command instructs the system to establish an encrypted secure connection with the host machine.
  - user_name represents the account that is being accessed on the host.
  - host refers to the machine which can be a computer or a router that is being accessed. It can be an IP address (e.g. 192.168.1.24) or domain name(e.g. www.domainname.com).

## 24. scp
- scp (secure copy) command in Linux system is used to copy file(s) between servers in a secure way. 
- The SCP command or secure copy allows secure transferring of files in between the local host and the remote host or between two remote hosts

        scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2
- OPTIONS - They grant different permissions depending on how they have been used. Some of the most common options include:
- P(Caps) - specifies the port to establish connection with the remote host.
- p(lowercase) - preserves the times-tamp for ease of modification and access.
- r - copies the entire directory recursively
- q - copies files quietly, doesn't display the progress messages. Also known as quiet mode.
- C - for compression of data during transmission.

- src_host - where the file is hosted. The source can either be a client or server depending on the origin of the file.
- dest_host - where the file will be copied to.

## 25. rsync
- rsync or remote synchronization is a software utility for Unix-Like systems that efficiently sync files and directories between two hosts or machines.
- There are basically two ways in which rsync can copy/sync data:
  - Copying/syncing to/from another host over any remote shell like ssh, rsh.
  - Copying/Syncing through rsync daemon using TCP.

        Syntax of rsync:
        rsync [options] source [destination]
  
## 26. ps
- Linux provides us a utility called ps for viewing information related with the processes on a system which stands as abbreviation for “Process Status”.
- ps command is used to list the currently running processes and their PIDs 

        ps [options]
## 27. rm
- rm stands for remove here. rm command is used to remove objects such as files, directories, symbolic links and so on from the file system like UNIX

        rm a.txt

## 28. rmdir
- rmdir command is used remove empty directories from the filesystem in Linux.

        rmdir mydir1 

## 29. tail
- The tail command, as the name implies, print the last N number of data of the given input. 
- By default it prints the last 10 lines of the specified files

        tail [OPTION]... [FILE]...
        tail state.txt

## 30. touch
- The touch command is a standard command used in UNIX/Linux operating system which is used to create, change and modify timestamps of a file

        touch file_name

## 31. uname
- The command ‘uname‘ displays the information about the system

        uname [OPTION]

## 32. which
- The which command allows users to search the list of paths in the $PATH environment variable and outputs the full path of the command specified as an argument

        which -a touch
- The which command has only one option, -a. It is optional and used to print all the matches it finds.

#ssh keys in github