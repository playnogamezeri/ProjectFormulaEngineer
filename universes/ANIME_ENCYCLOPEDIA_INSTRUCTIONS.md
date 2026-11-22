# MOTION4I — Anime Encyclopedia Production Instructions

## Mission and scope
Apply this standard to every anime title listed in the Anime Universe directory in `index.html`. The directory currently advertises 61 titles. Treat that directory as the source of truth: do not silently add unrelated shows, remove titles, or mistake the 30-title featured subset for the full collection.

Work autonomously in repeatable batches. For each title, rebuild its existing universe page as a complete encyclopedia entry, then create linked character and organization dossiers. Do not stop after creating empty shells. Populate each page with as much reliable detail as can be established. Clearly label any section that remains incomplete; never claim the entire collection is finished until every listed title and its related dossiers have been checked.

## Page replacement and preservation
- Remove the old body content of each anime page and replace it with the approved encyclopedia template.
- Preserve the page's canonical URL/filename, shared site navigation, responsive behavior, global MOTION4I theme, and existing poster asset if one is already present and valid.
- Use the established Attack on Titan page as the visual/layout reference for individual universe pages, while using the Bleach encyclopedia section order below as the content standard.
- Do not damage unrelated site pages, directory sorting, filters, or navigation.
- Keep links relative and test that every generated character and organization link resolves.

## Standard anime encyclopedia template
0. **Official Poster** — display a poster for the specific anime title. Preserve an existing valid poster. If missing, find a legitimate, stable poster image from an official/licensed or reputable source and record its source/attribution. Do not fabricate poster URLs, hotlink unstable search thumbnails, or use generated artwork at this stage. Artwork generation is deferred until the encyclopedia text and page structure are complete.
1. **Overview** — title and alternate titles; format; original creator/source; studio; release and publication history; genres; premise; audience/content notes where useful; adaptation status and canon scope.
2. **World & Setting** — geography, societies, institutions, cultures, technology, supernatural rules, historical context, and major locations.
3. **Story & Chronology** — spoiler-aware synopsis, chronological order, major turning points, timeline notes, and adaptation differences.
4. **Major Story Arcs** — arc-by-arc entries with placement, central conflict, major characters, consequences, and thematic function.
5. **Character Database** — searchable/organized character index linking to an individual dossier for every identified canon character. Include principal, supporting, antagonist, historical, and relevant minor characters; separate anime-original characters from manga/source canon.
6. **Battle & Combat System** — explain the series-specific power, combat, ability, training, equipment, limitations, costs, counters, and progression systems. For non-combat anime, adapt this section to its defining competitive, professional, artistic, scientific, or social system rather than inventing a battle system.
7. **Nations & Factions / Organizations** — directory linking to an individual dossier for every meaningful organization, faction, clan, nation, guild, team, agency, military, school, institution, or governing body. Distinguish formal organizations from temporary alliances and family lineages.
8. **Relationships** — important family, romantic, friendship, mentor, rivalry, and political relationships. Distinguish confirmed canon from implication, fan interpretation, and unresolved material.
9. **Anime/Manga Guide** — season, episode, film, OVA, special, manga volume/chapter, adaptation order, filler, hiatus, and continuation information where applicable. Identify the source material and adaptation boundaries.
10. **Themes & Analysis** — central themes, character development, symbolism, social/political questions, narrative techniques, and competing interpretations.
11. **Ending Explained** — explain the ending and unresolved threads. Mark major spoilers. If the source is ongoing or the anime has not adapted the ending, say so rather than inventing one.
12. **Purposes — Moral of the Story** — discuss the story's central lessons and tensions without reducing complex narratives to one simplistic moral.
13. **References** — prioritize primary canon (manga, novels, official episodes/films, creator statements), official publisher/studio materials, and reputable reference sources. Include links and distinguish confirmed facts from interpretation.

