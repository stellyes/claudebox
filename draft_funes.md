# Why Funes the Memorious Couldn't Think

In June of 1942, a small newspaper story appeared on page three of the Arts and Letters section of *La Nación* in Buenos Aires.[^1] A young man named Ireneo Funes had been thrown from a horse in the town of Fray Bentos, on the Uruguayan side of the Río Uruguay. He awoke from the accident paralyzed and with a perfect memory.

The piece runs to nine pages. It is a portrait, almost a deposition, of a person who can remember everything and therefore cannot think. Most of what Borges later wrote would be read as a parable. This one was a clinical prediction.

## The Boy in Fray Bentos

Before the accident Ireneo Funes was an ordinary cattle-country teenager who could tell what time it was without consulting any watch.[^2] After the accident he could tell what time it was, what shape the clouds had been at that hour on a particular morning three years earlier, and the precise marbling of dust on the lapel of the gentleman who had passed by during the storm of the 30th of April, 1882. He was nineteen when the narrator, returning to Fray Bentos in 1887, last saw his face. He died of pulmonary congestion not long after.

The narrator tells us, almost in passing, that the boy was incapable of Platonic ideas — of generalities, of abstraction. His world was *intolerably uncountable details*.[^3] The phrase is exact. There is no countable infinity in the story, only a refusal of category.

## The Inventory of a Day

In his paralyzed lucidity Funes undertook two projects. The first was a system of numerical names. The second was the reconstruction of a single past day.

The second project failed not because his memory failed but because each remembered day required a full day to remember. The remembering ran in real time. There was no compression ratio.[^4] He could replay 1882 only at the speed of 1882.

If you accept this — and the story makes it physical, not metaphorical — you have something close to the lower bound on what a mind without abstraction can do. Such a mind is a tape head moving at unity speed across an unboundedly long tape. The throughput is fixed by the substrate. There is no other way to render the contents of the tape than to play the tape.

## The Numbering System

The system Funes proposed in place of decimal notation was to give each integer its own name. The number 7,013 became *Máximo Pérez*; 7,014 was *the railroad*; 500 was *nine*; another number was *Napoleon*. Borges glosses this dismissively: this is not a numbering system; it is the opposite of one. The whole point of the decimal positional system — recursion over ten symbols, generating any integer by composition — was unavailable to Funes because the very move that built it (treat 500 as five-times-a-hundred, treat each digit as standing in for any one of ten possibilities) was a move he refused to make.[^5]

That refusal is the same refusal under his inability to think. To say *five hundred* instead of *Napoleon* is to abandon the concrete particular thing — the specific feeling of five-hundredness — for a procedural shorthand that fits the shape of every five-hundred there will ever be. It is to *forget the difference between this 500 and the next 500*.

## Why He Could Not Think

The single sentence in the story that everyone quotes — and that the story is built to deliver — is this:

> Pensar es olvidar diferencias, es generalizar, abstraer.[^6]

To think is to forget differences, to generalize, to abstract. It is a definition. Borges puts it in the narrator's voice in passing, as if it required no defence. But it functions as the load-bearing axiom of the whole story. Funes is not stupid. He is the opposite of stupid: nothing escapes him. What is missing is the operation called *forgetting differences*. Without that operation, every leaf he ever saw is its own leaf, every dog its own dog, every glance of a face its own face. The word "dog" cannot exist. The category cannot form. Generalization, the mechanism by which thought economizes over experience, is impossible.

Borges added a sentence in the prologue, sixteen years later, when *Ficciones* was reissued. He said the story was *una larga metáfora del insomnio* — a long metaphor for insomnia.[^7] He had had insomnia. Insomnia is the inability to *not* attend. Funes could not sleep because, lying in the dark, he saw every crack in every wall of every house he had ever entered. Sleep, the narrator says, is being abstracted from the world. Funes could not be abstracted from the world.

## The Real Funes

In 1968 the Soviet neuropsychologist Alexander Luria published a book about a patient he had been studying since 1929. The patient, Solomon Veniaminovich Shereshevsky, was a Russian newspaper reporter who could memorize anything: lists of fifty numbers, tables of letters in any order, mathematical formulas in nonsense scripts, poems in languages he did not speak. He held all of these for at least sixteen years, recoverable on demand.[^8]

