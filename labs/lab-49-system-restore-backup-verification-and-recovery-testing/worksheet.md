# Lab 49 Worksheet — System Restore, Backup Verification and Recovery Testing

**Name:** ______________________    **Date:** ______________

**Exam objective:** Configure System Restore and Windows backup, then verify recovery by performing an actual restore (Core 2 objectives 3.1 and 4.3).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Check whether System Protection is enabled on the system drive, since a machine with it disabled has no restore points to fall back on. |  |
| 2 | Create a restore point manually and confirm it appears in the list, recording its creation time and description. |  |
| 3 | Record what a restore point contains — system files, drivers, registry and installed programs — and what it excludes, which is personal data. |  |
| 4 | Record when System Restore is the right tool: after a bad driver, a failed update or a software installation that broke the system, but never for recovering a deleted document. |  |
| 5 | Configure File History or Windows Backup to a separate volume, and record why backing up to the same physical disk protects against nothing but accidental deletion. |  |
| 6 | Record the 3-2-1 rule: three copies of the data, on two different media, with one copy off site — and state which threat each part of the rule defeats. |  |
| 7 | Compare the backup types: full copies everything, incremental copies changes since the last backup of any type and clears the archive bit, and differential copies changes since the last full backup and leaves the archive bit set. |  |
| 8 | Work the restore arithmetic: from a Sunday full backup, restoring Thursday's data needs the full plus four incrementals, but only the full plus one differential — record why this decides the choice. |  |
| 9 | Move to the Killercoda playground and create a data set with a known checksum so the restore can be verified objectively. |  |
| 10 | Create the backup archive and confirm it exists with a sensible size. |  |
| 11 | Simulate the data loss by deleting the original directory, then restore from the archive. |  |
| 12 | Verify the restore objectively by re-checking the checksums against the originals, which is the step that actually proves the backup worked. |  |

## Verification

**Success criterion:** A restore point is created and listed; the archive is created and the original data deleted; the restore returns both files; md5sum -c reports OK for every file; and your recovery procedure states the 3-2-1 rule with the threat each part defeats.

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
