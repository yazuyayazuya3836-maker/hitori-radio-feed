#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""episodes.json から Podcast RSS (feed.xml) を生成する。

使い方:
  1. episodes/ に MP3 を置く
  2. episodes.json の "episodes" にエントリを追記
  3. python3 build_feed.py
  4. git add -A && git commit && git push  → GitHub Pages が自動配信
"""
import json
import os
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "episodes.json")))
ch = data["channel"]
base = ch["link"].rstrip("/")


def fmt_duration(sec):
    h, rest = divmod(int(sec), 3600)
    m, s = divmod(rest, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


items = []
for ep in data["episodes"]:
    path = os.path.join(HERE, ep["file"])
    size = os.path.getsize(path)
    url = f'{base}/{ep["file"]}'
    desc = escape(ep["description"]).replace("\n", "<br/>")
    items.append(f"""    <item>
      <title>{escape(ep["title"])}</title>
      <guid isPermaLink="false">{escape(ep["guid"])}</guid>
      <pubDate>{ep["pub_date"]}</pubDate>
      <enclosure url="{escape(url)}" length="{size}" type="audio/mpeg"/>
      <itunes:duration>{fmt_duration(ep["duration_sec"])}</itunes:duration>
      <itunes:episode>{ep["episode_number"]}</itunes:episode>
      <itunes:explicit>false</itunes:explicit>
      <description><![CDATA[{ep["description"].replace(chr(10), "<br/>")}]]></description>
    </item>""")

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{escape(ch["title"])}</title>
    <link>{escape(ch["link"])}</link>
    <atom:link href="{escape(ch["feed_url"])}" rel="self" type="application/rss+xml"/>
    <description>{escape(ch["description"])}</description>
    <language>{ch["language"]}</language>
    <itunes:author>{escape(ch["author"])}</itunes:author>
    <itunes:owner>
      <itunes:name>{escape(ch["owner_name"])}</itunes:name>
      <itunes:email>{escape(ch["owner_email"])}</itunes:email>
    </itunes:owner>
    <itunes:image href="{escape(ch["image"])}"/>
    <itunes:category text="{escape(ch["category"])}">
      <itunes:category text="{escape(ch["subcategory"])}"/>
    </itunes:category>
    <itunes:explicit>{"true" if ch["explicit"] else "false"}</itunes:explicit>
    <itunes:type>episodic</itunes:type>
{os.linesep.join(items)}
  </channel>
</rss>
"""

out = os.path.join(HERE, "feed.xml")
with open(out, "w", encoding="utf-8") as f:
    f.write(feed)
print(f"wrote {out} ({len(data['episodes'])} episodes)")
