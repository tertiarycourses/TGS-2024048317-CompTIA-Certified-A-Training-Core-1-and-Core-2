# Lab 34 — Linux Command Line Essentials on Killercoda

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Use the Linux commands named in Core 2 objective 1.11 for navigation, file management, searching, process control and package management (Core 2 objective 1.11).

## Goal

You work every Linux command the A+ objectives name, on a real Ubuntu machine in the browser. Each command is run against real files and real output so the behaviour, not just the syntax, is what you take away.

## What you'll produce

A verified Linux command reference with real output recorded for each command in the objective list.

## Tools and equipment

Killercoda Ubuntu Playground (https://killercoda.com/playgrounds/scenario/ubuntu)

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

1. Open https://killercoda.com/playgrounds/scenario/ubuntu and wait for the terminal. Confirm where you are and who you are running as.

   ```bash
   pwd && whoami && id
   ```

2. Install the packages this lab uses and note that apt is the package manager on Debian and Ubuntu.

   ```bash
   apt-get update -qq && apt-get install -y tree htop nano less
   ```

3. Create a working directory tree and confirm its structure visually.

   ```bash
   mkdir -p ~/aplus/{docs,logs,scripts} && tree ~/aplus
   ```

4. Create files with content so the later commands have real data to operate on.

   ```bash
   echo 'ERROR: disk full on /dev/sda1' > ~/aplus/logs/system.log && echo 'INFO: service started' >> ~/aplus/logs/system.log && echo 'ERROR: network timeout' >> ~/aplus/logs/system.log
   ```

5. List files with the long format showing permissions, ownership, size and modification time, including hidden files.

   ```bash
   ls -la ~/aplus/logs
   ```

6. Display file contents with cat, then page through a longer file with less to see how each is used.

   ```bash
   cat ~/aplus/logs/system.log && ls -la /etc | less -E -X | head -20
   ```

7. Search file contents with grep, which is the command you use to find an error in a log.

   ```bash
   grep -n 'ERROR' ~/aplus/logs/system.log && grep -c 'ERROR' ~/aplus/logs/system.log
   ```

8. Find files by name and by type across a directory tree.

   ```bash
   find /etc -name '*.conf' -type f 2>/dev/null | head -10
   ```

9. Copy, move and rename files, then confirm the result of each operation.

   ```bash
   cp ~/aplus/logs/system.log ~/aplus/docs/backup.log && mv ~/aplus/docs/backup.log ~/aplus/docs/archived.log && ls -l ~/aplus/docs
   ```

10. Check storage and memory usage, which are the first two things to check on a Linux machine reported as slow.

   ```bash
   df -h && du -sh ~/aplus && free -h
   ```

11. List running processes and identify the top consumers, then record how you would terminate a runaway process.

   ```bash
   ps aux --sort=-%mem | head -8 && echo 'Terminate with: kill <PID> or kill -9 <PID>'
   ```

12. Change file permissions and ownership, then verify both, and record the numeric meaning of the mode you set.

   ```bash
   chmod 640 ~/aplus/logs/system.log && ls -l ~/aplus/logs/system.log && echo '640 = owner rw-, group r--, others ---'
   ```


## Test it — verification

Every command runs without error on the playground; grep returns exactly two ERROR lines from the log; ls -l confirms the 640 permission as rw-r-----; and your reference records real output for each command rather than expected output.

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
