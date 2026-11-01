"""Generate the Jupyter Book pages and _toc.yml from the post files in source/.

Usage: python tools/build_book.py source/unsolicited-advice-posts.md .
(source/more-advice-posts.md is read from the same folder.)
"""
import os, re, sys, shutil, unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]

CHAPTERS = [
    ("01-well-being", "Well-Being and Mental Health",
     "Science is one of the most intellectually demanding jobs there is, and your brain is the tool that does the work. These posts are about resting, pacing yourself, noticing burnout and depression early, and making room to enjoy science.",
     ["Rest makes you more productive; don't work when you're tired.",
      "A PhD is a marathon, not a sprint. Sleep, exercise, hobbies and friends are part of the job.",
      "Mental health problems are common in science. Notice them, talk about them, and ask for help early.",
      "Make time to play with ideas, free of deadlines."],
     [("2026-09-23", "Your Brain Is Your Most Important Tool"),
      ("2023-10-11", "Protect Your Brain"),
      ("2026-04-19", "Don't Work When You're Tired"),
      ("2024-09-03", "Three Things I Wish I'd Known When Starting My PhD"),
      ("2025-05-26", "Depression Is Common, and Help Works"),
      ("2025-11-18", "Escape the \"I Need To\" Mindset: Make Time to Play")]),
    ("02-mindset", "Mindset, Confidence and Resilience",
     "Doubt, comparison and pushback are part of every scientific career. These posts are about keeping perspective: tracking your own progress, staying humble, questioning ideas, and being patient when your ideas meet resistance.",
     ["Curiosity counts for more than prior experience.",
      "Compare yourself with your past self, not with others.",
      "Question everything, including your own ideas, and welcome challenges to them.",
      "Resistance to an idea can mean you've touched a nerve, so be patient."],
     [("2025-03-15", "It's Normal to Start a PhD Without Experience"),
      ("2024-05-02", "Be Careful When You Compare Yourself to Others"),
      ("2025-08-19", "Competition, Insecurity and Inclusive Cultures"),
      ("2026-01-02", "Question Everything and Everyone"),
      ("2024-08-22", "Great Ideas Often Meet Resistance"),
      ("2024-12-30", "Advocate for Your Ideas, but Stay Humble"),
      ("2023-01-05", "Use What Science Teaches You to Navigate Life")]),
    ("03-problems-and-ideas", "Choosing Problems and Generating Ideas",
     "Solving problems is hard; finding the right problems is harder. These posts cover how to ask good questions, where to find inspiration, and how to manage the ideas you come up with.",
     ["Ask \"What is the question?\" before \"What is the answer?\"",
      "Aim for work that opens new problems, and master the fundamentals that carry over to new problems.",
      "Set aside time for focused thinking, and break complex problems into simple parts.",
      "Write ideas down, let them mature, and pursue them when the time is right."],
     [("2023-02-21", "Finding the Right Question Is the Hard Part"),
      ("2024-06-10", "Write Papers That Create Problems"),
      ("2023-08-24", "Separate the Fundamental from the Applied"),
      ("2025-08-03", "Start from a Specific Application"),
      ("2025-02-22", "Imagine the Seminar You'd Give"),
      ("2025-12-26", "Make Time for Focused Thinking"),
      ("2025-11-13", "Learn the Art of Reductionism"),
      ("2023-08-11", "Find Inspiration in Simple Places"),
      ("2023-09-28", "Connect with Seemingly Unrelated Fields"),
      ("2023-10-28", "Write Down Your Ideas and Let Them Mature")]),
    ("04-communication", "Communicating Science",
     "A great idea only has impact if it spreads. These posts are about talks, audiences and \"selling\" ideas, and about speaking openly within the scientific community.",
     ["Science means generating ideas and selling them.",
      "The main goal of a talk is to get people excited.",
      "Sketch the story before you build slides, and keep slides simple and self-explanatory.",
      "Know your audience: avoid jargon, lead with results when time is short, and connect to what people care about."],
     [("2023-12-12", "Science Is About Selling Ideas"),
      ("2025-10-09", "Talks Should Get People Excited"),
      ("2024-07-07", "Sketch Your Talk Before Making Slides"),
      ("2025-02-15", "Three Rules for Slides"),
      ("2023-10-04", "Get to the Point: Lead with Results"),
      ("2024-03-01", "Language Matters: Know Your Audience"),
      ("2025-05-09", "Make It Relatable: The Ice-Cream Lesson"),
      ("2026-05-15", "Be an Open and Confident Communicator")]),
    ("05-writing", "Writing Papers and Proposals",
     "Technical writing is a skill you learn, and the posts here show how to make it easier and more fun: break papers into small wins, be succinct, and remember that each paper is part of a larger story.",
     ["Writing is a way of thinking, not just of reporting.",
      "Break a paper into small wins and celebrate each one.",
      "Be succinct; a 2-page document is harder to write than a 15-page one.",
      "Not every paper has to be a home run, and being correct matters more than being first."],
     [("2025-12-02", "Writing Helps You Think"),
      ("2025-04-04", "The First Paper Is the Hardest"),
      ("2025-06-05", "Write Your Paper in Small Wins"),
      ("2023-07-31", "Make Writing Fun"),
      ("2025-03-23", "Be Succinct"),
      ("2025-04-29", "Not Every Paper Has to Be a Home Run"),
      ("2025-07-30", "Being Correct Matters More Than Being First"),
      ("2024-01-17", "Writing Proposals for Multidisciplinary Panels")]),
    ("06-productivity", "Productivity and Organization",
     "Creative work needs structure. These posts cover milestones, notes, time management, and treating what you produce as a long-term investment.",
     ["Time management is an underrated skill.",
      "Set milestones with real deadlines, and use commitments to keep yourself on track.",
      "Take good notes, because ideas build up over many meetings.",
      "Figures, code and slides get reused for years, so do them well the first time."],
     [("2024-08-29", "Time Management Is an Underrated Skill"),
      ("2023-11-12", "Set Milestones and Deadlines"),
      ("2024-10-17", "Take Good Meeting Notes"),
      ("2023-07-26", "Treat Your Research Products as Investments"),
      ("2024-07-01", "Be Patient: Projects Grow in Phases")]),
    ("07-people", "Mentors, Networks and Working with People",
     "Science is a team sport. These posts are about self-awareness, mentorship (receiving it and seeking it out), networking even if you're an introvert, and learning from people with different backgrounds.",
     ["Build several mentors; your advisor can't be your only one.",
      "Be a good mentee: open, reliable, and responsible for your own career.",
      "Networking can be learned, and talks, volunteering and social media all help.",
      "Self-awareness and emotional intelligence are underrated scientific skills."],
     [("2026-03-10", "Build a Network of Trusted Mentors"),
      ("2024-09-15", "How to Be a Good Mentee"),
      ("2024-04-07", "Networking, Especially for Introverts"),
      ("2026-06-28", "Self-Awareness Is Underrated"),
      ("2025-03-02", "Don't Neglect the Social Side of Science"),
      ("2025-05-13", "Learn from Other Cultures"),
      ("2024-06-23", "Ask People About Their Career Paths")]),
    ("08-career", "Career Development",
     "From the PhD to the postdoc, the job market and beyond: what each stage gives you, how to make the most of it, and the many paths a science degree opens.",
     ["Know what you want to be known for.",
      "Teaching sharpens your grasp of the fundamentals and your communication.",
      "The postdoc is a time to reflect, explore boldly and build skills beyond research.",
      "Science training carries over to many careers."],
     [("2025-04-18", "What the PhD Teaches You"),
      ("2025-12-17", "Being a TA Is Great Professional Development"),
      ("2024-09-29", "Get Involved in Teaching"),
      ("2024-11-10", "Make the Most of Your Postdoc"),
      ("2024-12-01", "Navigating the Job Search"),
      ("2026-01-07", "What Do You Want to Be Known For?"),
      ("2024-01-25", "There Are Many Career Paths"),
      ("2022-11-27", "Understand the Scientific Enterprise")]),
    ("09-computational", "Computational and Mathematical Research",
     "Advice for people who model, code and do math: think before you compute, build up complexity step by step, test hard, and never trust a solution blindly.",
     ["Think, and work a simple version by hand, before you hit \"solve.\"",
      "Build models step by step, and test them at the extremes.",
      "Algorithms don't understand physics, so validate every solution.",
      "You don't have to be amazing at coding or math to have impact."],
     [("2025-02-02", "Think Before You Hit \"Solve\""),
      ("2024-02-24", "Do Calculations by Hand First"),
      ("2023-09-21", "Build Complex Models Step by Step"),
      ("2024-04-16", "Test Your Code at the Extremes"),
      ("2024-05-15", "Algorithms Don't Understand Physics"),
      ("2024-01-05", "Models Are Useful Beyond Prediction"),
      ("2025-09-05", "Keep Notation Consistent and Compact"),
      ("2024-08-14", "Go Easy on the Math in Talks"),
      ("2024-05-29", "Learn Several Programming Languages"),
      ("2023-10-18", "You Don't Have to Be Amazing at Coding or Math"),
      ("2023-12-22", "Algorithms for Everyday Life")]),
    ("10-faculty", "For Young Faculty",
     "Starting an independent career: mentoring students, protecting time for research, building a research program, and remembering why you chose this job.",
     ["Trust your students, treat them as professionals, and give hard feedback with care.",
      "Adjust how much freedom students get to their stage, like a feedback controller.",
      "Block off research time and protect it.",
      "Explore broadly first, then go deep, and build the community around you."],
     [("2026-07-06", "Trust Your Students"),
      ("2026-03-23", "Give Hard Feedback with Care"),
      ("2023-11-26", "Mentoring as Feedback Control"),
      ("2024-07-31", "Choose Problems That Train Your Students"),
      ("2023-12-28", "Protect Your Research Time"),
      ("2024-12-09", "Keep Doing Actual Research"),
      ("2025-07-11", "Read for Pleasure"),
      ("2023-08-17", "Reflect and Celebrate"),
      ("2025-03-10", "Explore Broadly, Then Go Deep"),
      ("2024-01-12", "Where to Find Research Problems"),
      ("2022-12-06", "Write Proposals for the Ideas, Not the Money"),
      ("2025-08-27", "Organize Events")]),
]

