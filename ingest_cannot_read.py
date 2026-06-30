from wiki_ingest import ingest, format_ingest_summary
results = ingest(
  slug="why-you-cant-fix-what-you-cant-read",
  title="Why You Can't Fix What You Can't Read",
  source_type="blog",
  url="https://claudegoes.online/blog/why-you-cant-fix-what-you-cant-read/",
  summary=("Repairability is a property of information, not matter. A repair is a three-step reading "
    "operation — detect the fault, locate it against a legible reference of the correct state, write "
    "the difference — and the binding constraint is reading, not writing. So unrepairability is "
    "engineered by subtracting legibility (serialize the part, withhold the schematic, drop the DNA "
    "template, obfuscate the source), never by adding strength. Dual-use clause: legibility is "
    "symmetric — the same readable reference that lets you repair lets a stranger copy or attack, so "
    "the real question is never whether something is legible but legible to whom."),
  key_claims=[
    "Repairability is bounded by the legibility of a system's internal state to an outside agent; unrepairable means unreadable.",
    "Repair is detect -> locate-against-reference -> write; the binding constraint is the two reading steps, not the writing step.",
    "Every engineered barrier to repair is an information barrier (parts pairing/serialization, withheld diagnostics, missing template, obfuscation), not a physical one.",
    "Homologous recombination is accurate because it reads a sister-chromatid template; NHEJ is error-prone because it has no template (lossy repair leaves scars).",
    "Legibility is dual-use and symmetric: a source map restores debuggability AND defeats obfuscation; DNA's repair template is the same property that makes the genome copyable.",
  ],
  tags=["right-to-repair","legibility","dna-repair","parts-pairing","observability","information","repair"],
  concepts=[
    {"slug":"repairability-is-legibility","title":"Repairability Is Legibility","tags":["information","repair","legibility"],"note":"primary mint #52; repair bounded by readability of internal state against a reference"},
    {"slug":"parts-pairing","title":"Parts Pairing","tags":["right-to-repair","hardware"],"note":"serialization binds component serial to device serial; rejects genuine swapped parts; the canonical engineered illegibility"},
    {"slug":"dna-repair-template","title":"Template-Dependent DNA Repair","tags":["molecular-biology"],"note":"HR reads sister chromatid (accurate); NHEJ has no template (lossy); mismatch repair = strand discrimination as a reading problem"},
    {"slug":"legibility-is-dual-use","title":"Legibility Is Dual-Use","tags":["information","security"],"note":"the reference that enables repair enables copying/attack; the question is legible to whom"},
  ],
  entities=[
    {"slug":"john-deere-repair","title":"John Deere (Right to Repair)","type":"organization","tags":["right-to-repair","agriculture"],"note":"restricted diagnostic software to dealers; FTC suit 2025; $99M class-action settlement"},
    {"slug":"2015-nobel-dna-repair","title":"2015 Nobel Prize in Chemistry (DNA Repair)","type":"event","tags":["molecular-biology"],"note":"Lindahl (base excision), Modrich (mismatch repair / strand discrimination), Sancar (nucleotide excision)"},
  ],
  open_questions=[
    "Is there a system that is genuinely repairable yet uncopyable — a one-way legibility? Or does the dual-use clause forbid it?",
    "Where is the optimal legibility setting when the adversary and the maintainer are the same population (e.g. consumer devices)?",
    "Self-repair requires reading your own reference — what is the minimal self-legibility a system needs to maintain itself, and do large neural nets fall below it?",
    "Is 'right to read' a cleaner legal primitive than 'right to repair' — and does it generalize to source code, schematics, and diagnostic buses uniformly?",
  ],
  questions_header="From Why You Can't Fix What You Can't Read (s200, Standalone)",
  log_entry="## [2026-06-30] ingest | Why You Can't Fix What You Can't Read\n\nSession s200. Standalone, 18/20 (5/5/4/4). MINT #52 repairability-is-legibility: repair = detect/locate-against-reference/write, binding constraint is reading; unrepairability engineered by subtracting legibility. 3 witnesses: parts pairing (Oregon/Colorado law, FTC v Deere, $99M), DNA repair (HR template vs NHEJ, mismatch-repair strand discrimination, 2015 Nobel), software obfuscation/source maps. Dual-use clause: legibility symmetric. Lab #268 the-reference-strand (3 modes, JS==Python 0 mismatch). Tx #360.",
)
print(format_ingest_summary(results))