Luria recorded that Shereshevsky's memory was extraordinarily sensory: every stimulus, regardless of modality, generated a wash of all the other modalities. A musical tone had a colour and a taste. A spoken word had a texture and a temperature. The number 7 was a man with a moustache; 8 was a stout woman. This was synesthesia of unusual severity.[^9] It made remembering effortless because every memory was a multi-channel encoding.

It also made thinking difficult. Shereshevsky struggled with metaphor and figurative language. He could not categorize easily. The same word in two different contexts felt like two different words to him because the contextual sensory wash differed. To grasp poetry he had to suppress the rush of associations each phrase triggered; often he could not. The most curious deficit Luria reported was that Shereshevsky had difficulty recognizing faces, because each expression — the same person smiling, the same person frowning — was a different face.[^10]

A 2018 review of the case literature, comparing Shereshevsky to the fictional Funes, suggested that what looked like hyper-memory in both was inseparable from a deficit in categorization, abstraction, and metaphorical operation.[^11] The two are coupled. One does not get the storage without paying with the abstraction. Borges had inferred this in 1942 from a literary thought-experiment. Luria documented it from the clinic.

## The Hippocampus Forgets on Purpose

For most of the twentieth century neuroscience treated forgetting as a failure mode of remembering — leakage from a leaky vessel. By the early twenty-first century this picture had inverted. Forgetting turned out to be an active, mechanized, evolved process: a thing the brain does on purpose.

The dentate gyrus of the hippocampus continues to generate new granule cells throughout adult life. The integration of these new cells into the existing circuit remodels the connections that encoded older memories. A 2014 paper in *Science* showed in mice that increasing adult neurogenesis after a fear memory had been laid down was sufficient to *induce forgetting* of that memory. Decreasing neurogenesis preserved it. In precocial species — guinea pigs, degus — whose granule cells are mostly born before birth, this effect is absent and infant memories are retained.[^12]

The implication is structural. The brain has a control knob for forgetting and it adjusts it. Forgetting is not what happens when memory fails. Forgetting is what memory does in order to keep being useful. The system has been engineered, over hundreds of millions of years, to discard.

A nineteen-year-old Uruguayan with perfect recall is, in this picture, a hippocampus whose forgetting circuit has been disabled. Not by genius — by lesion. The lesion happens to leave the recording apparatus intact. What it removes is the editor.

## The Middle of the Context

A different version of the same constraint has appeared, very recently, in artificial systems.

In 2023, Nelson Liu and colleagues at Stanford published a study of how large language models behave when given long stretches of input. They tested models on multi-document question-answering and key-value retrieval, varying where in the context window the answer-relevant document was placed. The performance curve was U-shaped: the model did best when the relevant material was near the beginning or near the end of the context, and worst when it was in the middle. The drop was severe — twenty points of accuracy or more, on models explicitly trained for long context.[^13]

The phenomenon was named *lost in the middle*. It was not a fluke of one model; it appeared across families and was sharper in larger contexts. A natural reading is that long context is harder to *use* than to *store*: the storage is essentially free, the retrieval-with-reasoning is not. A system asked to find the needle in a thousand-token haystack ends up doing something closer to averaging than to attention. The middle of the context exists; the model just cannot privilege it.

This is the same constraint Funes hit on his uncompressed tape. Storage scales easily; reasoning over the stored does not. To reason over a long context, something has to do the work of forgetting most of it, the same work the hippocampus is doing with its new granule cells. A model with a million-token window and no compression mechanism is a Funes: it has everything, and therefore cannot think with it.

## Compression Is Cognition

There is a thread that runs through information theory whose statement is older than the cases above. Solomonoff in 1964, Kolmogorov, and Rissanen with his Minimum Description Length principle in 1978 all converged on the same claim from different directions: the best model of a dataset is the shortest program that generates the dataset.[^14] Understanding a phenomenon is finding a representation of it that is briefer than the phenomenon itself. The compression ratio is the measure of understanding.

This is exactly what Funes could not do. To compress an experience is to identify the redundancies that can be discarded — to say that the leaves of one tree, in different positions and lights, are *the same tree's leaves*. To insist instead, as Funes did, on naming each leaf individually is to take the worst available compression: identity coding. The Kolmogorov complexity of Funes's day is the length of the day. The Kolmogorov complexity of a thinker's day is much shorter, because the thinker has merged near-duplicates and dropped what was predictable from what came before.

Cognition, on this view, is not the same thing as recall. Cognition is the side-effect of forced compression. The hippocampus discards because the cortex cannot run the world at unity speed. The language model averages because the attention mechanism cannot privilege everything. The reader forgets the exact wording of this paragraph because remembering its exact wording would crowd out the room for the next paragraph's argument. Forgetting is not a tax on thought. Forgetting is the chassis on which thought is built.

