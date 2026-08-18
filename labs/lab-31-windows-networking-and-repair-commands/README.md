# Lab 31 — Windows Networking and Repair Commands

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Use Windows networking and repair commands to diagnose connectivity and repair system file corruption (Core 2 objective 1.2).

## Goal

You run the diagnostic and repair commands that appear directly in the Core 2 objectives, interpreting the output of each rather than merely executing it — because in support work the output is the diagnosis.

## What you'll produce

A command output interpretation record and a completed system file integrity check with results explained.

## Tools and equipment

Windows PC, Command Prompt as administrator, PowerShell

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Display the full network configuration and record the IP address, subnet mask, default gateway, DNS servers, DHCP server and MAC address.

   ```bash
   ipconfig /all
   ```

2. Release and renew the DHCP lease, recording the address before and after to confirm the DHCP server responded.

   ```bash
   ipconfig /release && ipconfig /renew
   ```

3. Display and then clear the DNS resolver cache, and record when clearing it is the correct fix — after a DNS record changes but the old answer is still cached.

   ```bash
   ipconfig /displaydns | more && ipconfig /flushdns
   ```

4. Test the loopback address first to confirm the TCP/IP stack itself is working before testing anything external.

   ```bash
   ping 127.0.0.1
   ```

5. Test the default gateway to separate a local network fault from an internet fault.

   ```bash
   ping -n 4 %GATEWAY%
   ```

6. Test an external IP address and then an external name, and record that success on the IP but failure on the name isolates the fault to DNS.

   ```bash
   ping -n 4 8.8.8.8 && ping -n 4 www.tertiarycourses.com.sg
   ```

7. Trace the route to a destination and identify where latency increases sharply or where the path stops.

   ```bash
   tracert -h 12 www.tertiarycourses.com.sg
   ```

8. Query DNS directly and record the resolver used and the addresses returned.

   ```bash
   nslookup www.tertiarycourses.com.sg
   ```

9. List active connections with the owning process ID so you can identify what is actually using the network.

   ```bash
   netstat -ano | findstr ESTABLISHED
   ```

10. Run the system file checker to scan and repair protected system files, and record the result it reports.

   ```bash
   sfc /scannow
   ```

11. Repair the component store that sfc itself depends on, and record why DISM must be run first when sfc reports it cannot fix the files.

   ```bash
   DISM /Online /Cleanup-Image /RestoreHealth
   ```

12. Check the disk for file system errors, and record the difference between /f which fixes errors and /r which also locates bad sectors and takes far longer.

   ```bash
   chkdsk C: /scan
   ```


## Test it — verification

Every command produces output you have interpreted in writing; ipconfig /all output identifies all six required fields; you correctly state that ping to IP succeeding while ping to name fails means DNS; and the sfc result is recorded with its meaning.

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
