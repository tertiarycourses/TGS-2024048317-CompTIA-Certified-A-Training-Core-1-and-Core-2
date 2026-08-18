# Lab 54 — Professional Communication, Scripting and Remote Access

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 09:** Operational Procedures — Core 2, 21% of Core 2  
> **Exam objective:** Apply professional communication standards including handling difficult customers, and select appropriate scripting and remote access methods for support tasks (Core 2 objectives 4.7, 4.8 and 4.9).

## Goal

This final lab covers the three areas that decide whether a technically correct technician is actually effective: how they communicate, how they automate repetitive work, and how they reach a machine they cannot physically touch.

## What you'll produce

A professional communication guide with difficult-customer scenarios, an automation candidate list and a remote access selection matrix.

## Tools and equipment

Killercoda Ubuntu Playground, communication scenario briefs, remote access reference

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

1. Record the professional appearance and language standards: dress to the environment, use plain language, avoid jargon, acronyms and slang, and maintain a positive attitude.
2. Record the listening rules: listen actively without interrupting, and confirm understanding by restating the problem in your own words before you act on it.
3. Record the cultural sensitivity rules: use appropriate professional titles, be punctual and contact the customer if you will be late, and avoid distractions including personal calls and social media.
4. Record the rules for difficult customers: do not argue or become defensive, do not dismiss the problem, do not be judgmental, and clarify with open-ended questions.
5. Record the rules on confidentiality: do not post anything about a customer on social media, and treat everything encountered on a customer's system as confidential.
6. Work the scenario of a customer who is angry that the same fault has recurred three times, and write what you would actually say, applying the difficult-customer rules.
7. Work the scenario of a customer who insists on a solution you know is wrong, and write how you would set correct expectations without arguing.
8. Record the automation candidates from the objectives: restarting machines, remapping network drives, installing applications, running backups, gathering information and initiating updates.
9. Record the script types and where each is used: .bat and .ps1 on Windows, .vbs as legacy Windows, .sh on Linux and macOS, .py cross-platform and .js in browsers and Node.
10. Write and run a simple inventory script on the Killercoda playground that gathers the information a support ticket needs.

   ```bash
   cat > /root/inventory.sh << 'EOF'
   #!/bin/bash
   echo "=== System Inventory ==="
   echo "Hostname : $(hostname)"
   echo "OS       : $(grep PRETTY /etc/os-release | cut -d'\"' -f2)"
   echo "Kernel   : $(uname -r)"
   echo "CPU      : $(nproc) cores"
   echo "Memory   : $(free -h | awk '/^Mem:/ {print $2}')"
   echo "Disk     : $(df -h / | awk 'NR==2 {print $2" total, "$4" free"}')"
   echo "Uptime   : $(uptime -p)"
   EOF
   chmod +x /root/inventory.sh && /root/inventory.sh
   ```

11. Record the risks of scripting from the objectives: unintentionally changing system settings, browser or system crashes from resource exhaustion, and mishandling of credentials inside a script.
12. Build the remote access matrix comparing RDP, VNC, SSH, VPN and third-party screen sharing on platform, encryption, port and best use, and record the security consideration for each.

## Test it — verification

The inventory script runs and outputs all seven fields; both difficult-customer scenarios have written responses applying the stated rules; the matrix covers five remote access methods with port and security consideration; and the scripting risks are recorded.

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