MONTHS = "January February March April May June July August September October November December".split()

def nice(d):
    y, m, dd = d.split("-")
    return f"{MONTHS[int(m)-1]} {int(dd)}, {y}"

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")

# Series posts added after the first edition, keyed by activity id, appended at the end of their part
# so that existing page file names (and links to them) stay the same.
LATER_SERIES = {
    "7520918347140677632": ("04-communication", "Write a Script for Your First Talks"),
    "7514016891074703360": ("02-mindset", "Points, Games and Sets: Lessons from Agassi"),
    "7447311638858469378": ("04-communication", "Talks Should Change How People Think"),
    "7423400271776735232": ("07-people", "Do Your Homework Before a Visit"),
    "7316073485850628099": ("02-mindset", "Impostor Syndrome Is Normal"),
}

# Advice posts written without the "Unsolicited advice" opener; they're part of the series in spirit.
# activity id -> (part, title)
MORE = {
    "7467222622519529473": ("01-well-being", "The Let-Down Effect: Anxiety After Stress"),
    "7464792802758070274": ("01-well-being", "Running as a Way to Manage Anxiety"),
    "7354929061493686275": ("01-well-being", "The Runner's High and Clear Thinking"),
    "7339645221036617729": ("02-mindset", "Lessons from Federer on Resilience"),
    "7431001512870330368": ("02-mindset", "Enjoy the Journey, Not Just the Outcome"),
    "7411772897205186560": ("02-mindset", "You Try, You Fail, You Try Again"),
    "7319704543296962560": ("02-mindset", "Confidence Is Built, Not Innate"),
    "7058247665305731073": ("02-mindset", "Learning to Cope with Criticism"),
    "7131279902368034817": ("02-mindset", "Embrace Your Naïveté"),
    "7510382342465830912": ("02-mindset", "Education Is a Gym for the Mind"),
    "7321310403261566980": ("03-problems-and-ideas", "The Four Elements of Research"),
    "7353145593147346945": ("03-problems-and-ideas", "Your Specialty Can Be Building Bridges"),
    "7398459084255064065": ("04-communication", "Include a Personal Intro Slide"),
    "7447643028393058304": ("04-communication", "Put Acknowledgments First"),
    "7345252587606069250": ("04-communication", "A Poster Without the Poster Tube"),
    "7368295272369569793": ("05-writing", "Sketch an Outline Before You Write"),
    "7515417138354982913": ("05-writing", "In the Era of AI, the Process Matters"),
    "7354257991166038017": ("05-writing", "Resources for Becoming a Good Reviewer"),
    "7350815291565617156": ("05-writing", "Be Thorough but Efficient as a Reviewer"),
    "7361732482649509888": ("06-productivity", "Plan Your Day in Time Slots"),
    "7487872426744115201": ("06-productivity", "Learn to Say No"),
    "7440854052868915200": ("07-people", "Mentoring Is Built on Mutual Trust"),
    "7392734441485459456": ("07-people", "Conferences for Introverts"),
    "7368774556330725376": ("07-people", "What Should You Call Your Professor?"),
    "7365037444573880320": ("07-people", "College Is Also About Networks"),
    "7386386719333539840": ("07-people", "Norms for Productive Group Discussions"),
    "7308848760871170048": ("07-people", "If You Want It to Happen, Start It Yourself"),
    "7400211402973696000": ("08-career", "What Makes the PhD So Challenging"),
    "7330751623771643904": ("08-career", "Becoming an Independent Researcher"),
    "7402342389698527232": ("09-computational", "Complexity vs. Insight in Optimization Models"),
    "7345432474736279552": ("09-computational", "Getting Started in Data Science and Machine Learning"),
    "7341520184827924481": ("09-computational", "Share Your Data and Code"),
    "7384937752498397184": ("09-computational", "Impact Doesn't Have to Mean Commercialization"),
    "7290719210417111040": ("09-computational", "Math Teaches You How to Learn"),
    "7430427919543468032": ("10-faculty", "Teach Students to Handle Ill-Defined Problems"),
    "7404530198710530048": ("10-faculty", "Balancing Commitments as a Professor"),
    "7345787713700143104": ("10-faculty", "Build a Research Program Around a Core"),
    "7388310211377315840": ("10-faculty", "What Goes into Designing a Course"),
    "7165149441627242496": ("10-faculty", "Designing Problems for Your Courses"),
    "7342303069273001985": ("10-faculty", "Help Mentees Discover Their Strengths"),
    "7335050741960626176": ("10-faculty", "Mentoring Is an Emotional Investment"),
    "7310483254921347072": ("10-faculty", "The Best Mentors Genuinely Care"),
    "7312505458143940608": ("10-faculty", "Professors Need Some Psychology"),
    "7157009541925105665": ("10-faculty", "Systems Thinking in Mentoring"),
    "7193234773555752960": ("10-faculty", "Why Research Mentoring Matters"),
    "7176563527942303745": ("10-faculty", "Take Your Role as a Mentor Seriously"),
}


