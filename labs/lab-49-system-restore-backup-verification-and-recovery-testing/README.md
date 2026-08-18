# Lab 49 — System Restore, Backup Verification and Recovery Testing

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 08:** Software Troubleshooting — Core 2, 23% of Core 2  
> **Exam objective:** Configure System Restore and Windows backup, then verify recovery by performing an actual restore (Core 2 objectives 3.1 and 4.3).

## Goal

An untested backup is not a backup. You configure protection and backup, then actually restore a file — because the restore is the only step that proves the whole chain works, and it is the step that gets skipped.

## What you'll produce

A configured and verified backup with a completed restore test and a written recovery procedure.

## Tools and equipment

Windows PC, System Protection, File History, Killercoda Ubuntu Playground, tar

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

1. Check whether System Protection is enabled on the system drive, since a machine with it disabled has no restore points to fall back on.

   ```bash
   powershell -Command "Get-ComputerRestorePoint | Format-Table CreationTime,Description -AutoSize"
   ```

2. Create a restore point manually and confirm it appears in the list, recording its creation time and description.

   ```bash
   powershell -Command "Checkpoint-Computer -Description 'A+ Lab Restore Point' -RestorePointType MODIFY_SETTINGS"
   ```

3. Record what a restore point contains — system files, drivers, registry and installed programs — and what it excludes, which is personal data.
4. Record when System Restore is the right tool: after a bad driver, a failed update or a software installation that broke the system, but never for recovering a deleted document.
5. Configure File History or Windows Backup to a separate volume, and record why backing up to the same physical disk protects against nothing but accidental deletion.
6. Record the 3-2-1 rule: three copies of the data, on two different media, with one copy off site — and state which threat each part of the rule defeats.
7. Compare the backup types: full copies everything, incremental copies changes since the last backup of any type and clears the archive bit, and differential copies changes since the last full backup and leaves the archive bit set.
8. Work the restore arithmetic: from a Sunday full backup, restoring Thursday's data needs the full plus four incrementals, but only the full plus one differential — record why this decides the choice.
9. Move to the Killercoda playground and create a data set with a known checksum so the restore can be verified objectively.

   ```bash
   mkdir -p ~/backup-test/data && echo 'Critical business data' > ~/backup-test/data/important.txt && echo 'Second file' > ~/backup-test/data/second.txt && md5sum ~/backup-test/data/* > ~/backup-test/original.md5 && cat ~/backup-test/original.md5
   ```

10. Create the backup archive and confirm it exists with a sensible size.

   ```bash
   tar -czf ~/backup-test/backup-$(date +%Y%m%d).tar.gz -C ~/backup-test data && ls -lh ~/backup-test/*.tar.gz
   ```

11. Simulate the data loss by deleting the original directory, then restore from the archive.

   ```bash
   rm -rf ~/backup-test/data && ls ~/backup-test && tar -xzf ~/backup-test/backup-*.tar.gz -C ~/backup-test && ls -l ~/backup-test/data
   ```

12. Verify the restore objectively by re-checking the checksums against the originals, which is the step that actually proves the backup worked.

   ```bash
   md5sum -c ~/backup-test/original.md5 && echo 'RESTORE VERIFIED - checksums match'
   ```


## Test it — verification

A restore point is created and listed; the archive is created and the original data deleted; the restore returns both files; md5sum -c reports OK for every file; and your recovery procedure states the 3-2-1 rule with the threat each part defeats.

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
