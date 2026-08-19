# Lab 5 Worksheet — Protocols and Ports — Building the A+ Port Reference

**Name:** ______________________    **Date:** ______________

**Exam objective:** Identify the TCP/UDP ports, transport protocol and secure replacement for every protocol on the CompTIA A+ Core 1 objective 2.1 list.

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open https://killercoda.com/playgrounds/scenario/ubuntu in your browser and wait for the terminal prompt to appear. You have root access and nothing is installed on your own machine. |  |
| 2 | Update the package list and install the networking tools you need for this lab. |  |
| 3 | Look up each A+ protocol in the system services database to confirm its official port and transport. |  |
| 4 | Record the port numbers for the file transfer and remote access group: FTP 20/21, SSH and SFTP 22, Telnet 23, RDP 3389. |  |
| 5 | Record the mail group: SMTP 25, POP3 110, IMAP 143, and note the secure TLS variants SMTPS 587/465, POP3S 995 and IMAPS 993. |  |
| 6 | Record the infrastructure group: DNS 53, DHCP 67 server and 68 client, and note that DNS uses UDP for queries and TCP for zone transfers. |  |
| 7 | Prove DNS runs over UDP by querying a public resolver and observing the transport used. |  |
| 8 | Confirm HTTP on 80 and HTTPS on 443 by requesting headers from a live site and reading the response code. |  |
| 9 | List every listening socket on the playground with its protocol, port and owning process, and identify which are TCP and which are UDP. |  |
| 10 | Start a listener on a chosen port, then scan it from the same host to see how a scanner reports an open port. |  |
| 11 | Complete the reference table with a Security column marking FTP, Telnet, HTTP, SNMPv1/v2 and POP3 as insecure, each with its secure replacement named. |  |
| 12 | Add the final rows for NetBIOS 137–139, SNMP 161/162, LDAP 389 and SMB/CIFS 445, then verify your table has all 16 protocols. |  |

## Verification

**Success criterion:** Your table lists all 16 protocols with the correct port, transport and purpose; every insecure protocol has its secure replacement named; and ss -tulnp output confirms at least one live listening socket with its transport.

- [ ] I completed every step in the lab.
- [ ] My result meets the success criterion above.
- [ ] I recorded my evidence (screenshots, output, completed tables).

## Reflection

**What surprised you in this lab?**

_______________________________________________________________

**Where would you apply this on the job?**

_______________________________________________________________

**What do you still need to revise before the exam?**

_______________________________________________________________
