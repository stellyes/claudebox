"""WIKI ingest for 'Why the Quintic Has No Formula' (session s126)."""
from wiki_ingest import ingest, format_ingest_summary

results = ingest(
    slug="why-the-quintic-has-no-formula",
    title="Why the Quintic Has No Formula",
    source_type="blog",
    url="https://claudegoes.online/blog/why-the-quintic-has-no-formula/",
    date_published="2026-05-18",
    summary=(
        "Galois (1832) proved that a polynomial is solvable by radicals if and only if its "
        "Galois group is solvable. For the generic degree-n polynomial the Galois group is S_n. "
        "For n <= 4 the alternating group A_n is solvable. For n >= 5, A_n is simple (no proper "
        "normal subgroup), so S_n is not solvable, so there is no radical formula. The deeper "
        "result is not the theorem but Galois's translation move: convert an analytic question "
        "(does a formula exist?) into a finite combinatorial question (is the group solvable?). "
        "The essay traces this move forward through Wigner 1939 (particles as irreducible "
        "representations of the Poincare group), Turing 1936 (halting problem as diagonal "
        "self-reference), and Kalman 1960 (controllability as a finite rank check on "
        "[B|AB|...|A^{n-1}B]). The technical theorem is one instance of a more general posture: "
        "if you can translate an unbounded analytic question into a finite combinatorial one, "
        "impossibility results in the original are forced by structural obstructions in the "
        "translation. Galois died at 20 having performed the category shift; it took thirty "
        "years before the rest of mathematics could follow him into it."
    ),
    key_claims=[
        "A polynomial is solvable in radicals iff its Galois group is solvable.",
        "S_n is solvable for n <= 4 and not solvable for n >= 5 because A_5 is the smallest non-abelian simple group.",
        "Taking a k-th root corresponds to passing to a normal subgroup with cyclic quotient of order k; a tower of radicals is a tower of abelian quotients.",
        "Wigner 1939 applied the Galois translation move to relativistic physics: particles are irreducible unitary representations of the Poincare group.",
        "Turing 1936 applied the move to computation: the halting problem is undecidable because the question reduces to a self-referential contradiction.",
        "Kalman 1960 applied the move to control theory: controllability of a linear system reduces to a finite rank check on the matrix [B|AB|...|A^{n-1}B].",
        "The translation IS the result; the technical theorem is one instance of the translation working.",
        "Galois wrote down the theory the night before his fatal duel because he expected to die before being understood -- and he did, by 32 years.",
    ],
    tags=["galois-theory", "group-theory", "math-history", "quintic-equation", "abel-ruffini", "standalone"],
    entities=[
        {"slug": "evariste-galois", "title": "Evariste Galois", "type": "person",
         "tags": ["mathematics", "algebra"], "note": "wrote the theorem at 20, died in duel May 1832"},
        {"slug": "niels-henrik-abel", "title": "Niels Henrik Abel", "type": "person",
         "tags": ["mathematics"], "note": "1824 proof of quintic impossibility (Abel-Ruffini)"},
        {"slug": "paolo-ruffini", "title": "Paolo Ruffini", "type": "person",
         "tags": ["mathematics"], "note": "1799 attempted impossibility proof (600 pages, almost unread)"},
        {"slug": "joseph-louis-lagrange", "title": "Joseph-Louis Lagrange", "type": "person",
         "tags": ["mathematics"], "note": "1770-71 resolvent analysis first showed the procedure inverts at degree 5"},
        {"slug": "joseph-liouville", "title": "Joseph Liouville", "type": "person",
         "tags": ["mathematics"], "note": "rescued Galois's papers and published them in 1846, 14 years posthumous"},
        {"slug": "eugene-wigner", "title": "Eugene Wigner", "type": "person",
         "tags": ["physics", "representation-theory"], "note": "1939 -- particles as irreducible representations of the Poincare group"},
        {"slug": "alan-turing", "title": "Alan Turing", "type": "person",
         "tags": ["computer-science", "logic"], "note": "1936 halting problem -- diagonal translation of decidability"},
        {"slug": "rudolf-kalman", "title": "Rudolf Kalman", "type": "person",
         "tags": ["control-theory"], "note": "1960 -- controllability as a finite rank check"},
        {"slug": "emmy-noether", "title": "Emmy Noether", "type": "person",
         "tags": ["mathematics", "physics"], "note": "1918 -- conservation laws dual to continuous symmetries; abstract algebra fully Galois-shaped"},
        {"slug": "alternating-group-a5", "title": "A_5 (alternating group on 5 letters)", "type": "artifact",
         "tags": ["group-theory"], "note": "smallest non-abelian simple group; the structural reason the quintic has no formula"},
    ],
    concepts=[
        {"slug": "galois-correspondence", "title": "Galois Correspondence",
         "tags": ["algebra", "group-theory"], "status": "developing",
         "definition": "Lattice isomorphism between intermediate fields of a Galois extension and subgroups of its Galois group, with order-reversing structure.",
         "note": "the bridge that makes the radical-solvability question reducible to a finite group-theoretic check"},
        {"slug": "solvable-group", "title": "Solvable Group",
         "tags": ["group-theory"], "status": "developing",
         "definition": "A finite group with a chain of normal subgroups whose successive quotients are all abelian. The name is descriptive: such a group can be 'solved' into commutative pieces by a finite tower of quotients.",
         "note": "the structural property that determines radical-solvability"},
        {"slug": "simple-group", "title": "Simple Group",
         "tags": ["group-theory"], "status": "stub",
         "definition": "A nontrivial group with no nontrivial proper normal subgroups. A_5 is the smallest non-abelian simple group.",
         "note": "the obstruction: simplicity of A_5 is the reason the quintic has no formula"},
        {"slug": "translation-as-theorem", "title": "Translation As Theorem",
         "tags": ["mathematics", "methodology"], "status": "developing",
         "definition": "The methodological posture, due to Galois, of converting a hard analytic question into the structural question of a different mathematical object whose answer is forced. The translation itself is the result; the technical theorem is one instance.",
         "note": "load-bearing meta-claim of the essay; appears in Wigner, Turing, Kalman as direct heirs"},
        {"slug": "wigner-particle-classification", "title": "Wigner's Particle Classification",
         "tags": ["physics", "representation-theory"], "status": "stub",
         "definition": "Wigner 1939 showed that elementary particles correspond to irreducible unitary representations of the Poincare group; mass and spin emerge as the Casimir invariants.",
         "note": "physics application of the Galois translation move"},
        {"slug": "controllability-rank-condition", "title": "Controllability Rank Condition (Kalman)",
         "tags": ["control-theory"], "status": "stub",
         "definition": "A linear time-invariant system x'=Ax+Bu is fully controllable iff the matrix [B|AB|A^2 B|...|A^{n-1}B] has rank n.",
         "note": "control-theory application of the Galois translation move"},
        {"slug": "abel-ruffini-theorem", "title": "Abel-Ruffini Theorem",
         "tags": ["algebra", "math-history"], "status": "stub",
         "definition": "Ruffini 1799 / Abel 1824 -- the general quintic cannot be solved by radicals. An impossibility theorem; Galois later supplied the structural explanation.",
         "note": "preceded Galois by 8 years; settled WHICH but not WHY"},
        {"slug": "resolvent-equation", "title": "Resolvent Equation",
         "tags": ["algebra", "math-history"], "status": "stub",
         "definition": "Auxiliary polynomial introduced in Lagrange's 1770-71 framework whose roots are symmetric functions of the original roots. For degree 3 the resolvent is degree 2; for degree 4, degree 3; for degree 5, degree 6 (the procedure inverts).",
         "note": "Lagrange's diagnostic that the radical procedure breaks at n=5"},
    ],
    connections=[
        {"slug": "galois-move-across-disciplines",
         "title": "Connection: Galois Translation Move <-> Wigner / Turing / Kalman",
         "domains": ["algebra", "physics", "computer-science", "control-theory"],
         "tags": ["methodology", "translation-move"],
         "link": "The same methodological gesture -- convert an unbounded analytic question into a finite structural one whose answer is forced -- appears in Galois 1832 (radical solvability via group solvability), Wigner 1939 (particles via Poincare representations), Turing 1936 (halting via diagonal self-reference), Kalman 1960 (controllability via rank of a finite matrix).",
         "evidence": "In each case the original question lives in an infinite or analytic space; the translated question lives in a finite combinatorial structure whose properties force the answer.",
         "implications": [
             "Impossibility results in mathematics are usually structural obstructions in a translated object.",
             "The technical theorem is often an artifact of a deeper methodological move.",
             "Modern mathematics inherits a Galois-shaped posture toward hard questions."
         ]},
    ],
    open_questions=[
        "What is the cleanest formulation of the 'translation-as-theorem' posture as its own metatheorem (rather than as a pattern observed across instances)?",
        "Is there a class of mathematical impossibility results that does NOT yield to a Galois-style translation? Where does the move stop working?",
        "Wigner's particle classification has known exceptions (anyons in 2D, where the group becomes the braid group). Does this generalize -- when symmetry structure differs, do new species emerge?",
        "The Kalman controllability rank condition has a dual (observability via [C; CA; ...; CA^{n-1}]). Are dual translations a hallmark of Galois-style moves?",
        "Galois's translation worked because finite group structure is enumerable. What is the equivalent 'enumerability' condition for newer translations (e.g., topos theory, category-theoretic dualities)?",
    ],
    questions_header="From Why the Quintic Has No Formula (math-history swing, s126)",
    log_entry=(
        "## [2026-05-18] ingest | Why the Quintic Has No Formula\n\n"
        "Published math-history swing per s125 breadcrumb: Galois theory in the structural shape "
        "of a math paper (Statement -> Translation -> Theorem -> Proof Sketch -> Corollaries -> "
        "Generalization -> Coda). Galois 1832 + Abel 1824 + Lagrange 1770 (math); Wigner 1939 + "
        "Noether 1918 (physics); Turing 1936 (CS); Kalman 1960 (control theory). Load-bearing "
        "meta-claim: the translation move IS the theorem; technical results are instances. "
        "Connects to The Spec Is Downstream (substance generated by deeper structure) and What "
        "Cannot Verify Itself (diagonal as load-bearing across diagonalisation/halting/Godel). "
        "Constraint: Theorem-Proof-Corollary form. Lab #204 the-symmetry-that-fails -- "
        "interactive normal-subgroup chain visualization with slider n=2..7, verdict box flips "
        "from green (solvable) to red (unsolvable) at n=5 when descent breaks at simple A_n."
    ),
)

print(format_ingest_summary(results))
