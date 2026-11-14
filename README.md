# Formula of Everything — V9

A local-first personal engineering laboratory and cross-disciplinary research workspace.

## Start with what you want to build

The formula library is organized around practical goals before academic formula names. Users can choose among nine build/design categories: Motion & transport; Machines & mechanisms; Energy & efficiency; Electrical & electronics; Materials & chemistry; Math & modeling; Business & growth; Buildings & spaces; and Water & fluid systems.

Every one of the 24 starter formulas includes:
- A practical explanation of what it can help a person create, engineer, estimate or understand.
- An ELI5-style explanation in everyday language and familiar examples.
- The equation, variables and units, calculator, worked example, practical uses, and assumptions/limitations.
- A build-goal category shown on the formula card and used to filter the library.

The build-goal selector narrows the formula list before the user chooses an individual formula. Academic discipline and topic filters remain available too.

## 15 dedicated department pages

The laboratory dashboard groups the approved disciplines into five understandable areas and provides a searchable department directory. Every department has its own page under `departments/`, with a consistent structure:

- A focused introduction describing what the discipline is useful for.
- An ELI5-style explanation of its starter model.
- Its own interactive educational calculator, equation and input fields.
- Assumptions and limitations displayed alongside the result.
- A saved calculation history shared with the main laboratory's local backup system.
- Navigation to the previous/next department, the full directory, formula library and guided journeys.

The 15 dedicated pages are:

1. Advanced Mathematics & Calculus — quadratic equation solver.
2. Physics & Quantum Mechanics — ideal projectile motion.
3. Chemistry & Material Science — molar concentration.
4. Biology & Genetics — Hardy–Weinberg genotype frequencies.
5. Human Anatomy & Physiology — educational cardiac-output estimate.
6. Electrical & Electronics Engineering — DC electrical power.
7. Mechanical Engineering — torque from perpendicular force.
8. Civil Engineering & Architecture — average nominal axial stress.
9. Computer Science & Artificial Intelligence — binary-search comparison bound.
10. Robotics & Automation — differential-drive kinematics.
11. Economics & Business — single-product break-even quantity.
12. Astronomy & Space Engineering — ideal circular-orbit period.
13. Agriculture & Environmental Science — irrigation water volume.
14. Psychology & Cognitive Science — reaction-time descriptive statistics.
15. Everyday Practical Formulas — recipe quantity scaling.

## Navigation and page architecture (V9)

The main dashboard is ordered around a practical workflow: personal workspace → knowledge map → department directory → guided build journeys → formula library → workshop → converters and learning → calculation and equation tools → research exchange. Department pages are separate URLs, not just panels embedded in the dashboard. The shared department model registry lives in `departments/department-data.js`; shared page behavior and styling live in `departments/department.js` and `departments/department.css`.

## Guided engineering journeys (V8)

The guided journey planner starts with a practical build or study goal and then leads through five milestones: define the mission, choose a system architecture, model and calculate, prototype or implement, and test/learn. It includes nine starter pathways:

- Desk-scale electric rover
- Solar USB charging station
- Automated plant irrigation
- Pedestrian bridge concept study (strictly conceptual)
- Indoor air-quality monitor
- Population genetics learning model
- Human movement and ergonomics study
- Classroom satellite orbit model
- Smart pantry and recipe planner

Together, these pathways connect all 15 approved disciplines. Each pathway links to relevant department studios, provides staged tasks and explicit limitations, and saves milestone progress locally in the browser. A user can save a selected pathway as a **private** project proposal in the local research register. No project data is sent to a server.

The pathways are structured educational starting points, not certified designs, construction instructions or professional engineering approvals. Safety-critical work requires qualified review and applicable standards. Health-related examples are educational only and do not diagnose or predict individual outcomes.

## Research workspace and exchange

The research register supports questions, project proposals, design notes, experiments, calculations, prototypes and findings. Records can identify a lead discipline and related disciplines, and preserve objectives, methods, results, assumptions and limitations.

Records default to Private and are stored in this browser. Users can deliberately mark records Public and export only those selected records into a portable JSON package. Importing a package adds records locally; it does not publish them to a server. No automatic cloud sync, hosted database, paid API, account system or automatic publication is included.

## Laboratory capabilities

Project register, research notebook, invention idea planner, formula library, engineering calculation bench, experiment log, curated equation solver, dimensional analysis and unit intelligence, converters, 15 department studios, saved local histories, dark mode and JSON backup/restore. V8 backups include research records, guided journey progress and department calculation history, and accept earlier V2–V7 backup schemas.

## GitHub Pages

The application uses a root `index.html` dashboard plus shared assets and 15 standalone pages under `departments/`. It requires no build step, server, API key or paid service. Keep the folder structure intact. In repository Settings → Pages, select deploy from branch `main` and folder `/(root)`. All department pages share the same model registry and calculator script, so improvements can be made consistently.

## Privacy, scientific quality and safety

Browser storage is not encrypted and may be lost if browser data is cleared or the device/profile is lost. Export backups regularly. Public research packages may contain sensitive information if authors include it; inspect them before sharing.

ELI5 explanations are learning aids, not substitutes for technical definitions. The department studios and calculators are educational starting tools, not comprehensive professional suites or certified engineering software. Dimensional consistency and arithmetic correctness do not establish that a model is physically appropriate. State assumptions and validity limits. Medical, structural, electrical, chemical, environmental and other safety-critical decisions require applicable standards, independent verification, testing and qualified professional review.
