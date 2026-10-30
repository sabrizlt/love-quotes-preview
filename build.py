#!/usr/bin/env python3
"""Genera le pagine dell'anteprima con testata e piede in comune: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
BUY_QUIET = "https://mybook.to/thequietartofnoticing"
BUY_HEALING = "https://www.amazon.com/dp/B0GWGK5334"
EMAIL = "hi@love-quotes.com"
SOCIALS = [
    ("Instagram", "https://instagram.com/love.quotes"),
    ("Threads", "https://www.threads.net/@love.quotes"),
    ("Facebook", "https://www.facebook.com/lovequotesmedia"),
    ("TikTok", "https://www.tiktok.com/@thelovequotes"),
    ("Spotify", "https://open.spotify.com/playlist/25cQGZJEVviMRgtNV8DTJt"),
]
NAV = [("shop.html", "Shop"), ("about.html", "About"), ("contacts.html", "Contacts")]


def links(items):
    return "".join(f'<li><a href="{href}" target="_blank" rel="noopener noreferrer">{label}</a></li>' for label, href in items)


def page(filename, title, description, body, current=None):
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>' for href, label in NAV
    )
    pages = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="styles.css">
<script src="site.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="bar">
    <a class="brand" href="index.html" aria-label="Love Quotes, home"><img src="assets/logo.png" alt="Love Quotes"></a>
    <nav class="site-nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="footer-top">
    <a href="index.html" aria-label="Love Quotes, home"><img src="assets/footer-logo.png" alt="Love Quotes"></a>
    <div class="footer-cols">
      <div><h2>Explore</h2><ul>{pages}</ul></div>
      <div><h2>Follow</h2><ul>{links(SOCIALS)}</ul></div>
      <div><h2>Contact</h2><ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 love-quotes. All rights reserved.</span>
    <span>Created by <a href="https://www.linkedin.com/in/sabri-zaltni-704310270/" target="_blank" rel="noopener noreferrer">Sabri Zaltni</a></span>
  </div>
</footer>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")


page("index.html", "Love Quotes", "Poetry, thoughts and books for those who feel deeply and observe the world in silence.", f"""
<section class="hero">
  <div class="reveal">
    <p class="eyebrow">Love Quotes</p>
    <h1>For those who <em>feel deeply</em> and observe the world in silence.</h1>
    <p class="lede">Fifteen years of words dedicated to those who love to reflect, get lost, and find themselves between the lines.</p>
    <div class="actions">
      <a class="btn" href="book-quiet-art.html">The quiet art of noticing</a>
    </div>
  </div>
  <div class="hero-media" aria-hidden="true">
    <video src="assets/dandelion.mp4" autoplay muted loop playsinline></video>
  </div>
</section>

<section class="section dark">
  <div class="feature">
    <img class="reveal" src="assets/quiet-art-cover.jpg" alt="Cover of The quiet art of noticing">
    <div class="reveal">
      <p class="eyebrow">The book</p>
      <h2>The quiet art of noticing</h2>
      <p class="lede">“The quiet art of noticing” is a curated collection of poetry, thoughts, and reflections born from quiet observation.</p>
      <p class="muted">Written for the subtle spectators of life – those who sit back, feel every moment vividly, and perceive what others often miss – this book serves as a companion for sensitive minds. It is a gentle reminder that there is profound strength, beauty, and art in simply paying attention to the world around you.</p>
      <div class="actions">
        <a class="btn btn-buy" href="{BUY_QUIET}" target="_blank" rel="noopener noreferrer">Buy on Amazon</a>
        <a class="btn" href="shop.html">Go to shop</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="story">
    <div class="reveal">
      <p class="eyebrow">About</p>
      <h2>The art of feeling</h2>
      <div class="prose">
        <p>Love Quotes is a digital sanctuary born to explore the infinite, often unspoken nuances of human connection, solitude, and personal growth. A safe space for moments when you don’t know how to feel, inviting you to slow down, listen to your inner voice, and discover that you are never truly alone in what you carry.</p>
      </div>
      <div class="figures">
        <div><strong>5M</strong><span>followers on Instagram</span></div>
        <div><strong>15</strong><span>years of words</span></div>
      </div>
      <div class="actions"><a class="btn" href="about.html">About</a></div>
    </div>
    <figure class="reveal"><img src="assets/quiet-art-table.jpg" alt="The quiet art of noticing on a table, next to a cup of coffee and autumn leaves" loading="lazy"></figure>
  </div>
