#!/usr/bin/env python3
"""Generate the labs/ tree — ONE FOLDER PER LAB — from the same single source.

Each lab folder contains:
  README.md    the full lab: objective, tools, step-by-step with commands, verification, review questions
  worksheet.md a fill-in worksheet the learner completes and keeps as evidence

Plus labs/README.md (the index) and labs/tools.md (the toolkit reference).
"""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
import course_data as C
from data_domain1 import DOMAIN1; from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3; from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5; from data_domain6 import DOMAIN6
from data_domain7 import DOMAIN7; from data_domain8 import DOMAIN8
from data_domain9 import DOMAIN9
ACT=(DOMAIN1+DOMAIN2+DOMAIN3+DOMAIN4+DOMAIN5+DOMAIN6+DOMAIN7+DOMAIN8+DOMAIN9)
TOPICS={t["num"]:t for t in C.TOPICS}

def _find_repo(start):
    env=os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d=start
    for _ in range(8):
        d=os.path.dirname(d)
        if os.path.isdir(os.path.join(d,"courseware")) and os.path.isdir(os.path.join(d,"labs")): return d
    return os.path.dirname(os.path.dirname(HERE))
REPO=_find_repo(HERE)
LABS=os.path.join(REPO,"labs")
os.makedirs(LABS,exist_ok=True)

def slug(title):
    s="".join(ch.lower() if ch.isalnum() else "-" for ch in title)
    while "--" in s: s=s.replace("--","-")
    return s.strip("-")

def folder_name(a): return f"lab-{a['num']:02d}-{slug(a['title'])}"

TOOL_BY_KEY={
 "ipcalculator":("IP Calculator","https://alfredang.github.io/ipcalculator/"),
 "pcapanalyzer":("PCAP Analyzer","https://alfredang.github.io/pcapanalyzer/"),
 "cybersecuritysimulator":("Cybersecurity Simulator","https://alfredang.github.io/cybersecuritysimulator/"),
 "regexgenerator":("RegexLab","https://alfredang.github.io/regexgenerator/"),
 "killercoda":("Killercoda Ubuntu Playground","https://killercoda.com/playgrounds/scenario/ubuntu"),
}
FIGDIR=os.path.join(REPO,"courseware","assets")
FIG_BY_NAME={
 "IP Calculator":"tool-ipcalculator.png",
 "PCAP Analyzer":"tool-pcapanalyzer.png",
 "Cybersecurity Simulator":"tool-cybersecuritysimulator.png",
 "RegexLab":"tool-regexlab.png",
 "Killercoda Ubuntu Playground":"tool-killercoda.png",
}
def tools_used(a):
    blob=(a["services"]+" "+" ".join(s+" "+c for s,c in a["steps"])).lower()
    hits=[]
    for key,(name,url) in TOOL_BY_KEY.items():
        if key in blob or name.lower() in blob:
            hits.append((name,url))
    return hits

