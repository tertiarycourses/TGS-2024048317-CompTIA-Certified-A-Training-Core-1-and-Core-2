# Lab 5 — Protocols and Ports — Building the A+ Port Reference

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Identify the TCP/UDP ports, transport protocol and secure replacement for every protocol on the CompTIA A+ Core 1 objective 2.1 list.

## Goal

You build the complete A+ port reference table from live evidence rather than memorisation: you query each service on a Killercoda Ubuntu playground, observe which transport it uses, and record the secure alternative where the protocol is insecure. The table becomes your revision sheet.

## What you'll produce

A complete 16-row port reference table with port number, transport, purpose, security status and secure replacement.

## Tools and equipment

Killercoda Ubuntu Playground (https://killercoda.com/playgrounds/scenario/ubuntu), ss, nmap, /etc/services

### Browser tools used in this lab

- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open https://killercoda.com/playgrounds/scenario/ubuntu in your browser and wait for the terminal prompt to appear. You have root access and nothing is installed on your own machine.
2. Update the package list and install the networking tools you need for this lab.

   ```bash
   apt-get update -qq && apt-get install -y net-tools iproute2 nmap dnsutils curl netcat-openbsd
   ```

3. Look up each A+ protocol in the system services database to confirm its official port and transport.

   ```bash
   grep -wE 'ftp|ssh|telnet|smtp|domain|bootps|bootpc|http|pop3|netbios-ssn|imap2|snmp|ldap|https|microsoft-ds' /etc/services
   ```

4. Record the port numbers for the file transfer and remote access group: FTP 20/21, SSH and SFTP 22, Telnet 23, RDP 3389.

   ```bash
   grep -wE 'ftp-data|ftp|ssh|telnet' /etc/services | head -20
   ```

5. Record the mail group: SMTP 25, POP3 110, IMAP 143, and note the secure TLS variants SMTPS 587/465, POP3S 995 and IMAPS 993.

   ```bash
   grep -wE 'smtp|pop3|imap2|imaps|pop3s|submission' /etc/services
   ```

6. Record the infrastructure group: DNS 53, DHCP 67 server and 68 client, and note that DNS uses UDP for queries and TCP for zone transfers.

   ```bash
   grep -wE 'domain|bootps|bootpc' /etc/services
   ```

7. Prove DNS runs over UDP by querying a public resolver and observing the transport used.

   ```bash
   dig +noall +stats google.com @8.8.8.8
   ```

8. Confirm HTTP on 80 and HTTPS on 443 by requesting headers from a live site and reading the response code.

   ```bash
   curl -sI https://www.tertiarycourses.com.sg | head -5
   ```

9. List every listening socket on the playground with its protocol, port and owning process, and identify which are TCP and which are UDP.

   ```bash
   ss -tulnp
   ```

10. Start a listener on a chosen port, then scan it from the same host to see how a scanner reports an open port.

   ```bash
   nc -l -p 8080 & sleep 1 && nmap -sT -p 8080 127.0.0.1
   ```

11. Complete the reference table with a Security column marking FTP, Telnet, HTTP, SNMPv1/v2 and POP3 as insecure, each with its secure replacement named.
12. Add the final rows for NetBIOS 137–139, SNMP 161/162, LDAP 389 and SMB/CIFS 445, then verify your table has all 16 protocols.

## Test it — verification

Your table lists all 16 protocols with the correct port, transport and purpose; every insecure protocol has its secure replacement named; and ss -tulnp output confirms at least one live listening socket with its transport.

## Troubleshooting this lab

| Symptom | What to check |
| --- | --- |
| A command returns "command not found" | Re-run the `apt-get install` step at the start of the lab — the playground starts with a minimal package set. |
| The Killercoda terminal has reset | The playground times out when idle. Reopen it and re-run the setup commands from step 1. |
| A browser tool will not load | Check the URL against `labs/tools.md`. All four tools run entirely client-side and need no login. |
| Output differs from the guide | Record what you actually observed — your environment differs from the reference, and explaining the difference is part of the exercise. |

## Review questions

1. State the exam objective this lab maps to, in your own words.
2. Which single step in this lab would you perform first on a real support call, and why?
3. What evidence would you attach to a support ticket to show this work was completed correctly?
4. Name one thing that would make this procedure fail, and how you would recognise it.

## Record your evidence

Complete [worksheet.md](worksheet.md) as you work through this lab and keep it — the Practical Performance assessment mirrors these tasks.

---

[← Labs index](../README.md)  ·  [Learner Guide](../../LG-CompTIA-Certified-A-Training-Core-1-and-Core-2.md)  ·  [Course page](https://www.tertiarycourses.com.sg/wsq-comptia-certified-a-training-core-1-and-core-2.html)
