#!/usr/bin/env python3
"""Generate the lab-tool reference figures embedded in the Learner Guide.

Each figure is a labelled interface map of one lab tool: the panels the learner
will actually click, in their real screen positions, with the fields this course
uses called out. Drawn deterministically with Pillow so the figures are
reproducible, version-controllable and do not depend on a live capture.

Output: courseware/assets/tool-<slug>.png
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))
REPO = _find_repo(HERE)
OUT = os.path.join(REPO, "courseware", "assets")
os.makedirs(OUT, exist_ok=True)

W, H = 1400, 860
BLUE=(0x1F,0x6F,0xEB); TEAL=(0x10,0xB9,0x81); AMBER=(0xF5,0x9E,0x0B)
VIOLET=(0x7C,0x3A,0xED); INK=(0x16,0x1B,0x26); GREY=(0x5B,0x63,0x72)
LIGHT=(0xF5,0xF8,0xFC); LINE=(0xE2,0xE8,0xF0); WHITE=(255,255,255)
DARKBG=(0x0B,0x12,0x20); CODE=(0x9C,0xDC,0xFE)

def _font(sz, bold=False):
    for p in ("/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold
              else "/System/Library/Fonts/Supplemental/Arial.ttf",
              "/System/Library/Fonts/Helvetica.ttc",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")):
        try: return ImageFont.truetype(p, sz)
        except Exception: pass
    return ImageFont.load_default()

def _mono(sz):
    for p in ("/System/Library/Fonts/Menlo.ttc","/System/Library/Fonts/Monaco.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"):
        try: return ImageFont.truetype(p, sz)
        except Exception: pass
    return ImageFont.load_default()

def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def chrome(d, title, url, accent):
    """Browser chrome: title bar + address bar."""
    d.rectangle([0,0,W,H], fill=WHITE)
    d.rectangle([0,0,W,64], fill=LIGHT)
    for i,c in enumerate([(0xFF,0x5F,0x57),(0xFE,0xBC,0x2E),(0x28,0xC8,0x40)]):
        d.ellipse([26+i*26,25,40+i*26,39], fill=c)
    d.rounded_rectangle([120,18,W-30,46], radius=14, fill=WHITE, outline=LINE, width=1)
    d.text((140,25), url, font=_font(15), fill=GREY)
    d.rectangle([0,64,W,68], fill=accent)
    d.text((30,88), title, font=_font(30,True), fill=INK)

def panel(d, x, y, w, h, label, accent, body=None, mono=False):
    d.rounded_rectangle([x,y,x+w,y+h], radius=10, fill=LIGHT, outline=LINE, width=1)
    d.rectangle([x,y,x+w,y+7], fill=accent)
    d.text((x+18,y+20), label, font=_font(15,True), fill=accent)
    if body:
        f = _mono(14) if mono else _font(14)
        yy = y+48
        for ln in body:
            d.text((x+18,yy), ln, font=f, fill=INK if not mono else INK)
            yy += 24

def callout(d, x, y, n, text, accent, width=330):
    d.ellipse([x,y,x+30,y+30], fill=accent)
    tw = d.textlength(str(n), font=_font(16,True))
    d.text((x+15-tw/2,y+6), str(n), font=_font(16,True), fill=WHITE)
    f=_font(14)
    for i,ln in enumerate(wrap(d, text, f, width)):
        d.text((x+42,y+2+i*19), ln, font=f, fill=GREY)

def footer(d, name, url):
    d.rectangle([0,H-46,W,H], fill=LIGHT)
    d.text((30,H-34), f"{name}  ·  {url}", font=_font(13), fill=GREY)
    t=f"{C.SHORT_TITLE} · {C.COURSE_CODE}"
    d.text((W-30-d.textlength(t,font=_font(13)),H-34), t, font=_font(13), fill=GREY)

# ---------------------------------------------------------------- IP Calculator
def fig_ipcalc():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img)
    chrome(d,"IP Calculator — subnet and address planning","https://alfredang.github.io/ipcalculator/",BLUE)
    for i,(t,on) in enumerate([("IPv4",True),("IPv6",False),("Batch",False)]):
        x=30+i*130
        d.rounded_rectangle([x,140,x+118,180],radius=8,fill=BLUE if on else LIGHT,outline=LINE)
        tw=d.textlength(t,font=_font(15,True))
        d.text((x+59-tw/2,151),t,font=_font(15,True),fill=WHITE if on else GREY)
    panel(d,30,200,640,120,"ADDRESS  /  NETMASK",BLUE)
    d.rounded_rectangle([48,246,650,300],radius=8,fill=WHITE,outline=BLUE,width=2)
    d.text((64,262),"192.168.50.75/24",font=_mono(22),fill=INK)
    panel(d,30,340,640,300,"RESULT",TEAL,[
        "Address         192.168.50.75",
        "Netmask         255.255.255.0  = 24",
        "Wildcard        0.0.0.255",
        "Network         192.168.50.0/24",
        "Broadcast       192.168.50.255",
        "HostMin         192.168.50.1",
        "HostMax         192.168.50.254",
        "Hosts/Net       254            (Private Internet)",
    ],mono=True)
    d.text((710,150),"What this course uses it for",font=_font(17,True),fill=INK)
    for i,(n,t) in enumerate([
        (1,"Enter the address with its prefix. Accepts CIDR (/24), dotted decimal (255.255.255.0) or hex."),
        (2,"Read the Network and Broadcast addresses — these two are reserved in every subnet."),
        (3,"Read HostMin–HostMax. This is the range a client address must fall inside."),
        (4,"Read Hosts/Net. Choose the SMALLEST prefix that still meets the host requirement."),
        (5,"Batch tab: one subnet per line with a # comment, then export the plan to CSV."),
    ]):
        callout(d,710,190+i*88,n,t,[BLUE,TEAL,VIOLET,AMBER,BLUE][i],width=640)
    footer(d,"IP Calculator","https://alfredang.github.io/ipcalculator/")
    img.save(os.path.join(OUT,"tool-ipcalculator.png"))

# ---------------------------------------------------------------- PCAP Analyzer
def fig_pcap():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img)
    chrome(d,"PCAP Analyzer — packet capture analysis","https://alfredang.github.io/pcapanalyzer/",VIOLET)
    d.rounded_rectangle([30,140,W-30,210],radius=10,fill=LIGHT,outline=VIOLET,width=2)
    d.text((52,158),"Drop a .pcap or .pcapng file here, or click to browse",font=_font(17,True),fill=INK)
    d.text((52,182),"Files are parsed locally in your browser. Nothing is uploaded.",font=_font(14),fill=GREY)
    d.rounded_rectangle([W-190,152,W-52,196],radius=8,fill=VIOLET)
    d.text((W-160,166),"Sample",font=_font(16,True),fill=WHITE)
    stats=[("Packets","1,284"),("Bytes","742 KB"),("Duration","18.4 s"),("Avg pkt","578 B"),("Format","pcapng")]
    cw=(W-60-4*14)//5
    for i,(k,v) in enumerate(stats):
        x=30+i*(cw+14)
        d.rounded_rectangle([x,230,x+cw,310],radius=10,fill=LIGHT,outline=LINE)
        d.rectangle([x,230,x+cw,236],fill=[BLUE,TEAL,VIOLET,AMBER,BLUE][i])
        d.text((x+16,250),k,font=_font(13,True),fill=GREY)
        d.text((x+16,272),v,font=_font(22,True),fill=INK)
    panel(d,30,330,430,230,"PROTOCOL DISTRIBUTION",BLUE)
    for i,(p,pc,c) in enumerate([("TCP",62,BLUE),("UDP",21,TEAL),("DNS",9,VIOLET),("ICMP",5,AMBER),("ARP",3,GREY)]):
        y=378+i*34
        d.text((48,y),p,font=_font(14,True),fill=INK)
        d.rectangle([120,y+3,120+int(pc*2.9),y+17],fill=c)
        d.text((120+int(pc*2.9)+10,y),f"{pc}%",font=_font(13),fill=GREY)
    panel(d,485,330,430,230,"TOP TALKERS  /  CONVERSATIONS",TEAL,[
        "192.168.50.75    →  93.184.216.34",
        "192.168.50.75    →  8.8.8.8",
        "192.168.50.1     →  192.168.50.75",
        "192.168.50.75    →  142.250.66.:443",
    ],mono=True)
    panel(d,940,330,430,230,"PACKETS TABLE",VIOLET,[
        "Time    Source        Proto  Len",
        "0.000   192.168.50.75  TCP    74",
        "0.012   93.184.216.34  TCP    74",
        "0.104   192.168.50.75  DNS    82",
        "0.221   8.8.8.8        DNS   148",
    ],mono=True)
    for i,(n,t) in enumerate([
        (1,"Load your own capture, or click Sample to explore without one."),
        (2,"Read the four headline statistics first — they characterise the whole capture."),
        (3,"Protocol distribution shows what is on the wire, and which traffic is unencrypted."),
        (4,"Top conversations identify which host pair to investigate; then read that packet's detail."),
    ]):
        callout(d,30+(i%2)*690,590+(i//2)*70,n,t,[BLUE,TEAL,VIOLET,AMBER][i],width=600)
    footer(d,"PCAP Analyzer","https://alfredang.github.io/pcapanalyzer/")
    img.save(os.path.join(OUT,"tool-pcapanalyzer.png"))

# ---------------------------------------------------------------- Cybersecurity Simulator
def fig_cyber():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img)
    chrome(d,"Cybersecurity Simulator — safe threat simulation lab","https://alfredang.github.io/cybersecuritysimulator/",AMBER)
    menu=["Dashboard","Phishing","XSS","SQL Injection","Password Lab","Malware",
          "Ransomware","Social Engineering","Data Leakage","Final Quiz"]
    x=30
    for i,m in enumerate(menu):
        w=int(d.textlength(m,font=_font(13,True)))+26
        if x+w>W-30: break
        on=(i==0)
        d.rounded_rectangle([x,140,x+w,176],radius=8,fill=AMBER if on else LIGHT,outline=LINE)
        d.text((x+13,150),m,font=_font(13,True),fill=WHITE if on else GREY)
        x+=w+8
    tiles=[("Phishing Simulator","Classify safe vs phishing e-mail; inspect the real link destination.",BLUE),
           ("Password Lab","Measure strength, estimated crack time and entropy in bits.",TEAL),
           ("SQL Injection","Watch the live query change as you type. Fake in-memory data only.",VIOLET),
           ("XSS Simulator","Compare unsafe vs safe rendering. No code actually executes.",AMBER),
           ("Malware / Ransomware","Conceptual animations and a simulated lock screen. Completely safe.",BLUE),
           ("Social Engineering","Scenario decisions across 8 tactics, with a score and a tactic guide.",TEAL)]
    tw=(W-60-2*18)//3; th=150
    for i,(t,b,c) in enumerate(tiles):
        x=30+(i%3)*(tw+18); y=200+(i//3)*(th+18)
        d.rounded_rectangle([x,y,x+tw,y+th],radius=10,fill=LIGHT,outline=LINE)
        d.rectangle([x,y,x+tw,y+7],fill=c)
        d.text((x+18,y+22),t,font=_font(16,True),fill=INK)
        for j,ln in enumerate(wrap(d,b,_font(13),tw-36)):
            d.text((x+18,y+52+j*20),ln,font=_font(13),fill=GREY)
    d.rounded_rectangle([30,530,W-30,640],radius=10,fill=(0xE8,0xF7,0xEE),outline=LINE)
    d.rectangle([30,530,37,640],fill=TEAL)
    d.text((56,552),"EVERYTHING HERE IS SIMULATED",font=_font(14,True),fill=(0x12,0x7A,0x3E))
    for j,ln in enumerate(wrap(d,"No real malware runs, no real credentials are used and no data leaves your browser. "
                                 "The SQL and XSS modules operate on fake in-memory data and never execute injected code. "
                                 "This is what makes it safe to demonstrate attacks in a classroom.",_font(14),W-120)):
        d.text((56,578+j*22),ln,font=_font(14),fill=INK)
    for i,(n,t) in enumerate([
        (1,"Pick a module from the top menu — each has warning signs, prevention tips and a quick quiz."),
        (2,"Password Lab reports entropy and crack time: use the figures to justify your policy rules."),
    ]):
        callout(d,30+i*690,672,n,t,[BLUE,TEAL][i],width=600)
    footer(d,"Cybersecurity Simulator","https://alfredang.github.io/cybersecuritysimulator/")
    img.save(os.path.join(OUT,"tool-cybersecuritysimulator.png"))

# ---------------------------------------------------------------- RegexLab
def fig_regex():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img)
    chrome(d,"RegexLab — pattern testing for log analysis","https://alfredang.github.io/regexgenerator/",TEAL)
    panel(d,30,140,W-60,110,"REGULAR EXPRESSION",TEAL)
    d.rounded_rectangle([48,182,W-78,236],radius=8,fill=WHITE,outline=TEAL,width=2)
    d.text((64,196),r"/\b(?:\d{1,3}\.){3}\d{1,3}\b/g",font=_mono(20),fill=INK)
    for i,(f,on) in enumerate([("g",True),("i",False),("m",False),("s",False),("u",False),("y",False)]):
        x=30+i*74
        d.rounded_rectangle([x,266,x+64,304],radius=8,fill=TEAL if on else LIGHT,outline=LINE)
        tw=d.textlength(f,font=_mono(17))
        d.text((x+32-tw/2,276),f,font=_mono(17),fill=WHITE if on else GREY)
    d.text((520,276),"g = all matches   i = ignore case   m = multiline   s = dotall",font=_font(14),fill=GREY)
    panel(d,30,324,660,250,"TEST STRING",BLUE,[
        "2026-08-19 09:15:03 ERROR",
        "  Connection refused from 10.0.0.55",
        "2026-08-19 09:16:10 ERROR",
        "  Auth failed from 203.0.113.9",
        "2026-08-19 09:18:31 CRITICAL",
        "  Database unreachable at 10.0.0.80",
    ],mono=True)
    panel(d,710,324,660,250,"MATCHES  ·  3 found",VIOLET,[
        "1.  10.0.0.55        index 47",
        "2.  203.0.113.9      index 118",
        "3.  10.0.0.80        index 191",
        "",
        "Substitution preview:",
        "  <redacted> for every match",
    ],mono=True)
    for i,(n,t) in enumerate([
        (1,"Type the pattern; matches highlight live as you type. The counter shows how many were found."),
        (2,"Toggle flags — g for every match rather than just the first, i to ignore case."),
        (3,"Read the matches panel to confirm the pattern found what you intended, and nothing else."),
        (4,"Then apply the proven pattern with grep on the command line against the real log."),
    ]):
        callout(d,30+(i%2)*690,600+(i//2)*70,n,t,[BLUE,TEAL,VIOLET,AMBER][i],width=600)
    footer(d,"RegexLab","https://alfredang.github.io/regexgenerator/")
    img.save(os.path.join(OUT,"tool-regexlab.png"))

# ---------------------------------------------------------------- Killercoda
def fig_killercoda():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img)
    chrome(d,"Killercoda Ubuntu Playground — a real Linux machine in the browser",
           "https://killercoda.com/playgrounds/scenario/ubuntu",INK)
    d.rounded_rectangle([30,140,W-30,600],radius=10,fill=DARKBG)
    d.rectangle([30,140,W-30,176],fill=(0x1B,0x25,0x38))
    d.text((52,150),"Terminal — root@controlplane",font=_font(14,True),fill=(0xB6,0xC2,0xD4))
    lines=[("$ ","cat /etc/os-release | grep PRETTY"),
           ("","PRETTY_NAME=\"Ubuntu 22.04.3 LTS\""),
           ("$ ","apt-get update -qq && apt-get install -y net-tools dnsutils"),
           ("","Reading package lists... Done"),
           ("$ ","ip -brief addr show"),
           ("","lo     UNKNOWN  127.0.0.1/8"),
           ("","eth0   UP       10.244.0.14/24"),
           ("$ ","dig +short www.tertiarycourses.com.sg"),
           ("","104.22.35.191"),
           ("$ ","chmod 640 ~/aplus/logs/system.log && ls -l ~/aplus/logs/"),
           ("","-rw-r----- 1 root root  118 Aug 19 09:14 system.log"),
           ("$ ","grep -c 'ERROR' ~/aplus/logs/system.log"),
           ("","2"),
           ("$ ","_")]
    y=196
    for pre,txt in lines:
        x=52
        if pre:
            d.text((x,y),pre,font=_mono(16),fill=TEAL); x+=int(d.textlength(pre,font=_mono(16)))
        d.text((x,y),txt,font=_mono(16),fill=CODE if pre else (0xC9,0xD4,0xE3))
        y+=28
    for i,(n,t) in enumerate([
        (1,"Open the URL and wait for the prompt. You get root on a real Ubuntu machine — nothing to install."),
        (2,"Start every lab with apt-get update, then install only the packages that lab needs."),
        (3,"The playground RESETS when idle. If your terminal disappears, reopen it and re-run the setup steps."),
    ]):
        callout(d,30+(i%2)*690,626+(i//2)*76,n,t,[BLUE,TEAL,AMBER][i],width=600)
    footer(d,"Killercoda Ubuntu Playground","https://killercoda.com/playgrounds/scenario/ubuntu")
    img.save(os.path.join(OUT,"tool-killercoda.png"))

# Four of these tools were captured as REAL browser screenshots (see courseware/assets/).
# A real screenshot always beats a drawn approximation, so the generator only fills the
# gaps: Killercoda sits behind a login/captcha and cannot be captured headlessly.
# Pass --force to regenerate a drawn figure over an existing file.
FORCE = "--force" in sys.argv
JOBS = [("tool-ipcalculator.png", fig_ipcalc),
        ("tool-pcapanalyzer.png", fig_pcap),
        ("tool-cybersecuritysimulator.png", fig_cyber),
        ("tool-regexlab.png", fig_regex),
        ("tool-killercoda.png", fig_killercoda)]
made = kept = 0
for name, fn in JOBS:
    if os.path.exists(os.path.join(OUT, name)) and not FORCE:
        kept += 1
        continue
    fn(); made += 1
print(f"Tool figures in {OUT}: {made} generated, {kept} kept (real screenshots)")
