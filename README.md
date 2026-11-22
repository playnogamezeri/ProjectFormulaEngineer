# MOTION4I — The Nexus

A growing, source-conscious entertainment encyclopedia for anime and television. The project organizes series, characters, episodes, creative personnel, story worlds and critical analysis into dedicated, interconnected reference pages.

**Live website:** https://playnogamezeri.github.io/ProjectFormulaEngineer/

## Worlds

### Anime World
The Anime World is a multi-universe encyclopedia covering series across action, adventure, supernatural fantasy, martial arts, science fiction and sports.

Current universe directory:
- Naruto
- Dragon Ball Z
- Bleach
- One Piece
- Hunter × Hunter
- Beelzebub
- Jujutsu Kaisen
- Fullmetal Alchemist: Brotherhood
- My Hero Academia
- Attack on Titan
- Hajime no Ippo
- The Prince of Tennis
- Haikyu!!
- Eyeshield 21
- History's Strongest Disciple Kenichi
- Yu Yu Hakusho
- The Seven Deadly Sins
- Chainsaw Man
- Toriko
- Fairy Tail
- Soul Eater
- Death Note
- Code Geass
- Demon Slayer: Kimetsu no Yaiba
- Vinland Saga
- Solo Leveling
- Gintama
- Rurouni Kenshin
- Berserk
- One-Punch Man

Individual universe pages connect to character dossiers and other reference material. Coverage is being expanded progressively; a listed universe or profile should not be assumed complete merely because its page exists.

### Television World
The Television World applies a format-aware encyclopedia structure to television programmes.

**Current model entry**
- [CBS Summer Playhouse (1987–1989)](https://playnogamezeri.github.io/ProjectFormulaEngineer/television/cbs-summer-playhouse.html) — anthology-series overview, broadcast and production profile, season history, episode guide, pilot catalogue, performers, pilot outcomes, themes, legacy and sources.

CBS Summer Playhouse is the template example for future television entries. The structure is designed to adapt to each programme's format: anthology, sitcom, drama, crime series, miniseries, variety programme or other television form. Episode and cast records should reflect the actual production format rather than forcing every show into the same model.

## Character and episode research

Character dossiers can include:
- Identity, background and life chronology
- Personality and psychological characterization
- Affiliations, relationships and narrative role
- Abilities, techniques, limitations and demonstrated feats
- Canon status, adaptation differences and continuity notes
- Individual character portrait artwork where available
- References and clearly identified research gaps

Television entries can include:
- Series identity, format and broadcast history
- Seasons and episode-by-episode catalogue
- Pilot concepts and development outcomes
- Cast, guest performers and creative personnel
- Performance reviews and character/role analysis
- Reception, legacy and source verification

## Research standards

Information should be distinguished as **Canon / primary record**, **Secondary source**, **Interpretation**, **Fan theory**, or **Real-world comparison**, as appropriate.

- Cite sources for factual claims and identify what each source supports.
- Do not present an interpretation as an established fact.
- Preserve meaningful disagreements between databases and historical records; explain conflicts rather than silently choosing a total.
- Distinguish a pilot broadcast from a series order or full-season commission.
- Distinguish a guest appearance from a regular cast role.
- Keep adaptation-specific details separate when anime, manga, films or television versions differ.
- Mark unknown or unverified details as research gaps instead of inventing information.

## Design and implementation

- Static, responsive HTML/CSS pages hosted with GitHub Pages.
- Shared styling and reusable page structures where practical.
- Interconnected directories, section navigation and individual reference pages.
- Portrait assets stored in `assets/characters/Portraits/` and displayed on individual character dossiers; the anime character index is kept text-focused.
- No build step or backend is required for the current static site.

## Repository structure

- `index.html` — main MOTION4I website entry point.
- `universes/` — Anime World universe encyclopedias and related pages.
- `universes/characters/` — individual anime character dossiers.
- `television/` — Television World programme encyclopedias.
- `assets/characters/Portraits/` — individual character portrait assets.

## Development approach

Work is delivered in verifiable increments. A page, image or section is considered complete only after its repository file exists, its links and asset paths are checked, and the live deployment is allowed to update. Directory counts and coverage claims should reflect the current repository rather than planned work.

## Local use

Open `index.html` in a modern browser. The current site is primarily static and can be browsed without a backend or paid service.

## Archive

The previous Formula of Everything engineering site is preserved in Git branch `archive/formula-engineer-2026-11-15`.