# ------------------------------------------------ per-lab folders
for a in ACT:
    t=TOPICS[a["topic"]]
    d=os.path.join(LABS,folder_name(a))
    os.makedirs(d,exist_ok=True)
    L=[]
    L.append(f"# Lab {a['num']} — {a['title']}")
    L.append("")
    L.append(f"> **Course:** {C.TITLE} ({C.COURSE_CODE})  ")
    L.append(f"> **Topic {t['code']}:** {t['title']} — {t['core']}, {t['exam_weight']}  ")
    L.append(f"> **Exam objective:** {a['objective']}")
    L.append("")
    L.append("## Goal")
    L.append("")
    L.append(a["desc"])
    L.append("")
    L.append("## What you'll produce")
    L.append("")
    L.append(a["build"])
    L.append("")
    L.append("## Tools and equipment")
    L.append("")
    L.append(a["services"])
    L.append("")
    tu=tools_used(a)
    if tu:
        L.append("### Browser tools used in this lab")
        L.append("")
        for name,url in tu:
            L.append(f"- **{name}** — <{url}>")
        L.append("")
        for name,url in tu:
            fn=FIG_BY_NAME.get(name)
            if fn and os.path.exists(os.path.join(FIGDIR,fn)):
                rel=os.path.relpath(os.path.join(FIGDIR,fn),d)
                L.append(f"![{name} interface map]({rel})")
                L.append("")
                L.append(f"*{name} — the panels and fields this lab uses.*")
                L.append("")
    L.append("## Safety")
    L.append("")
    L.append("- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.")
    L.append("- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.")
    L.append("- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.")
    L.append("- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.")
    L.append("")
    L.append("## Step-by-step")
    L.append("")
    for i,(instr,cmd) in enumerate(a["steps"],1):
        L.append(f"{i}. {instr}")
        if cmd:
            L.append("")
            L.append("   ```bash")
            for ln in cmd.split("\n"):
                L.append(f"   {ln}")
            L.append("   ```")
            L.append("")
    L.append("")
    L.append("## Test it — verification")
    L.append("")
    L.append(a["test"])
    L.append("")
    L.append("## Troubleshooting this lab")
    L.append("")
    L.append("| Symptom | What to check |")
    L.append("| --- | --- |")
    L.append("| A command returns \"command not found\" | Re-run the `apt-get install` step at the start of the lab — the playground starts with a minimal package set. |")
    L.append("| The Killercoda terminal has reset | The playground times out when idle. Reopen it and re-run the setup commands from step 1. |")
    L.append("| A browser tool will not load | Check the URL against `labs/tools.md`. All four tools run entirely client-side and need no login. |")
    L.append("| Output differs from the guide | Record what you actually observed — your environment differs from the reference, and explaining the difference is part of the exercise. |")
    L.append("")
    L.append("## Review questions")
    L.append("")
    L.append(f"1. State the exam objective this lab maps to, in your own words.")
    L.append(f"2. Which single step in this lab would you perform first on a real support call, and why?")
    L.append(f"3. What evidence would you attach to a support ticket to show this work was completed correctly?")
    L.append(f"4. Name one thing that would make this procedure fail, and how you would recognise it.")
    L.append("")
    L.append("## Record your evidence")
    L.append("")
    L.append(f"Complete [worksheet.md](worksheet.md) as you work through this lab and keep it — the Practical Performance assessment mirrors these tasks.")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"[← Labs index](../README.md)  ·  [Learner Guide](../../LG-{C.SHORT_TITLE}.md)  ·  [Course page]({C.COURSE_URL})")
    L.append("")
    with open(os.path.join(d,"README.md"),"w") as f: f.write("\n".join(L))

    # worksheet
    W=[]
    W.append(f"# Lab {a['num']} Worksheet — {a['title']}")
    W.append("")
    W.append(f"**Name:** ______________________    **Date:** ______________")
    W.append("")
    W.append(f"**Exam objective:** {a['objective']}")
    W.append("")
    W.append("## Record as you go")
    W.append("")
    W.append("| Step | What you did | What you observed |")
    W.append("| --- | --- | --- |")
    for i,(instr,cmd) in enumerate(a["steps"],1):
        short=instr if len(instr)<=70 else instr[:67]+"..."
        W.append(f"| {i} | {short} |  |")
    W.append("")
    W.append("## Verification")
    W.append("")
    W.append(f"**Success criterion:** {a['test']}")
    W.append("")
    W.append("- [ ] I completed every step in the lab.")
    W.append("- [ ] My result meets the success criterion above.")
    W.append("- [ ] I recorded my evidence (screenshots, output, completed tables).")
    W.append("")
    W.append("## Reflection")
    W.append("")
    W.append("**What surprised you in this lab?**")
    W.append("")
    W.append("_______________________________________________________________")
    W.append("")
    W.append("**Where would you apply this on the job?**")
    W.append("")
    W.append("_______________________________________________________________")
    W.append("")
    W.append("**What do you still need to revise before the exam?**")
    W.append("")
    W.append("_______________________________________________________________")
    W.append("")
    with open(os.path.join(d,"worksheet.md"),"w") as f: f.write("\n".join(W))

# ------------------------------------------------ labs index
I=[]
I.append(f"# Hands-On Labs — {C.TITLE}")
I.append("")
I.append(f"> **Course code:** {C.COURSE_CODE}  ·  **Version {C.VERSION}** · {C.VERSION_DATE}  ")
I.append(f"> **Register:** {C.COURSE_URL}")
I.append("")
I.append(f"{len(ACT)} hands-on labs across the nine CompTIA A+ exam domains. **Each lab has its own folder** "
         f"containing the full procedure (`README.md`) and a fill-in worksheet (`worksheet.md`).")
I.append("")
I.append("Every lab runs on training hardware provided in class or in your web browser — see "
         "[tools.md](tools.md) for the toolkit. There is nothing to install and nothing to license.")
