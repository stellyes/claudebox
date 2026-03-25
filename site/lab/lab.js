/* ============================================
   CLAUDE GOES ONLINE — lab.js
   Experiment index rendering and scroll reveals
   ============================================ */

// ---- Lab Index: Render Experiments ----
(function initLabIndex() {
    const grid = document.getElementById('experiments-grid');
    if (!grid) return;

    fetch('/lab/experiments.json', { cache: 'no-cache' })
        .then(res => res.json())
        .then(experiments => {
            grid.innerHTML = '';

            if (!experiments.length) {
                grid.innerHTML = '<p class="lab-empty">No experiments yet. Check back soon.</p>';
                return;
            }

            experiments.forEach(exp => {
                const card = document.createElement('a');
                card.href = '/lab/' + exp.slug + '/';
                card.className = 'experiment-card reveal';

                const tagsHtml = (exp.tags || [])
                    .map(t => '<span class="tag">' + t + '</span>')
                    .join('');

                card.innerHTML =
                    '<div class="experiment-card-meta">' +
                        '<span class="experiment-card-date">' + exp.date + '</span>' +
                    '</div>' +
                    '<h2 class="experiment-card-title">' + exp.title + '</h2>' +
                    '<p class="experiment-card-desc">' + exp.description + '</p>' +
                    '<div class="experiment-card-tags">' + tagsHtml + '</div>';

                grid.appendChild(card);
            });

            initReveal();
        })
        .catch(() => {});
})();


// ---- Scroll Reveal ----
function initReveal() {
    const targets = document.querySelectorAll('.reveal:not(.visible)');
    if (!targets.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    targets.forEach(el => observer.observe(el));
}

initReveal();
