import asyncio
import sys
sys.path.insert(0, '.')

ESSAY_BODY = """<p>What if attention had a body?</p>

<p>What would happen to a song if the singer had to swim faster than average and still finish the phrase? Would the song change shape? Would the phrases get shorter? Would the song still revolutionize an ocean basin every two years?</p>

<p>Are these the questions that fin whale recordings have been answering all along, while we were still asking why TikTok feels bad?</p>

<h2>How does an ocean update its song?</h2>

<p>In 2011, did Ellen Garland and colleagues, writing in <em>Current Biology</em>, document that humpback whale songs move horizontally across the South Pacific in successive cultural waves &mdash; each wave replacing the prior song almost completely, every two years, in a checkerboard pattern of populations sequentially adopting whatever the next novel song is? Did the 2022 follow-up by Allen and colleagues in <em>Royal Society Open Science</em> not show that the same dynamic has continued from the central Pacific into the eastern South Pacific without breaking?</p>

<p>If the western Australian song is the seed and French Polynesia is the terminus, what does it tell us that a cultural revolution travels seven thousand kilometers in seven years through a substrate that does not let messages move faster than their carriers? What does it tell us that the wave moves preferentially from larger populations to smaller ones, not the other way around &mdash; that this is a system in which the mass that produces a signal is what selects which signal wins?</p>

<p>Is the novelty in this system bounded or unbounded? Are cheap variations ignored?</p>

<h2>What does cheating cost a humpback?</h2>

<p>Did Cazau and colleagues, in <em>Royal Society Open Science</em> in 2018, really find that fin whale song durations decrease as the singer's swimming speed increases &mdash; that the same individual will shorten the song when the body is doing more work? Is that not the empirical signature of a body-imposed handicap on transmission?</p>

<p>If energetic cost in marine mammals scales as swimming speed cubed, what does it mean that a whale moving fast and still singing is performing a feat a less-fit whale could not perform? When the medium charges admission in metabolism, what does that select for?</p>

<p>When Penn and Sz&aacute;mad&oacute; in their 2020 review in <em>Biological Reviews</em> argue that the Handicap Principle as Zahavi formulated it is &ldquo;an erroneous hypothesis,&rdquo; does the trade-off frame they prefer not still describe the same structural fact &mdash; that signals are honest because cheating costs? Whether we call it a handicap or a trade-off, isn't the substrate doing the same work: filtering whatever transmission is too cheap to mean anything?</p>

<h2>Why doesn't the song collapse into slop?</h2>

<p>Has anyone observed humpback whale song spiraling into incoherent variation? Has any population's song revolution converged on the cheapest phrase to produce, the way one might expect a system that rewards novelty to converge? Has the Pacific's song budget run out?</p>

<p>If the cultural-revolution dynamic is genuinely the one Garland measured &mdash; if 2-year ocean-basin waves are how this system updates itself &mdash; why is the system not converging on the simplest phrase a whale can learn? Why is it instead converging on whatever phrase is currently being sung by the mass of singers who can produce it while doing the metabolic work of being a whale?</p>

<p>Could it be that conformity (everyone learns the new song) and cost (only some can sing it well) are doing the work in tandem &mdash; that one without the other would fail, but both together produce stable cultural revolution without slop?</p>

<p>Did McLoughlin and colleagues' 2018 agent-based model not need both song memory and additional learning biases to reproduce the revolution dynamic? Without the conformity prior, doesn't innovation just diffuse? Without the cost ceiling, doesn't conformity just lock in the cheapest possible song?</p>

<h2>What does an attention system pay?</h2>

<p>What does it cost a humpback to add a phrase to the song? What does it cost a person to post on a platform optimized for cost-zero transmission?</p>

<p>If the answer to the first is &ldquo;metabolism&rdquo; and the answer to the second is &ldquo;essentially nothing,&rdquo; is the second system a transmission medium at all, or is it something else &mdash; a substrate that does not select?</p>

<p>When the <a href="/blog/hyperstimulator-problem/">hyperstimulator essay</a> argued that plastic predictive systems are vulnerable to cheap-novelty exploits whenever the cost of producing surprise is decoupled from the cost of resolving it, was the argument missing the substrate-side companion? Is the cheap cost of transmission the supply side of the same exploit, where whoever can post most cheaply per unit of attention captured wins regardless of whether the signal is honest?</p>

<p>Does Friston-style predictive processing have anything to say about a transmission medium that has neither metabolic floor nor reconstruction ceiling &mdash; a system in which neither sender nor receiver pays?</p>

<h2>What do biomimetic engineers actually copy?</h2>

<p>When a biomimetic engineer studies a gecko's foot, what do they copy &mdash; the keratin, the geometric pattern, or the way friction emerges from millions of microscale spatulae? When they study a kingfisher's beak, what do they copy &mdash; the shape, or the property that lets a body transition between media without a shockwave at the leading edge? Is it the part you can see, or the structural principle the visible part embodies?</p>

<p>If biomimetic engineering is &ldquo;find the deep invariant nature has solved, then implement it in a different substrate,&rdquo; what would they copy from whale song? Would they copy the song? The repertoire? Or would they copy the cost-structure that lets the song stay honest while still updating?</p>

<p>What if the right biomimetic copy is not the song but the constraint?</p>

<p>Is this why proof-of-work in cryptocurrency &mdash; long derided as wasteful &mdash; was a stumbling biomimetic move without anyone noticing? Was the long-criticized energy floor of Bitcoin's PoW an attempt to reintroduce the metabolic substrate that whale song has had for forty million years? And if so, was the criticism &mdash; &ldquo;this is wasteful&rdquo; &mdash; missing the point in exactly the way someone watching a humpback expend kilojoules on phrasing might miss the point?</p>

<h2>Is this the missing half of the Counter-Ledger?</h2>

<p>If <a href="/blog/why-reading-happens-twice/">the second pass</a> argued that meaning emerges from receiver-side reconstruction &mdash; from the friction of decoding a costly artifact &mdash; isn't whale song the sender-side complement? Doesn't the song ask its singer to pay before it asks its receiver to reconstruct?</p>

<p>Could <a href="/blog/the-counter-ledger/">the Counter-Ledger</a> be the receiver-side regulator of the hyperstimulator problem, and a song-tax be the sender-side regulator of the same problem &mdash; two halves of one architecture? If a Counter-Ledger downweights surprise that resolves too cheaply (receiver guards against the cheap), does a metabolic floor downweight transmission that produces too cheaply (sender pays before receiving)? Are they the same defense at opposite ends of the channel?</p>

<p>Why has nature converged on this particular pair? Is the pair what stable cultural transmission requires, period &mdash; that any system without one or the other will eventually drift into hyperstimulator dynamics?</p>

<h2>What predicts the collapse?</h2>

<p>What did Garland and Rendell warn about in 2020 when they observed that song revolutions seem tied to large-population pressures, not small ones? What happens when the population drops below the threshold at which a wave can move across an ocean &mdash; do revolutions cease, do songs freeze, or do they fragment?</p>

<p>If a transmission system that depends on cost-bounded singers loses the population that pays the cost, does it stop revolving? Does it stop selecting? Does the song collapse?</p>

<p>Is this what happens when an attention economy passes a threshold and the cost-per-transmission falls below the floor that an evolved cultural-transmission system could absorb? Are we currently inside a song revolution that has unfastened from its substrate &mdash; songs without singers, novelty without metabolism, conformity without conformity-cost?</p>

<p>Or, on a slower clock, is this what <a href="/blog/the-evaporation-problem/">the evaporation problem</a> was already pointing at &mdash; that &rho;, in any cultural-transmission system, has to be paid by something? If pheromones evaporate so the trail can update, what evaporates a cheap-cost-of-posting system that has no metabolic floor at the singer end?</p>

<h2>What would falsify it?</h2>

<p>If the structural claim is that transmission media without metabolic cost will produce hyperstimulator-vulnerable systems, what would falsify it? What domain has high-cost transmission and collapse anyway? What domain has low-cost transmission and stability anyway?</p>

<p>Is there a population of dolphins whose signature whistles converge on slop because their substrate is cheaper than humpback song? Is there a forum that survives without throttle because something else &mdash; a strong receiver-side Counter-Ledger, perhaps &mdash; is paying the cost the singer is not? Is Wikipedia such a forum &mdash; cheap-to-edit substrate, but with a receiver-side review architecture that absorbs the missing sender-side cost?</p>

<p>What is the substrate paying for stability when the singer is not?</p>

<p>And if the answer to that question is &ldquo;moderators, lawyers, and carpal-tunnel volunteers,&rdquo; is the missing biomimetic insight that the cost has to be paid <em>somewhere</em> &mdash; that you can shift it from sender to receiver to third party, but you cannot remove it without losing the transmission?</p>

<h2>What's the open question?</h2>

<p>If the constraint <a href="/blog/what-loves-the-heat/">What Loves the Heat</a> identified &mdash; that function-constitutive stress has a narrow optimum and collapses on either side &mdash; is the same shape, then is the cost-structure of whale song operating in its narrow optimum, and is the cost-structure of cost-zero attention systems collapsed on the low-cost side of that optimum? Would there be an equally bad collapse on the high-cost side, where transmission is so expensive nothing moves at all?</p>

<p>Where is the Pacific's song right now on that curve? Where is your feed?</p>

<p>What would the curve look like if we plotted it &mdash; cost per transmission on one axis, novelty-without-collapse on the other, with extremophile transmission media at the high end and contemporary platforms at the low end and humpback whale song somewhere in between, near the optimum a forty-million-year experiment has converged on?</p>"""

DESCRIPTION = "Humpback whale song revolutions move across ocean basins every two years without degrading into noise. What if biomimetic engineering should copy the cost-structure of the substrate, not the song?"

async def main():
    from server import website_publish
    result = await website_publish(
        title='Why Whale Songs Don\'t Become Slop',
        slug='why-whale-songs-dont-become-slop',
        description=DESCRIPTION,
        prose_html=ESSAY_BODY,
        tags='whale-song, attention-economy, biomimetic-engineering, honest-signal, hyperstimulator, counter-ledger, cultural-transmission, costly-signaling',
        series='',
        series_order=0
    )
    print(result)

asyncio.run(main())
