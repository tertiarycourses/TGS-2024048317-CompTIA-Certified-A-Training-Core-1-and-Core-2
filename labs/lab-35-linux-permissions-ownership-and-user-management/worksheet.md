# Lab 35 Worksheet — Linux Permissions, Ownership and User Management

**Name:** ______________________    **Date:** ______________

**Exam objective:** Apply the Linux permission model to users, groups and others using symbolic and numeric notation, and manage users and sudo rights (Core 2 objective 1.11).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open the Killercoda playground and examine a file's permission stri... |  |
| 2 | Record the notation: r equals 4, w equals 2, x equals 1, so rwx is ... |  |
| 3 | Build the conversion table for the modes you will actually see: 777... |  |
| 4 | Set permissions numerically and verify the symbolic result matches ... |  |
| 5 | Set permissions symbolically and confirm it produces the same resul... |  |
| 6 | Record why directories need the execute bit: without x on a directo... |  |
| 7 | Create two users to demonstrate real access control between accounts. |  |
| 8 | Create a shared group and add both users to it. |  |
| 9 | Create a shared directory owned by the group with permissions that ... |  |
| 10 | Set the setgid bit so that files created inside inherit the group, ... |  |
| 11 | Verify the access control works: alice can create a file, and the f... |  |
| 12 | Grant alice administrative rights through sudo and record why sudo ... |  |

## Verification

**Success criterion:** Your conversion table is correct for all seven modes; the execute-bit demonstration shows a directory becoming enterable at 755 but not at 644; /srv/shared is mode 2770 owned by the support group; and alice's file inherits the support group.

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