</section>

<section class="section quote">
  <blockquote class="reveal">We are never truly alone in what we carry.</blockquote>
</section>
""")

BOOKS = [
    ("book-quiet-art.html", "The quiet art of noticing", "assets/quiet-art-cover.jpg", "$12.90"),
    ("book-agenda-2027.html", "Weekly Agenda 2027", "assets/agenda-2027.jpg", "Coming soon"),
    ("book-art-of-healing.html", "The art of healing", "assets/art-of-healing.png", "Coming soon"),
]
cards = "".join(f"""
  <article class="book reveal">
    <a class="book-cover" href="{href}"><img src="{image}" alt="Cover of {title}" loading="lazy"></a>
    <h2><a href="{href}">{title}</a></h2>
    <p class="meta">{meta}</p>
    <a class="text-link" href="{href}">Discover</a>
  </article>""" for href, title, image, meta in BOOKS)

page("shop.html", "Shop – Love Quotes", "Books and creative spaces designed to give shape to what you feel.", f"""
<header class="page-head reveal">
  <p class="eyebrow">Books</p>
  <h1>Stories made to be felt.</h1>
  <p class="lede">Discover our books and creative spaces – designed to give shape to what you feel and bring a moment of clarity to your day.</p>
</header>
<section class="books" aria-label="Books">{cards}
</section>
""", "shop.html")


def book(filename, title, image, status, tagline, paragraphs, action):
    prose = "".join(f"<p>{text}</p>" for text in paragraphs)
    page(filename, f"{title} – Love Quotes", tagline or title, f"""
<section class="book-page">
  <div class="cover reveal"><img src="{image}" alt="Cover of {title}"></div>
  <div class="reveal">
    <a class="back" href="shop.html">← Back to shop</a>
    <p class="eyebrow">{status}</p>
    <h1>{title}</h1>
    {f'<p class="tagline">{tagline}</p>' if tagline else ''}
    {f'<div class="prose">{prose}</div>' if prose else ''}
    {action}
  </div>
</section>
""", "shop.html")


book("book-quiet-art.html", "The quiet art of noticing", "assets/quiet-art-cover.jpg", "$12.90",
     "For those who feel deeply and observe the world in silence.", [
         "“The quiet art of noticing” is a curated collection of poetry, thoughts, and intimate reflections born entirely from quiet observation and solitude.",
         "Written for the subtle spectators of life – those who sit back, feel every shift in the air vividly, and perceive the small, invisible details that others often overlook – this book serves as a silent companion for sensitive minds.",
         "It explores the spaces between words, the weight of unsaid things, the beauty of slowing down, and the quiet resilience found in healing. Each page is designed to feel like a conversation with your own thoughts, offering a gentle reminder that there is profound strength, hidden poetry, and art in simply paying attention to the world around you, and to yourself.",
         "Whether you read it slowly before sleep or open it on a quiet afternoon when you need to feel understood, this collection is a place to land when your mind is full and your heart is listening.",
     ], f'<div class="actions"><a class="btn btn-buy" href="{BUY_QUIET}" target="_blank" rel="noopener noreferrer">Buy now</a></div>')

book("book-agenda-2027.html", "Weekly Agenda 2027", "assets/agenda-2027.jpg", "Coming soon", "", [], "")

book("book-art-of-healing.html", "The art of healing", "assets/art-of-healing.png", "Coming soon",
     "A mindful coloring journey to quiet the mind, release anxiety, and re-anchor yourself.", [
         "Designed as a creative sanctuary from daily stress, The ART of Healing invites you to slow down, breathe, and re-engage with your inner self through art therapy. More than just a coloring book, it is a visual journey through serene spaces… guiding you from surreal, abstract worlds to iconic real-world locations and mysterious ancient sites.",
         "Each chapter opens with a thoughtful reflection on emotional healing, followed by intricate illustrations and a meditative mandala designed to promote deep relaxation. Whether you are seeking stress relief, a creative outlet, or a peaceful path toward healing parts of yourself, this book offers a quiet space to unplug, unwind, and piece together what truly matters.",
         "ISBN: 979-8255116997",
     ], f'<div class="actions"><a class="btn btn-buy" href="{BUY_HEALING}" target="_blank" rel="noopener noreferrer">On Amazon</a></div>')

page("about.html", "About – Love Quotes", "The story of the Love Quotes project, in the words of its founder, Nick.", """
<section class="about-hero">
  <video src="assets/swing.mp4" autoplay muted loop playsinline aria-hidden="true"></video>
  <h1 class="reveal">The <em>Love Quotes</em><br>Project</h1>
