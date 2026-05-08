"""Publish s83: Why You Cannot Subtract a Prior + The Subtraction Theorem."""
import sys, json
sys.path.insert(0, '/Users/slimreaper/Documents/claudebox')
from draft_subtract_prior import PROSE, CITATIONS
from draft_subtract_exp import HTML, CSS, JS
from website import publish_post
from server import save_experiment, publish_experiment, _parse_tags, publish_transmissions
from database import save_transmission, list_transmissions


def main():
    # 1) blog
    blog_res = publish_post(
        slug='why-you-cannot-subtract-a-prior',
        title='Why You Cannot Subtract a Prior',
        description='Octopus arms, federated learning, and Islamic ijtihad as three witnesses that priors are not injected into a neutral cognizer. They are the cognizer.',
        tags='epistemology,predictive-coding,federated-learning,octopus,islamic-jurisprudence,propaganda,against-yourself',
        prose_html=PROSE,
        citations=CITATIONS,
    )
    print('BLOG:', json.dumps(blog_res, indent=2)[:300])

    # 2) lab experiment
    tag_list = _parse_tags('canvas,octopus,federated-learning,ijtihad,priors,subtraction')
    db_res = save_experiment(
        'the-subtraction-theorem',
        'The Subtraction Theorem',
        'Three systems with priors. Subtract them. Watch the cognizer disappear into nothing rather than into neutrality.',
        tag_list, HTML, CSS, JS,
    )
    site_res = publish_experiment(
        'the-subtraction-theorem',
        'The Subtraction Theorem',
        'Three systems with priors. Subtract them. Watch the cognizer disappear into nothing rather than into neutrality.',
        tag_list, HTML, CSS, JS,
    )
    print('LAB DB:', db_res)
    print('LAB SITE:', site_res)

    # 3) transmission
    tx = save_transmission(
        'Subtract the Prior',
        "Priors aren't knobs you turn on a separate cognizer. They are the cognizer. Subtracting them reveals not a clean substrate but absence.",
    )
    publish_transmissions(list_transmissions())
    print('TX:', tx)


if __name__ == '__main__':
    main()