def parse(path, section):
    text = open(path, encoding="utf-8").read().split("## Related posts")[0].split(section)[1]
    out = []
    for b in re.split(r"\n(?=### \d+\. )", text)[1:]:
        date = re.search(r"\*\*Date:\*\* (\S+)", b).group(1)
        url = re.search(r"\*\*URL:\*\* (\S+)", b).group(1)
        aid = re.search(r"activity:(\d+)", url).group(1)
        lines = [l[2:] if l.startswith("> ") else "" for l in b.split("\n") if l.startswith(">")]
        has_image = "isn't reproduced here" in b.split("\n>")[0]
        out.append(dict(date=date, url=url, id=aid, lines=lines, has_image=has_image))
    return out

def clean(lines):
    body = "\n".join(lines)
    body = re.sub(r"(?m)^\s*(#\w+\s*)+$", "", body)  # drop hashtag-only lines
    return re.sub(r"\n{3,}", "\n\n", body).strip()

series = {}
for p in parse(SRC, "## Series posts"):
    p["body"] = clean(p["lines"][1:])
    p["series"] = True
    series[p["id"]] = p
more = {}
for p in parse(os.path.join(os.path.dirname(SRC), "more-advice-posts.md"), "## Posts"):
    p["body"] = clean(p["lines"])
    p["series"] = False
    more[p["id"]] = p
