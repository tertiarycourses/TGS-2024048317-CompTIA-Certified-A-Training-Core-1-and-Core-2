# Lab 30 — Windows Command Line — Navigation, Files and Copy Operations

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Use the Windows command line for navigation, file management and resilient copy operations, choosing correctly between copy, xcopy and robocopy (Core 2 objective 1.2).

## Goal

You work the Windows command line the way a technician does during a migration or a repair, when the GUI is unavailable or too slow. The lab ends on robocopy, because it is the tool that actually survives a large real-world file migration.

## What you'll produce

A command reference sheet and a completed file migration performed with robocopy, verified against the source.

## Tools and equipment

Windows PC, Command Prompt, PowerShell

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open Command Prompt as administrator and confirm your starting location and the commands available.

   ```bash
   cd && help | more
   ```

2. Practise navigation: move between directories, move up one level, and return to the drive root.

   ```bash
   cd C:\Users && cd .. && cd \
   ```

3. List directory contents with the switches that matter: all files including hidden, and a recursive listing.

   ```bash
   dir /a && dir /s /b C:\Windows\System32\*.msc
   ```

4. Create a directory structure for the exercise and confirm it exists.

   ```bash
   md C:\aplus-lab\source && md C:\aplus-lab\dest && dir C:\aplus-lab
   ```

5. Create test files with content so the copy operations have something real to move.

   ```bash
   echo Test file one > C:\aplus-lab\source\file1.txt && echo Test file two > C:\aplus-lab\source\file2.txt
   ```

6. Use copy for a single file and record its limitation — it copies files only and cannot handle directory trees.

   ```bash
   copy C:\aplus-lab\source\file1.txt C:\aplus-lab\dest\ && dir C:\aplus-lab\dest
   ```

7. Use xcopy with the switches for subdirectories including empty ones, and record that it handles trees but cannot resume.

   ```bash
   xcopy C:\aplus-lab\source C:\aplus-lab\dest /E /I /Y
   ```

8. Use robocopy to mirror the source to the destination, which is the correct tool for a real migration.

   ```bash
   robocopy C:\aplus-lab\source C:\aplus-lab\dest /MIR /R:2 /W:2 /LOG:C:\aplus-lab\copy.log
   ```

9. Read the robocopy log and record the files copied, skipped and failed, and the total bytes transferred.

   ```bash
   type C:\aplus-lab\copy.log
   ```

10. Record why robocopy is the right choice for migrations: it retries failed files, resumes interrupted transfers, preserves attributes and timestamps, and logs everything.
11. Warn on the /MIR switch: it makes the destination identical to the source, which means it deletes files in the destination that are not in the source. Verify the destination before every mirror.
12. Verify the migration by comparing both directories, then clean up the exercise files.

   ```bash
   dir C:\aplus-lab\source /b && dir C:\aplus-lab\dest /b && rd /s /q C:\aplus-lab
   ```


## Test it — verification

Every command executes without error, the robocopy log confirms the expected file count copied, your reference sheet states the specific limitation of copy and xcopy that robocopy overcomes, and the /MIR deletion warning is recorded.

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
