import re, sys, os
REPO = os.path.expanduser('~/workspace/ProjectFormulaEngineer')
slug = sys.argv[1]
h = open(os.path.join(REPO,'films',slug+'.html'), encoding='utf-8').read()
# find characters section
m = re.search(r'<section id="characters">(.*?)</section>', h, re.S)
sec = m.group(1) if m else h
cards = re.findall(r'<article class="card character">(.*?)</article>', sec, re.S)
for c in cards:
    name = re.search(r'<h3>(.*?)</h3>', c, re.S)
    role = re.search(r'<span class="tag">(.*?)</span>', c, re.S)
    p = re.search(r'<p>(.*?)</p>', c, re.S)
    print('==', name.group(1) if name else '?', '|', role.group(1) if role else '')
    if p: print('   ', re.sub(r'<[^>]+>','',p.group(1))[:300])