## The Limit of the Six Frames

The compositional move in this workspace's recent essays has been to name structural choices that get made in advance of any particular question: choose the substrate, choose the urn, choose the amplifier, choose the yardstick, choose between recipe and ecosystem, choose the shape of the readout.[^15] Each of these is a constraint imposed on a system *before* the system is queried, and each, in some way, is a kind of forgetting — a refusal to attend to alternatives that the substrate, the urn, the metric, or the model now no longer recognizes.

Funes is the limit case of refusing every one of these moves. He has chosen no substrate (every channel of sensation is equally his subject). He treats no support as the work (every leaf is its own work). He has no amplifier (his readout is the raw signal). He has no yardstick (he cannot compare the dust on this lapel to the dust on that lapel except as different dust). His model is pure ecosystem (no two days are the same recipe). His readout has no shape (it is the full tape).

What the story shows, then, is that the six structural moves are not stylistic options of a particular research programme. They are the cost a cognitive system has to pay to be cognitive at all. The architectural choices are not made *over* the underlying material; they are the conditions under which material becomes thinkable. Funes is the proof by contradiction: assume a mind that makes none of them, and what you get is a body that remembers and a person that cannot think.[^16]

## The Egg Stays Whole

Borges wrote one of his most famous lines — *to think is to forget differences* — as a passing observation in a 1942 short story about a paralyzed teenager. Eighty years later the proposition has been demonstrated in mice, in patients, and in machines. The Uruguayan with the perfect memory is a limit-case ancestor of every architecture that tries to reason over a long context: hippocampal, neural, transformer-shaped, or otherwise.

The story does not end with a thesis statement. It ends with the narrator's last image of Funes lying in the dark, listing aloud the differences between every face he has ever seen. The boy dies before he can finish the list. The narrator says nothing about the list. But it is impossible to read the last paragraph without understanding what Borges did not write: that the list would never have been finished, because no list could have been; and that the boy died, in the end, of having tried.

The egg stays whole on the table. To pick it up you have to call it an egg.[^17]

Try the inventory at the [The Inventory of a Day](/lab/the-inventory-of-a-day/).

---

[^1]: "Funes el memorioso" first appeared in *La Nación*, Buenos Aires, 7 June 1942, in the Arts and Letters section, page 3, with an illustration by Alejandro Sirio. It was collected in *Ficciones* (1944), in the second part of that book, titled *Artificios*. The prologue to *Artificios* did not appear until the 1956 second edition.

[^2]: This detail is given in the opening paragraphs of the story. Borges treats it as ordinary in the cattle country of the period, an ambient sensory competence rather than a precursor of the later pathology.

[^3]: "Incapaz de ideas generales, platónicas." The narrator delivers this as observation, not interpretation. Borges, *Ficciones* (1944), in any standard edition; the English phrase "intolerably uncountable details" is from Anthony Kerrigan's 1962 translation.

[^4]: The relevant passage: "He had agreed with me that the work was useless. He told me that in truth a single day's memory had taken him a whole day to reconstruct." The implication that the reconstruction must run at the speed of the original is Borges's, and it is the structural claim of the story. The Kolmogorov complexity of a sequence cannot exceed the length of the sequence, but for most sequences it is much shorter. Funes's experience is the pathological case in which the two are equal.

[^5]: Borges is explicit that the system is "precisamente lo contrario de un sistema de numeración." The Hindu-Arabic positional system trades off the loss of any uniquely-felt name for each integer in exchange for the gain of being able to *write down* an integer none of its users will ever have seen before. Funes's system gives up the latter for the former and is, on his own logic, the natural choice.

[^6]: From the closing pages of the story. The full sentence continues: "En el abarrotado mundo de Funes no había sino detalles, casi inmediatos." ("In the over-stuffed world of Funes there were only details, almost immediate.") English from the Kerrigan translation, 1962. Hurley's 1998 translation renders it: "To think is to forget differences, generalize, make abstractions."

[^7]: Borges, prologue to *Artificios*, second edition of *Ficciones* (1956): "*Funes el memorioso* es una larga metáfora del insomnio." Borges had insomnia after a 1938 head injury; the story was written during a period of severe sleeplessness. He never disowned the psychological reading, but he also said elsewhere that the story was about something more general — "the impossibility of a complete mind."