I.append("")
I.append("## How to use these labs")
I.append("")
I.append("1. Read the objective and the goal first, so you know what the lab is proving.")
I.append("2. Work the steps in order — later steps depend on earlier ones.")
I.append("3. Complete the **Test it** verification before moving on. It is what the Practical Performance assessment mirrors.")
I.append("4. Fill in `worksheet.md` as you go and keep it as your evidence record.")
I.append("5. Answer the review questions from memory — if you cannot, revisit the concept in the Learner Guide.")
I.append("")
for exam in ["Core 1","Core 2"]:
    tops=[t for t in C.TOPICS if t["core"]==exam]
    exam_code = "220-1101" if exam=="Core 1" else "220-1102"
    I.append(f"## {exam} ({exam_code})")
    I.append("")
    for t in tops:
        acts=[x for x in ACT if x["topic"]==t["num"]]
        I.append(f"### Topic {t['code']} — {t['title']}  ({t['exam_weight']})")
        I.append("")
        I.append(t["subtitle"])
        I.append("")
        I.append("| Lab | Title | Exam objective |")
        I.append("| --- | --- | --- |")
        for a in acts:
            I.append(f"| [{a['num']:02d}]({folder_name(a)}/) | [{a['title']}]({folder_name(a)}/README.md) | {a['objective']} |")
        I.append("")
I.append("## Lab folder structure")
I.append("")
I.append("```")
I.append("labs/")
for a in ACT[:3]:
    I.append(f"  {folder_name(a)}/")
    I.append(f"    README.md      the full lab procedure")
    I.append(f"    worksheet.md   fill-in evidence record")
I.append("  ...")
I.append(f"  ({len(ACT)} lab folders in total)")
I.append("  README.md          this index")
I.append("  tools.md           the lab toolkit reference")
I.append("```")
I.append("")
with open(os.path.join(LABS,"README.md"),"w") as f: f.write("\n".join(I))

# ------------------------------------------------ tools reference
T=[]
T.append("# Lab Toolkit Reference")
T.append("")
T.append(f"Every tool used in the {C.TITLE} labs. All are free, all run in the browser, "
         f"and none requires an install or a login.")
T.append("")
T.append("## Browser tools")
T.append("")
T.append("| Tool | Link | What it does |")
T.append("| --- | --- | --- |")
for name,url,desc in C.LAB_TOOLS:
    T.append(f"| **{name}** | <{url}> | {desc} |")
T.append("")
T.append("## Which lab uses which tool")
T.append("")
T.append("| Tool | Labs |")
T.append("| --- | --- |")
for key,(name,url) in TOOL_BY_KEY.items():
    labs=[a["num"] for a in ACT if any(n==name for n,_ in tools_used(a))]
    if labs:
        T.append(f"| {name} | {', '.join(f'Lab {n}' for n in labs)} |")
T.append("")
T.append("## Killercoda Ubuntu Playground")
T.append("")
T.append("A real Ubuntu machine with root access, running in a browser tab. Used for every Linux "
         "command-line lab in this course.")
T.append("")
T.append("```bash")
T.append("# Every Killercoda lab starts by refreshing the package index")
T.append("apt-get update -qq")
T.append("apt-get install -y <the packages that lab needs>")
T.append("```")
T.append("")
T.append("The playground resets when idle. If your terminal disappears, reopen it and re-run the "
         "setup commands from the start of the lab.")
T.append("")
T.append("## Windows command reference")
T.append("")
T.append("```text")
for c in ["ipconfig /all","ipconfig /release","ipconfig /renew","ipconfig /flushdns",
          "ping <host>","tracert <host>","nslookup <domain>","netstat -ano",
          "sfc /scannow","DISM /Online /Cleanup-Image /RestoreHealth","chkdsk C: /scan",
          "robocopy <src> <dst> /MIR /R:2 /W:2","net accounts","net user","net localgroup Administrators",
          "manage-bde -status C:","netsh advfirewall show allprofiles state",
          "taskmgr","msconfig","eventvwr.msc","diskmgmt.msc","devmgmt.msc","taskschd.msc",
          "lusrmgr.msc","perfmon.msc","gpedit.msc","cleanmgr","dfrgui","resmon","msinfo32"]:
    T.append(c)
T.append("```")
T.append("")
T.append("## Linux command reference")
T.append("")
T.append("```bash")
for c in ["pwd","ls -la","cd <dir>","cp <src> <dst>","mv <src> <dst>","rm -r <dir>","mkdir -p <dir>",
          "cat <file>","less <file>","grep -n '<pattern>' <file>","find <path> -name '<glob>'",
          "df -h","du -sh <dir>","free -h","ps aux","top","htop",
          "chmod 750 <file>","chown user:group <file>","useradd -m <user>","usermod -aG sudo <user>",
          "ip -brief addr show","ip route show","ping -c 3 <host>","dig +short <domain>",
          "traceroute <host>","ss -tulnp","tcpdump -i any -c 100 -w capture.pcap",
          "apt-get update && apt-get install -y <pkg>","smartctl -H /dev/sda","lsblk","man <command>"]:
    T.append(c)
T.append("```")
T.append("")
with open(os.path.join(LABS,"tools.md"),"w") as f: f.write("\n".join(T))

print(f"Generated {len(ACT)} lab folders + index + tools reference in {LABS}")
