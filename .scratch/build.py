#!/usr/bin/env python3
"""Assemble MOTION4I character pages from a per-film data module.
Usage: python3 build.py <data_module_name>  (module defines FILM and CHARACTERS)
Extracts <style> and <script> verbatim from the film's own page.
"""
import re, sys, os, importlib

REPO = os.path.expanduser('~/workspace/ProjectFormulaEngineer')

def esc(s):
    return s

def render(data):
    film = data.FILM
    fslug, ftitle, fyear = film['slug'], film['title'], film['year']
    fhtml = open(os.path.join(REPO, 'films', fslug + '.html'), encoding='utf-8').read()
    style = re.search(r'<style>(.*?)</style>', fhtml, re.S).group(1)
    script = re.search(r'<script>(.*?)</script>', fhtml, re.S).group(1)
    out_paths = []
    for c in data.CHARACTERS:
        name, cslug = c['name'], c['slug']
        L = []
        L.append('<!doctype html>\n<html lang="en"><head>')
        L.append('<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">')
        L.append('<meta name="theme-color" content="#080b13">')
        L.append(f'<meta name="description" content="MOTION4I Movie Galaxy character archive: {name} of {ftitle} ({fyear}) — biography, personality, relationships, arc, symbolism and analysis. Full spoilers.">')
        L.append(f'<title>{name} — {ftitle} ({fyear}) · MOTION4I Character Archive</title>')
        L.append(f'<style>{style}</style>')
        L.append('</head><body>')
        L.append(f'<header class="top"><a class="brand" href="../../index.html">MOTION<span>4I</span> / THE NEXUS</a><a class="back" href="../../films/{fslug}.html">← FILM ARCHIVE</a></header>')
        pills = ''.join(f'<span class="pill">{p}</span>' for p in c['pills'])
        L.append(f'<section class="hero"><div class="wrap hero-inner"><div class="eyebrow">THE NEXUS · MOVIE GALAXY · CHARACTER ARCHIVE</div><h1><em>{name}</em></h1><p class="subtitle">{c["subtitle"]}</p><div class="meta">{pills}</div><div class="hero-actions"><a class="btn" href="#overview">EXPLORE CHARACTER FILE</a><a class="btn alt" href="#relationships">RELATIONSHIPS</a></div><div class="warning"><b>FULL-SPOILER ARCHIVE:</b> {c["warning"]}</div></div></section>')
        L.append('<main class="wrap layout"><aside class="side"><strong>CHARACTER FILE INDEX</strong>')
        idx = [('overview','01 · Overview'),('identity','02 · Identity & Role'),('biography','03 · Biography'),('personality','04 · Personality & Psychology'),('abilities','05 · Abilities & Skills'),('relationships','06 · Relationships'),('arc','07 · Character Arc'),('symbolism','08 · Symbolism & Themes'),('analysis','09 · Analysis & Investigation'),('moments','10 · Key Moments'),('behind','11 · Behind the Character'),('legacy','12 · Legacy & Significance'),('sources','13 · References')]
        L.append(''.join(f'<a href="#{i}">{t}</a>' for i, t in idx))
        L.append('</aside>\n<div class="content">')

        def section(sid, kick, title, body, open_=False):
            o = ' open' if open_ else ''
            return (f'<section id="{sid}"><div class="section-kicker">{kick}</div><h2>{title}</h2>'
                    f'<details class="section-details"{o}><summary>EXPAND SECTION DETAILS <span>＋</span></summary>'
                    f'<div class="section-detail-body">{body}</div></details></section>')

        # 01 overview
        cards = ''.join(f'<div class="card"><span class="tag">{t}</span><h3>{h}</h3><p>{p}</p></div>' for t, h, p in c['overview_cards'])
        body = (f'<p class="lead">{c["overview_lead"]}</p><div class="grid three">{cards}</div>'
                f'<h3>Place in the story</h3><p>{c["overview_place"]}</p>'
                f'<div class="panel"><h4>Archive scope</h4><p>This file documents {name} as {c.get("scope_pronoun","they appear")} in <i>{ftitle}</i> ({fyear}). Plot and production statements are drawn from the cited sources; personality, symbolism and analysis sections are editorial interpretation, flagged as such, grounded in what the character does on screen.</p></div>')
        L.append(section('overview', '01 / CHARACTER FILE', 'Overview', body, open_=True))

        # 02 identity
        rows = ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in c['identity_rows'])
        body = (f'<div class="table-wrap"><table><thead><tr><th>Field</th><th>Information</th></tr></thead><tbody>{rows}</tbody></table></div>'
                f'<p>{c["identity_p"]}</p>')
        L.append(section('identity', '02 / IDENTITY & ROLE', 'Identity & Role', body))

        # 03 biography
        paras = ''.join(f'<p>{p}</p>' for p in c['bio'])
        body = (f'<div class="spoiler"><details><summary>REVEAL FULL CHARACTER STORY</summary>{paras}</details></div>'
                f'<p class="muted">The biography above is an editorial paraphrase of the documented plot accounts (Wikipedia and the cited sources), not a scene-by-scene transcript.</p>')
        L.append(section('biography', '03 / BIOGRAPHY', 'Biography: Their Story', body))

        # 04 personality
        items = ''.join(f'<h3>{h}</h3><p>{p}</p>' for h, p in c['personality'])
        body = f'<p class="muted">This section is editorial interpretation, grounded in the character\'s on-screen actions.</p>{items}'
        L.append(section('personality', '04 / PERSONALITY & PSYCHOLOGY', 'Personality & Psychology', body))

        # 05 abilities
        cards = ''.join(f'<div class="card"><span class="tag">{t}</span><h3>{h}</h3><p>{p}</p></div>' for t, h, p in c['abilities'])
        body = f'<div class="grid">{cards}</div>'
        L.append(section('abilities', '05 / ABILITIES & SKILLS', 'Abilities, Skills & Weaknesses', body))

        # 06 relationships
        rows = ''.join(f'<tr><td>{a}</td><td>{r}</td><td>{s}</td></tr>' for a, r, s in c['relationships'])
        body = f'<div class="table-wrap"><table><thead><tr><th>Connection</th><th>Relationship</th><th>Story significance</th></tr></thead><tbody>{rows}</tbody></table></div>'
        L.append(section('relationships', '06 / RELATIONSHIPS', 'Relationships', body))

        # 07 arc
        evs = ''.join(f'<div class="event"><b>{b}</b><p>{p}</p></div>' for b, p in c['arc'])
        body = f'<div class="timeline">{evs}</div>'
        L.append(section('arc', '07 / CHARACTER ARC', 'Character Arc', body))

        # 08 symbolism
        items = ''.join(f'<h3>{h}</h3><p>{p}</p>' for h, p in c['symbolism'])
        body = f'<p class="muted">This section is editorial interpretation.</p>{items}'
        L.append(section('symbolism', '08 / SYMBOLISM & THEMES', 'Symbolism & Themes', body))

        # 09 analysis
        items = ''.join(f'<h3>{h}</h3><p>{p}</p>' for h, p in c['analysis'])
        body = f'<p class="muted">This section is editorial analysis. Documented facts are cited to the sources in Section 13; readings of the character\'s function are the archive\'s own.</p>{items}'
        L.append(section('analysis', '09 / ANALYSIS & INVESTIGATION', 'Analysis & Investigation', body))

        # 10 moments
        evs = ''.join(f'<div class="event"><b>{b}</b><p>{p}</p></div>' for b, p in c['moments'])
        body = f'<div class="timeline">{evs}</div>'
        L.append(section('moments', '10 / KEY MOMENTS', 'Key Moments', body))

        # 11 behind
        items = ''.join(f'<h3>{h}</h3><p>{p}</p>' for h, p in c['behind'])
        L.append(section('behind', '11 / BEHIND THE CHARACTER', 'Behind the Character', items))

        # 12 legacy
        paras = ''.join(f'<p>{p}</p>' for p in c['legacy'])
        L.append(section('legacy', '12 / LEGACY & SIGNIFICANCE', 'Legacy & Significance', paras))

        # 13 sources
        lis = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for u, t in c['sources'])
        body = (f'<p>Sources below support the character\'s identity, portrayal, story beats and production context. Personality, symbolism and analysis sections are editorial interpretation, as flagged in place.</p>'
                f'<ul class="source-list">{lis}</ul>'
                f'<div class="panel"><h4>Archive status</h4><p>This character file follows the MOTION4I Character Archive\'s 13-section structure, adapted from the Movie Galaxy film pages: overview, identity, biography, personality, abilities, relationships, arc, symbolism, analysis, key moments, behind the character, legacy and references. Facts, spoiler summaries and editorial interpretations are clearly distinguished.</p></div>')
        L.append(section('sources', '13 / RESEARCH & VERIFICATION', 'References', body))

        L.append(f'<footer class="foot">MOTION4I · THE NEXUS · MOVIE GALAXY · CHARACTER ARCHIVE · {name} — {ftitle} ({fyear})<br><a href="../../films/{fslug}.html">Return to the Film Archive</a> · <a href="../../index.html#movies">Return to Movie Galaxy Index</a></footer>')
        L.append('</div></main>')
        L.append(f'<script>{script}</script></body></html>')
        outdir = os.path.join(REPO, 'characters', fslug)
        os.makedirs(outdir, exist_ok=True)
        path = os.path.join(outdir, cslug + '.html')
        open(path, 'w', encoding='utf-8').write('\n'.join(L))
        out_paths.append(path)
        print('wrote', path, os.path.getsize(path), 'bytes')
    return out_paths

if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    mod = importlib.import_module(sys.argv[1])
    render(mod)
