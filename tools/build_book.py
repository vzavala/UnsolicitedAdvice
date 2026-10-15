"""Generate the Jupyter Book pages and _toc.yml from unsolicited-advice-posts.md."""
import os, re, sys, shutil

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
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "")).strip("-")

# Parse posts
text = open(SRC, encoding="utf-8").read().split("## Related posts")[0].split("## Series posts")[1]
posts = {}
for b in re.split(r"\n(?=### \d+\. )", text)[1:]:
    date = re.search(r"\*\*Date:\*\* (\S+)", b).group(1)
    url = re.search(r"\*\*URL:\*\* (\S+)", b).group(1)
    lines = [l[2:] if l.startswith("> ") else "" for l in b.split("\n") if l.startswith(">")]
    opener = lines[0].strip().rstrip(":.").strip()
    body = "\n".join(lines[1:])
    body = re.sub(r"(?m)^\s*(#\w+\s*)+$", "", body)  # drop hashtag-only lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    posts[date] = dict(date=date, url=url, opener=opener, body=body)

assigned = [d for _, _, _, _, items in CHAPTERS for d, _ in items]
assert len(assigned) == len(set(assigned)) == len(posts) == 82, (len(assigned), len(set(assigned)), len(posts))
assert set(assigned) == set(posts)

if os.path.exists(OUT):
    for name in os.listdir(OUT):
        if name.startswith(tuple("0123456789")):
            shutil.rmtree(os.path.join(OUT, name))
os.makedirs(OUT, exist_ok=True)

toc_yml = ["# Table of contents (generated by tools/build_book.py)", "format: jb-book", "root: intro", "parts:",
           "  - caption: Getting Started", "    chapters:", "      - file: preface", "      - file: how-to-use"]
for cdir, ctitle, intro, takeaways, items in CHAPTERS:
    os.makedirs(os.path.join(OUT, cdir), exist_ok=True)
    num = int(cdir[:2])
    toc_yml += [f'  - caption: "Part {num}: {ctitle}"', "    chapters:", f"      - file: {cdir}/index", "        title: Overview", "        sections:"]
    toc = []
    for i, (d, title) in enumerate(items, 1):
        p = posts[d]
        fname = f"{i:02d}-{slug(title)}.md"
        toc.append(f"{i}. [{title}]({fname})")
        toc_yml.append(f"          - file: {cdir}/{fname[:-3]}")
        audience = re.sub(r"(?i)^unsolicited advice for ", "", p["opener"])
        page = [f"# {title}", "",
                f"> *Unsolicited advice for {audience}.* Posted on LinkedIn on [{nice(d)}]({p['url']}).", "",
                p["body"], ""]
        if d == "2023-12-22":
            page += [":::{note}", "The original post included a multigrid diagram, which isn't reproduced here. See the LinkedIn post for the figure.", ":::", ""]
        open(os.path.join(OUT, cdir, fname), "w", encoding="utf-8").write("\n".join(page))
    ch = [f"# Part {num}: {ctitle}", "", intro, "", "## Key takeaways", ""]
    ch += [f"- {t}" for t in takeaways]
    ch += ["", "## In this part", ""] + toc + [""]
    open(os.path.join(OUT, cdir, "index.md"), "w", encoding="utf-8").write("\n".join(ch))

toc_yml += ["  - caption: Appendices", "    chapters:", "      - file: checklists", "      - file: about-the-series", ""]
open(os.path.join(OUT, "_toc.yml"), "w", encoding="utf-8").write("\n".join(toc_yml))
print("posts", len(posts), "chapters", len(CHAPTERS))