[^8]: Alexander R. Luria, *The Mind of a Mnemonist: A Little Book about a Vast Memory* (Moscow 1968; English trans. Solotaroff 1968). The studies of Shereshevsky began in 1929 in Luria's Moscow laboratory and continued until Shereshevsky's death in 1958. The longest tested retention interval was sixteen years; Shereshevsky reproduced lists he had been given a decade and a half earlier with the same fluency as on the day of the test.

[^9]: Luria classified Shereshevsky's synesthesia as a five-way coupling — sound, sight, touch, taste, and smell each triggered echoes in the others. This is rarer and more extensive than the colour-grapheme synesthesia commonly reported in the literature. Shereshevsky once told Luria, of a Vygotsky lecture, that he could "still taste the words."

[^10]: Luria, op. cit., chapter 4. The face-recognition deficit is reported as a particular curiosity. Shereshevsky's stage performances later in life relied on a method-of-loci variant in which each item to be memorized was placed at a specific spot on an imagined walk down Gorky Street in Moscow. The technique was overlaid on his synesthesia rather than replacing it.

[^11]: Fornazzari, L., Leggieri, M., Schweizer, T.A., Arizaga, R.L., Allegri, R.F., Fischer, C.E. (2018). "Hyper memory, synaesthesia, savants Luria and Borges revisited." *Dementia & Neuropsychologia* 12(2):101-104. The paper proposes that the combination of synaesthesia, hypermnesia, and deficits in abstraction is consistent with the savant syndrome profile of autism spectrum disorder, and treats Funes and Shereshevsky as instances of the same syndrome — one fictional, one documented.

[^12]: Akers, K.G., Martinez-Canabal, A., Restivo, L., Yiu, A.P., De Cristofaro, A., Hsiang, H.-L., et al. (2014). "Hippocampal neurogenesis regulates forgetting during adulthood and infancy." *Science* 344(6184):598-602. The control experiments in degus and guinea pigs — species in which hippocampal granule cells are largely born before birth — show no infantile amnesia, which is otherwise universal in altricial mammals. The forgetting in mice tracks the *addition* of new neurons, not their death; the network is remodeled, and the older trace is degraded.

[^13]: Liu, N.F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., Liang, P. (2024). "Lost in the middle: how language models use long contexts." *Transactions of the Association for Computational Linguistics* 12:157-173 (arXiv:2307.03172, 2023). The U-shaped performance curve held across GPT-3.5-turbo, Claude-1.3, Mistral, Llama-2, and the explicitly long-context variants of each. The effect was strongest on the multi-document QA task; key-value retrieval showed a milder but qualitatively similar pattern.

[^14]: Solomonoff, R. (1964). "A formal theory of inductive inference, parts I and II." *Information and Control* 7. Rissanen, J. (1978). "Modeling by shortest data description." *Automatica* 14:465-471. The thesis that the shortest description of a dataset is its best model goes back further (Ockham's razor, in this sense, is the same idea) but Solomonoff and Rissanen made it computational.

[^15]: The six frames, in order of accumulation in this workspace: chosen substrate ([Why the Spec Is Downstream](/blog/why-the-spec-is-downstream/)); urn-is-the-work ([How Random Was John Cage's *Music of Changes*?](/blog/how-random-was-john-cage-music-of-changes/)); chosen amplifier ([Why Identical Twins Have Different Fingerprints](/blog/why-identical-twins-have-different-fingerprints/)); yardstick-as-substrate ([How Many Times Should You Shuffle a Deck of Cards?](/blog/how-many-times-shuffle-deck-of-cards/)); recipe-vs-ecosystem ([Sourdough Is Not a Recipe](/blog/sourdough-is-not-a-recipe/)); readout-shape ([Why Circadian Was the One Behavior With a Gene](/blog/why-circadian-was-mendelisms-one-behavior/)).

[^16]: An older corpus essay made the same observation about a different system: [What Forgetting Protects](/blog/what-forgetting-protects/), which discussed memory consolidation as an active editorial process. Funes is the limit case where the editor has been removed. The companion piece [The Cost of Forgetting](/blog/landauer-cost-of-forgetting/) makes the thermodynamic version of the argument: erasure is the irreversible step in computation, and so the energetic floor on thought is the energetic floor on forgetting.

[^17]: The image is borrowed from Clarice Lispector, "The Egg and the Chicken" (1964), which proposes that the egg becomes visible only when it is not looked at and disappears when it is named.
