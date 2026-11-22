import re, sys
LED = '/home/hatch/workspace/goals/motion4i-movie-galaxy/hidden_files/character-pages-progress.md'
def update(num, title, year, slug, detail):
    txt = open(LED, encoding='utf-8').read()
    pat = re.compile(r'^- \[ \] #' + str(num) + r' ' + re.escape(title) + r' \(' + year + r'\) — `' + slug + r'` — TODO$', re.M)
    new = f'- [x] #{num} {title} ({year}) — `{slug}` — DONE: {detail}'
    txt2, n = pat.subn(new, txt)
    assert n == 1, (num, n)
    open(LED, 'w', encoding='utf-8').write(txt2)
    print('ledger updated for', num)
if __name__ == '__main__':
    pass
