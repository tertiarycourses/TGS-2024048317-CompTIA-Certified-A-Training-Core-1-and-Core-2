# Lab 52 Worksheet — Backup Strategy Design and the 3-2-1 Rule

**Name:** ______________________    **Date:** ______________

**Exam objective:** Design a backup strategy specifying types, rotation, retention and off-site copy, and justify it against a stated recovery objective (Core 2 objective 4.3).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Record the two objectives that drive every backup design: the recovery point objective, which is how much data the business can afford to lose, and the recovery time objective, which is how long it can afford to be down. |  |
| 2 | Record the scenario objectives: a small business with a 24-hour RPO and a 4-hour RTO for its file server. |  |
| 3 | Record the 3-2-1 rule and what each element defeats: three copies defeat corruption, two different media defeat media failure, and one off-site copy defeats fire, flood and theft. |  |
| 4 | Compare full, incremental and differential backups on backup time, storage consumed, restore complexity and archive bit behaviour. |  |
| 5 | Work the restore arithmetic for an incremental scheme: a Sunday full plus daily incrementals means restoring Thursday requires the full plus Monday, Tuesday, Wednesday and Thursday — five operations. |  |
| 6 | Work the same arithmetic for a differential scheme: a Sunday full plus daily differentials means restoring Thursday requires only the full plus Thursday — two operations. |  |
| 7 | Choose between them against the 4-hour RTO, and justify the choice on restore time rather than on backup window alone. |  |
| 8 | Record the rotation schemes: grandfather-father-son with daily, weekly and monthly sets, and the tower of Hanoi scheme, and state what each provides. |  |
| 9 | Define the retention policy: how long daily, weekly, monthly and yearly copies are kept, and note that retention may be set by regulation rather than by preference. |  |
| 10 | Specify the off-site copy: where it goes, how it gets there, how often, and whether it is encrypted in transit and at rest. |  |
| 11 | Record the ransomware requirement: at least one copy must be offline, air-gapped or immutable, because ransomware encrypts every backup it can reach over the network. |  |
| 12 | Define the backup testing schedule, specifying how often a restore is actually performed and who signs off that it succeeded. |  |

## Verification

**Success criterion:** Your strategy states both RPO and RTO and the schedule meets them; the restore arithmetic is worked for both incremental and differential; the choice is justified against the 4-hour RTO; and the design includes an offline or immutable copy and a stated restore test schedule.

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
