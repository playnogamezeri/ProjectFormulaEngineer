# Formula of Everything — V5

A local-first personal engineering laboratory for learning, calculating, recording experiments and developing inventions.

## V5: Dimensional Analysis & Unit Intelligence
- Unit converter expanded across length, area, volume, mass, time, speed, acceleration, force, energy, power, pressure, density, voltage, current, resistance, frequency and absolute temperature.
- Explicit SI scale factors for supported units; absolute temperature conversion includes offsets.
- SI base-dimension signatures for seven SI base dimensions (length, mass, time, electric current, thermodynamic temperature, amount of substance and luminous intensity).
- Dimensional consistency audit for all 12 curated equation models carried forward from V4.
- Equation audit displays left/right dimension signatures and the dimensions assigned to each variable.
- V5 JSON backup schema retains V2/V3/V4 compatibility and includes all existing laboratory records.

## Existing features retained
- 15 knowledge disciplines, formula library, supported calculators and practical project guides.
- Personal project register, research notebook, invention idea inbox, calculation bench and experiment log.
- Curated equation solving engine with explicit rearrangements, unit-aware inputs and saved solution history.
- Browser-local storage, JSON backup/restore, dark mode and responsive layout.

## Run locally or publish with GitHub Pages
Open `index.html` in a modern browser. No build step, package installation, API key or server is required. To publish, place `index.html`, `styles.css`, `app.js` and this README in the repository root and configure GitHub Pages to deploy from the `main` branch and `/(root)`.

## Data and privacy
Projects, notes, ideas, calculations, experiments and equation history are stored in the current browser profile using localStorage. This prototype does not send these records to a server. Browser storage is not encrypted and is accessible to someone with access to the same browser profile. Browser cleanup, profile reset or device loss can erase records. Export regular JSON backups and store them securely. Public source code does not make each user's browser-local lab records public.

## Scientific and engineering limits
The equation solver is curated, not a general-purpose symbolic algebra system. The dimensional checker validates the dimensions encoded for the listed models; it does not prove physical correctness, derivation, model suitability, input accuracy or operating-range validity. Unit conversions do not establish measurement traceability. Critical electrical, structural, pressure, chemical, medical and life-safety designs require applicable standards, independent verification, testing and qualified professional review.

## Scope
This is an evolving personal engineering laboratory, not a complete scientific database or certified engineering tool. Coverage across all 15 disciplines remains a development roadmap.