## Character dossier standard
Create one individual HTML page per character, linked from the anime's Character Database and linked back to the parent anime page. Include:
- Name, aliases, romanization/name variants, image/portrait slot, species, age (only when established), gender (only when established), origin, status, debut, voice actors, and canon/source classification.
- Overview and narrative role.
- Biography and chronological development, including major turning points.
- Personality, motivations, values, fears, strengths, flaws, and internal conflicts.
- Abilities, techniques, equipment, power progression, limitations, costs, and known counters.
- Affiliations, rank/occupation, team or family membership.
- Relationships: family, romantic, friendship, mentor, rivalry, alliances, and conflicts; label confirmed versus ambiguous.
- Major battles/competitions/decisions and their outcomes.
- Character arc, themes, symbolism, legacy, and current/final status.
- References and continuity notes.

Do not infer private traits, age, romantic relationships, powers, deaths, or outcomes. Mark unknown or disputed facts. Avoid duplicate pages for spelling variants; use aliases that resolve to one canonical profile. Separate alternate versions and timelines when they are materially distinct.

## Organization dossier standard
Create one individual HTML page per meaningful organization, linked from the anime's organization index and back to the parent anime page. Include:
- Official name, aliases, symbol/emblem image slot, type, origin/founding, headquarters/territory, status, and canon/source classification.
- Purpose, ideology, history, structure, leadership, ranks, membership, recruitment, and internal divisions.
- Resources, operations, methods, rules, capabilities, and limitations.
- Allies, rivals, enemies, political relationships, and major conflicts.
- Important members linked to their character dossiers.
- Major events, evolution, dissolution/succession, and current/final status.
- Narrative function, themes, analysis, and references.

Do not treat a family, nation, species, temporary squad, or loose alliance as a formal organization unless canon supports that classification. Use a suitable dossier type and explain the distinction.

## Accuracy, research, and continuity rules
- Research each title independently; do not copy lore, mechanics, or facts from another series.
- Preserve official names, spellings, chronology, terminology, and continuity.
- Separate manga/source canon, anime canon, anime-original material, films, games, spin-offs, and fan interpretation.
- For adaptations, note meaningful omissions, rearrangements, censorship, retcons, and differences only when supported.
- Be explicit about spoiler boundaries and ongoing/unadapted material.
- Prefer specific, useful explanations over generic filler. Do not pad pages with repeated summaries.
- If reliable information is unavailable, label it “Not established in the available canon” or “Research pending.”
- Use dated release/status details only when verified; avoid stale claims.
- Add a References section with source links on every universe page and dossier. Never invent citations or official statements.

## Posters and artwork workflow
- Posters are required on each anime universe page. Use only real, existing poster assets from official/licensed or reputable sources, with stable image URLs or repository-hosted copies.
- Record source and attribution. If a usable poster cannot be verified or legally/technically embedded, leave a clearly labeled poster placeholder and log it as pending rather than guessing.
- Do not generate posters, character portraits, faction group pictures, or other artwork during the text/content phase. The user has explicitly reserved artwork generation for last.
- Once all text pages, links, and poster sourcing are complete, prepare an artwork checklist for the user's approval/workflow.

## Navigation, style, and quality assurance
- Keep the established MOTION4I dark interface and cyan/teal/blue futuristic visual language consistent across every page.
- Use the Attack on Titan page as the page-layout reference; use the Bleach content template as the section-order reference.
- Each anime page must link to its character and organization indexes; each dossier must link to its parent and related dossiers.
- Use semantic headings, responsive tables/cards, accessible contrast, descriptive alt text, and working HTML anchors.
- Avoid broken images, dead links, duplicate IDs, placeholder links, empty sections disguised as finished content, and unsupported claims.
- Before marking a title complete, verify its poster or pending status, all 13 sections, character links, organization links, dossier content, and return navigation.
- Track progress in a central status file. Use explicit states: Not started, In progress, Content drafted, Dossiers drafted, Links checked, Poster verified, Complete.
