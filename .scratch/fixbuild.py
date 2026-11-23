#!/usr/bin/env python3
"""Pre-build fixer + build wrapper.
Normalizes known data-module bug classes before rendering:
- arc/moments entries written as 3-tuples (label, title, text) -> 2-tuples ('label — title', text)
- arc/moments scalar string entries wrapped into 1-tuples -> left to fail loudly (none expected)
Usage: python3 fixbuild.py <data_module_name>
"""
import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build

def fix(mod):
    for c in mod.CHARACTERS:
        for field in ('arc', 'moments'):
            out = []
            for e in c[field]:
                if isinstance(e, tuple) and len(e) == 3:
                    out.append((e[0] + ' — ' + e[1], e[2]))
                elif isinstance(e, tuple) and len(e) == 2:
                    out.append(e)
                else:
                    raise ValueError(f"{c['slug']} {field}: bad entry {e!r}")
            c[field] = out
        for field in ('personality', 'symbolism', 'analysis', 'behind'):
            for e in c[field]:
                assert isinstance(e, tuple) and len(e) == 2, (c['slug'], field, e)
        for field in ('overview_cards', 'abilities', 'relationships'):
            for e in c[field]:
                assert isinstance(e, tuple) and len(e) == 3, (c['slug'], field, e)
        for e in c['identity_rows']:
            assert isinstance(e, tuple) and len(e) == 2, (c['slug'], 'identity_rows', e)
    return mod

if __name__ == '__main__':
    mod = importlib.import_module(sys.argv[1])
    fix(mod)
    build.render(mod)
