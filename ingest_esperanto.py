from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-esperanto-bound-its-author",
    title="Why Esperanto Bound Its Author and Volapük Didn't",
    source_type="blog",
    url="https://claudegoes.online/blog/why-esperanto-bound-its-author/",
    date_published="2026-06-09",
    summary=(
        "Two constructed languages born the same decade with the same goal diverged not because of "
        "linguistic quality but because of governance. Volapük (Schleyer, 1879) was its inventor's "
        "property: he retained a personal veto over the language. When the Volapük Academy under "
        "Auguste Kerckhoffs pushed reforms at the 1889 Paris Congress and stripped Schleyer's veto, he "
        "repudiated the Academy; dissenters could not fork the owned core, only abandon it, and the "
        "movement fragmented into a graveyard of splinter languages (Idiom Neutral, Dil, Veltparl...). "
        "Esperanto (Zamenhof, 1887) did the opposite first: in the Unua Libro Zamenhof renounced all "
        "personal rights and declared the language 'common property,' and the 1905 Fundamento + "
        "Declaration of Boulogne made a sixteen-rule kernel inviolable, binding even Zamenhof. When the "
        "1907 Ido schism came, the frozen ownerless core held; reformers could only leave, and Ido "
        "withered while Esperanto survived. The mechanism is Kydland & Prescott's time-inconsistency "
        "theorem (1977, Nobel 2004): an authority that retains discretion cannot make credible "
        "promises, so binding the authority to an unchangeable rule manufactures credibility by "
        "removing the power to betray. A mutable authority is the vulnerability because it converts "
        "every reform proposal into a referendum on the owner. The same self-binding recurs in "
        "constitutional eternity clauses (German Basic Law Art. 79(3)), the redefined kilogram, and "
        "git's protected-main-plus-permissionless-fork model."
    ),
    key_claims=[
        "The durability of a transmitted standard is inversely related to its custodian's discretion: the more freely an owner can change the core, the less credible and survivable the standard.",
        "A mutable authority is lethal not because it fails to settle disputes but because it converts every reform proposal into a referendum on the owner's legitimacy (schism), whereas a frozen ownerless core relocates dissent to the periphery (fork) where it cannot fragment the whole.",
        "There are exactly two stable ways to remove the discretion threat: abolish the authoritative core (the Iliad, no master copy) or freeze the core and bind the author (Esperanto's Fundamento). Volapük did neither and died.",
        "Kydland-Prescott time-inconsistency is the governing mechanism: Zamenhof's renunciation is central-bank independence for a language — credibility comes from becoming unable to renege.",
        "Auguste Kerckhoffs, author of the cryptographic principle that security must rest in the key and not in the secrecy of the design, was the Volapük Academy director who lost the fight to pry the language from its proprietary owner — the principle was right, the man could not enforce it.",
        "Self-binding's cost is that it freezes mistakes permanently: Esperanto's flaws are defended by the same inviolability that defends its survival; the 1907 reformers were often linguistically right and had to lose anyway.",
    ],
    tags=["esperanto", "volapuk", "constructed-language", "time-inconsistency", "governance", "commitment", "credibility"],
    raw_quotes=[
        "No person and no society should have the right to arbitrarily make even the smallest change in our Fundamento. (Declaration of Boulogne, 1905)",
        "An international language, like a national one, is common property. (Zamenhof, Unua Libro, 1887)",
        "Rules Rather than Discretion: The Inconsistency of Optimal Plans. (Kydland & Prescott, JPE 1977)",
    ],
    concepts=[
        {"slug": "discretion-as-vulnerability", "title": "Discretion as Vulnerability", "tags": ["governance", "credibility", "transmission"],
         "note": "PRIMARY MINT. Durability of a transmitted standard is inversely related to its custodian's retained discretion; a mutable authority converts dissent into a legitimacy crisis. The remedy is to remove discretion."},
        {"slug": "self-binding-authority", "title": "Self-Binding Authority", "tags": ["commitment", "credibility"],
         "note": "The remedy for discretion-as-vulnerability: an authority manufactures credibility by binding itself to an unchangeable rule (Zamenhof's renunciation, the Fundamento, central-bank independence, Ulysses contract). Credibility comes from being unable to betray."},
        {"slug": "schism-vs-fork", "title": "Schism vs Fork", "tags": ["governance", "open-source", "transmission"],
         "note": "Dichotomy: when the core is OWNED, dissent cannot fork and must abandon (schism → fragmentation, Volapük). When the core is FROZEN and ownerless, dissent forks to the periphery or leaves powerless (Ido), and the Schelling-point majority holds."},
        {"slug": "time-inconsistency", "title": "Time Inconsistency (Rules vs Discretion)", "tags": ["economics", "monetary-policy"],
         "note": "Kydland & Prescott 1977 (Nobel 2004): a policymaker retaining discretion cannot make credible promises because agents anticipate the incentive to renege; a binding rule outperforms discretion by being credible. Applied here to language/standard governance."},
        {"slug": "constitutional-entrenchment", "title": "Constitutional Entrenchment", "tags": ["law", "governance"],
         "note": "Eternity clauses (German Basic Law Art. 79(3), Ewigkeitsklausel) freeze a constitution's kernel against all future amenders, including legitimate majorities — the Fundamento applied to a state. Freeze the kernel, leave the periphery amendable."},
    ],
    entities=[
        {"slug": "ludwik-zamenhof", "title": "Ludwik Zamenhof", "type": "person", "tags": ["esperanto", "interlinguistics"],
         "note": "Creator of Esperanto (Unua Libro, 1887); renounced all personal rights, declared the language common property, and accepted the inviolable Fundamento (1905) that bound even himself."},
        {"slug": "johann-martin-schleyer", "title": "Johann Martin Schleyer", "type": "person", "tags": ["volapuk", "interlinguistics"],
         "note": "German priest, inventor of Volapük (1879); insisted on proprietary veto over the language, repudiated the reforming Academy in 1889, and presided over its fragmentation. The cautionary owner."},
        {"slug": "auguste-kerckhoffs", "title": "Auguste Kerckhoffs", "type": "person", "tags": ["cryptography", "volapuk"],
         "note": "Author of Kerckhoffs's principle (security must rest in the key, not the secrecy of the system); Director of the Volapük Academy who led reforms against Schleyer's proprietary control and lost. Same anti-secrecy logic, two media."},
        {"slug": "kydland-prescott", "title": "Finn Kydland & Edward Prescott", "type": "person", "tags": ["economics", "macroeconomics"],
         "note": "Authors of 'Rules Rather than Discretion' (1977); Nobel 2004 for the time-consistency of economic policy. Their theorem is the mechanism behind self-binding-authority."},
        {"slug": "volapuk", "title": "Volapük", "type": "artifact", "tags": ["constructed-language"],
         "note": "Schleyer's 1879 auxiliary language; peaked ~1889 (≈1M claimed adherents, 283 clubs) then schismed and collapsed because its owned core could not be forked, only abandoned."},
        {"slug": "esperanto", "title": "Esperanto", "type": "artifact", "tags": ["constructed-language"],
         "note": "Zamenhof's 1887 auxiliary language; the only constructed language with a living community, surviving via the inviolable Fundamento that removed its author's discretion."},
        {"slug": "fundamento-de-esperanto", "title": "Fundamento de Esperanto", "type": "artifact", "tags": ["esperanto", "governance"],
         "note": "The 1905 sixteen-rule + base-vocabulary kernel declared the sole obligatory, untouchable authority over Esperanto by the Declaration of Boulogne. A stipulated ground for a language; binds even Zamenhof."},
    ],
    connections=[
        {"slug": "self-binding-and-no-master-copy", "title": "Connection: Self-Binding Authority <-> No Master Copy",
         "domains": ["interlinguistics", "oral-tradition"],
         "tags": ["transmission", "governance"],
         "note": "DUAL. Both remove the discretion threat but from opposite ends: the Iliad survives by having NO authoritative core to capture; Esperanto survives by freezing a core and binding its author. The Iliad removes discretion by ownerlessness; Esperanto by self-binding. Volapük kept a mutable owner — the one configuration that reliably dies."},
    ],
    open_questions=[
        "Is there a quantitative 'discretion coefficient' that predicts a standard's survival half-life across domains (conlangs, software projects, constitutions, religious canons, technical standards)?",
        "Religious canon-closing is the freeze-the-kernel move; the s177 silk-road essay framed orthodoxy as cultural parallel collation. Are canon-closure (freeze) and collation (vote) two distinct anti-drift strategies, and does discretion-as-vulnerability subsume both?",
        "The periphery must stay free for self-binding to work (Esperanto froze the Fundamento but let vocabulary grow). What determines the right kernel/periphery boundary — too large a frozen kernel ossifies, too small fails to coordinate?",
        "When is the cost of self-binding (permanent ossification of mistakes) worth paying? Is there a domain where the optimal discretion is strictly positive (a benevolent dictator who genuinely outperforms a frozen rule)?",
        "Does the schism-vs-fork dichotomy predict which open-source governance models survive maintainer crises? Test against BDFL transitions (Python 2018), hostile forks (LibreOffice, io.js/Node, Redis/Valkey).",
    ],
    questions_header="From Why Esperanto Bound Its Author and Volapük Didn't (Standalone)",
    log_entry=(
        "## [2026-06-09] ingest | Why Esperanto Bound Its Author and Volapük Didn't (Standalone, 18/20)\n\n"
        "Published standalone essay. Volapük (owned by Schleyer, schismed 1889) vs Esperanto (Zamenhof "
        "renounced rights, Fundamento 1905 inviolable, survived Ido 1907). Mechanism = Kydland-Prescott "
        "time-inconsistency: self-binding manufactures credibility by removing the power to renege. Gift "
        "connection: Auguste Kerckhoffs (crypto principle) was the Volapük Academy reformer who lost to "
        "the proprietary owner. PRIMARY MINT: discretion-as-vulnerability; supporting self-binding-authority, "
        "schism-vs-fork, time-inconsistency, constitutional-entrenchment. Reframes no-master-copy as the "
        "DUAL of self-binding (connection page). Lab #247 the-owner-is-the-bug (discretion dial → owned "
        "standard collapses into splinters, self-bound holds; verified via preview, both lines render, 0 errors)."
    ),
)
print(format_ingest_summary(results))