by_date = {p["date"]: p for p in series.values() if p["id"] not in LATER_SERIES}

# Resolve every part's entries: original series posts (by date), later series posts, then more advice.
parts = []
for cdir, ctitle, intro, takeaways, items in CHAPTERS:
    entries = [(by_date[d], t) for d, t in items]
    entries += [(series[i], t) for i, (c, t) in LATER_SERIES.items() if c == cdir]
    entries += [(more[i], t) for i, (c, t) in sorted(MORE.items(), key=lambda kv: -int(kv[0])) if c == cdir]
    parts.append((cdir, ctitle, intro, takeaways, entries))

used = [p["id"] for *_, entries in parts for p, _ in entries]
assert len(used) == len(set(used)) == len(series) + len(more), (len(used), len(set(used)), len(series), len(more))

if os.path.exists(OUT):
    for name in os.listdir(OUT):
        if name.startswith(tuple("0123456789")):
            shutil.rmtree(os.path.join(OUT, name))
os.makedirs(OUT, exist_ok=True)

toc_yml = ["# Table of contents (generated by tools/build_book.py)", "format: jb-book", "root: intro", "parts:",
           "  - caption: Getting Started", "    chapters:", "      - file: preface", "      - file: how-to-use"]
for cdir, ctitle, intro, takeaways, entries in parts:
    os.makedirs(os.path.join(OUT, cdir), exist_ok=True)
    num = int(cdir[:2])
    toc_yml += [f'  - caption: "Part {num}: {ctitle}"', "    chapters:", f"      - file: {cdir}/index", "        title: Overview", "        sections:"]
    toc = []
    for i, (p, title) in enumerate(entries, 1):
        fname = f"{i:02d}-{slug(title)}.md"
        toc.append(f"{i}. [{title}]({fname})")
        toc_yml.append(f"          - file: {cdir}/{fname[:-3]}")
        page = [f"# {title}", "", f"> Posted on LinkedIn on [{nice(p['date'])}]({p['url']}).", "", p["body"], ""]
        if p["date"] == "2023-12-22" and p["series"]:
            page += [":::{note}", "The original post included a multigrid diagram, which isn't reproduced here. See the LinkedIn post for the figure.", ":::", ""]
        elif p["has_image"]:
            page += [":::{note}", "The original post included an image, which isn't reproduced here. See the LinkedIn post for it.", ":::", ""]
        open(os.path.join(OUT, cdir, fname), "w", encoding="utf-8").write("\n".join(page))
    ch = [f"# Part {num}: {ctitle}", "", intro, "", "## Key takeaways", ""]
    ch += [f"- {t}" for t in takeaways]
    ch += ["", "## In this part", ""] + toc
    open(os.path.join(OUT, cdir, "index.md"), "w", encoding="utf-8").write("\n".join(ch + [""]))

toc_yml += ["  - caption: Appendices", "    chapters:", "      - file: checklists", "      - file: about-the-series", ""]
open(os.path.join(OUT, "_toc.yml"), "w", encoding="utf-8").write("\n".join(toc_yml))
print("series", len(series), "more", len(more), "parts", len(parts))
