# Lab 16 Worksheet — CPU Architecture, Sockets and Cooling Solutions

**Name:** ______________________    **Date:** ______________

**Exam objective:** Compare CPU architectures, socket types and cooling solutions, and diagnose thermal problems from observed behaviour (Core 1 objectives 3.4 and 5.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Compare x86-64 and ARM on power consumption, heat output, software compatibility and typical device class, and record which dominates desktops and which dominates mobile. |  |
| 2 | Record the socket types: LGA with pins on the motherboard used by Intel, PGA with pins on the processor still used by some AMD parts, and BGA soldered permanently in mobile devices. |  |
| 3 | Explain why a BGA processor in a laptop cannot be upgraded, and what that means when advising a customer on a slow machine. |  |
| 4 | Define core count, thread count and simultaneous multithreading, and explain why an eight-core processor may report sixteen logical processors. |  |
| 5 | Open Task Manager, go to Performance then CPU, and record the reported cores, logical processors, base speed, current speed and virtualization state. |  |
| 6 | Explain thermal throttling: a processor reduces its clock speed when it exceeds its temperature limit, which protects the silicon but degrades performance. |  |
| 7 | Explain the difference between throttling and overclocking, and note that Intel Turbo Boost and AMD Precision Boost are sanctioned automatic overclocking within thermal headroom. |  |
| 8 | Compare passive cooling — heatsink, thermal paste and heat pipes with no moving parts — against active cooling with a fan, and note where each is appropriate. |  |
| 9 | Explain the role of thermal paste: it fills the microscopic gaps between the processor's heat spreader and the cooler base so heat can actually transfer, and record that too much is as bad as too little. |  |
| 10 | Compare air cooling against liquid cooling on cooling capacity, noise, cost and failure mode, noting that a liquid cooler leak can destroy the whole system. |  |
| 11 | Build the thermal fault diagnostic sequence: confirm all fans spin, check intakes and heatsink fins for dust, verify the cooler is properly seated, check paste condition, then check ambient temperature and case airflow. |  |
| 12 | Monitor processor temperature under load and record the idle temperature, the load temperature and whether the clock speed dropped, then state whether the cooling is adequate. |  |

## Verification

**Success criterion:** Task Manager confirms the core and logical processor counts and the virtualization state; your diagnostic sequence orders the checks from cheapest to most invasive; and the temperature record supports a stated conclusion about cooling adequacy.

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
