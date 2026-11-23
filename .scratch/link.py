import re, sys, os
REPO = os.path.expanduser('~/workspace/ProjectFormulaEngineer')
# usage: link.py <film-slug> <h3 text>=<char-slug> ...
fslug = sys.argv[1]
pairs = [a.split('=', 1) for a in sys.argv[2:]]
path = os.path.join(REPO, 'films', fslug + '.html')
h = open(path, encoding='utf-8').read()
m = re.search(r'(<section id="characters">)(.*?)(</section>)', h, re.S)
assert m, 'characters section not found'
sec = m.group(2)
for text, cslug in pairs:
    old = f'<h3>{text}</h3>'
    new = f'<h3><a class="character-link" href="../characters/{fslug}/{cslug}.html">{text}</a></h3>'
    assert sec.count(old) == 1, (text, sec.count(old))
    sec = sec.replace(old, new)
h = h[:m.start(2)] + sec + h[m.end(2):]
open(path, 'w', encoding='utf-8').write(h)
print('linked', len(pairs), 'cards in', fslug)