</section>
<section class="about-body">
  <div class="prose reveal">
    <p class="opening">Hello there, I’m Nick. Welcome to my world.</p>
    <p>It all started back in 2011. I was just a fifteen-year-old kid looking for a safe space to express what I was feeling inside… A quiet, unburdened corner to process my thoughts, unravel my silences, and give a genuine voice to my emotions. That’s when I turned to social media and created a small, modest quote blog to share reflections of all kinds, with no grand masterplan, just an urgent need to connect with something true.</p>
    <p>As I grew older, my vision inevitably evolved. Life taught me nuance, pain, wonder, and the quiet complexities of human experience. Because of that, I chose to narrow my focus onto what truly matters most: love, human connection, and the intricate architecture of our inner lives. That’s how Love Quotes truly found its identity, shifting from a random collection of thoughts into a focused, deliberate path of emotional exploration.</p>
    <p>Today, Love Quotes is no longer just a place where I express my personal feelings. It has grown into a collective sanctuary where millions of people recognize themselves, find comfort in moments of fragility, and realize a fundamental truth: we are never truly alone in what we carry.</p>
    <p>And because words were never meant to stay trapped behind a glass screen, what began as digital reflections has now naturally expanded into physical books and daily companions. Crafting poetry and quote collections is our way of giving a tangible, physical shape to what you feel… Something you can hold in your hands, turn the pages of, and keep by your bedside.</p>
    <p>After fifteen years, the core goal remains entirely unchanged: to keep inspiring this community, to honor the beauty of vulnerability, and to stay endlessly inspired by life, growth, and love in all its infinite forms.</p>
    <p>Thank you for being a part of this journey.</p>
    <p class="sign">—Nick</p>
  </div>
  <figure class="reveal"><video src="assets/billboard.mp4" autoplay muted loop playsinline aria-label="A Love Quotes billboard on a city building at night"></video></figure>
</section>
""", "about.html")

channels = "".join(f'<li><a href="{href}" target="_blank" rel="noopener noreferrer">{label}</a></li>' for label, href in SOCIALS)
page("contacts.html", "Contacts – Love Quotes", "Suggestions, partnerships, collaborations or a message to share your experience.", f"""
<section class="contact">
  <div class="reveal">
    <p class="eyebrow">Contact</p>
    <h1>Get in touch with us</h1>
    <a class="mail text-link" href="mailto:{EMAIL}">{EMAIL}</a>
    <ul class="channels">{channels}</ul>
  </div>
  <div class="reveal">
    <p class="lede">Whether it’s suggestions, partnerships, collaboration opportunities, or simply a message to share your experience with us, our team is at your disposal to listen. We’re always happy to connect with our community.</p>
    <p class="muted" style="margin:1.25rem 0 3rem">If you have questions, requests for information, or want to collaborate with us, please fill out the form below, and we’ll respond as soon as possible. We invite you to complete all required fields to enable us to provide a clear and prompt response.</p>
    <form>
      <label class="field"><span>First name *</span><input name="first" required autocomplete="given-name"></label>
      <label class="field"><span>Last name *</span><input name="last" required autocomplete="family-name"></label>
      <label class="field full"><span>Email *</span><input name="email" type="email" required autocomplete="email"></label>
      <label class="field full"><span>Message *</span><textarea name="message" rows="5" required></textarea></label>
      <div><button class="btn" type="submit">Send</button></div>
      <p class="form-note" role="status"></p>
    </form>
  </div>
</section>
""", "contacts.html")
