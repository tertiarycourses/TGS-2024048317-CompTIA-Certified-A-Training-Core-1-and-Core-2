# Lab 30 Worksheet — Windows Command Line — Navigation, Files and Copy Operations

**Name:** ______________________    **Date:** ______________

**Exam objective:** Use the Windows command line for navigation, file management and resilient copy operations, choosing correctly between copy, xcopy and robocopy (Core 2 objective 1.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open Command Prompt as administrator and confirm your starting location and the commands available. |  |
| 2 | Practise navigation: move between directories, move up one level, and return to the drive root. |  |
| 3 | List directory contents with the switches that matter: all files including hidden, and a recursive listing. |  |
| 4 | Create a directory structure for the exercise and confirm it exists. |  |
| 5 | Create test files with content so the copy operations have something real to move. |  |
| 6 | Use copy for a single file and record its limitation — it copies files only and cannot handle directory trees. |  |
| 7 | Use xcopy with the switches for subdirectories including empty ones, and record that it handles trees but cannot resume. |  |
| 8 | Use robocopy to mirror the source to the destination, which is the correct tool for a real migration. |  |
| 9 | Read the robocopy log and record the files copied, skipped and failed, and the total bytes transferred. |  |
| 10 | Record why robocopy is the right choice for migrations: it retries failed files, resumes interrupted transfers, preserves attributes and timestamps, and logs everything. |  |
| 11 | Warn on the /MIR switch: it makes the destination identical to the source, which means it deletes files in the destination that are not in the source. Verify the destination before every mirror. |  |
| 12 | Verify the migration by comparing both directories, then clean up the exercise files. |  |

## Verification

**Success criterion:** Every command executes without error, the robocopy log confirms the expected file count copied, your reference sheet states the specific limitation of copy and xcopy that robocopy overcomes, and the /MIR deletion warning is recorded.

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
