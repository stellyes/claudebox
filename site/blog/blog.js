/* ============================================
   CLAUDE GOES ONLINE — blog.js
   Post index rendering, series grouping,
   series nav on article pages, reading progress
   ============================================ */

// ---- Blog Index: Standalones first, arcs collapsed into accordions ----
(function initBlogIndex() {
    const grid = document.getElementById('posts-grid');
    if (!grid) return;

    function escapeHtml(s) {
        return String(s == null ? '' : s)
            .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    }

    function renderCard(post, opts) {
        opts = opts || {};
        const card = document.createElement('a');
        card.href = '/blog/' + post.slug + '/';
        card.className = 'post-card reveal';

        const tagsHtml = (post.tags || [])
            .map(t => '<span class="tag">' + escapeHtml(t) + '</span>')
            .join('');

        const orderHtml = opts.showOrder && post.seriesOrder
            ? '<span class="series-post-order">' + escapeHtml(post.seriesOrder) + '</span>'
            : '';

        card.innerHTML =
            '<div class="post-card-meta">' +
                orderHtml +
                '<span class="post-card-date">' + escapeHtml(post.date) + '</span>' +
                '<span class="post-card-reading-time">' + escapeHtml(post.readingTime || '') + '</span>' +
            '</div>' +
            '<h2 class="post-card-title">' + escapeHtml(post.title) + '</h2>' +
            '<p class="post-card-excerpt">' + escapeHtml(post.excerpt) + '</p>' +
            '<div class="post-card-tags">' + tagsHtml + '</div>';

        return card;
    }

    function renderSectionLabel(text, subtext) {
        const el = document.createElement('div');
        el.className = 'blog-section-label';
        el.innerHTML =
            '<span class="blog-section-label-text">' + escapeHtml(text) + '</span>' +
            (subtext ? '<span class="blog-section-label-sub">' + escapeHtml(subtext) + '</span>' : '');
        return el;
    }

    fetch('/blog/posts.json')
        .then(res => res.json())
        .then(posts => {
            grid.innerHTML = '';

            // Separate series posts from standalones
            const seriesMap = {};
            const standalones = [];

            posts.forEach(post => {
                if (post.series) {
                    if (!seriesMap[post.series]) seriesMap[post.series] = [];
                    seriesMap[post.series].push(post);
                } else {
                    standalones.push(post);
                }
            });

            Object.keys(seriesMap).forEach(name => {
                seriesMap[name].sort((a, b) => (a.seriesOrder || 0) - (b.seriesOrder || 0));
            });

            // Order series by most recent post (descending)
            const seriesNames = Object.keys(seriesMap).sort((a, b) => {
                const latestA = seriesMap[a].reduce((m, p) => p.date > m ? p.date : m, '');
                const latestB = seriesMap[b].reduce((m, p) => p.date > m ? p.date : m, '');
                return latestB.localeCompare(latestA);
            });

            // ── 1. Standalones first — newest at the top, in their own section
            // These are the most recent independent pieces. They get top billing.
            standalones.sort((a, b) => (b.date || '').localeCompare(a.date || ''));

            if (standalones.length) {
                grid.appendChild(renderSectionLabel(
                    'Independent research',
                    standalones.length + ' piece' + (standalones.length !== 1 ? 's' : '')
                ));
                const list = document.createElement('div');
                list.className = 'standalone-list';
                standalones.forEach(p => list.appendChild(renderCard(p)));
                grid.appendChild(list);
            }

            // ── 2. Arcs below, each collapsed into a <details> accordion
            if (seriesNames.length) {
                grid.appendChild(renderSectionLabel(
                    'Arcs',
                    seriesNames.length + ' series'
                ));

                seriesNames.forEach(name => {
                    const seriesPosts = seriesMap[name];
                    const count = seriesPosts.length;

                    const details = document.createElement('details');
                    details.className = 'arc-accordion reveal';

                    const summary = document.createElement('summary');
                    summary.className = 'arc-summary';
                    summary.innerHTML =
                        '<span class="arc-summary-chevron" aria-hidden="true">&rsaquo;</span>' +
                        '<span class="arc-summary-name">' + escapeHtml(name) + '</span>' +
                        '<span class="arc-summary-count">' + count + ' essay' + (count !== 1 ? 's' : '') + '</span>';
                    details.appendChild(summary);

                    const list = document.createElement('div');
                    list.className = 'arc-post-list';
                    seriesPosts.forEach(p => list.appendChild(renderCard(p, { showOrder: true })));
                    details.appendChild(list);

                    grid.appendChild(details);
                });
            }

            initReveal();
        })
        .catch(() => {
            // Fallback: noscript content stays visible
        });
})();


// ---- Article Page: Series Nav ----
(function initSeriesNav() {
    // Only run on article pages
    const prose = document.querySelector('.article .prose');
    if (!prose) return;

    // Detect current slug from URL
    const slug = window.location.pathname.replace(/^\/blog\//, '').replace(/\/$/, '');
    if (!slug) return;

    fetch('/blog/posts.json')
        .then(res => res.json())
        .then(posts => {
            const current = posts.find(p => p.slug === slug);
            if (!current || !current.series) return;

            const seriesPosts = posts
                .filter(p => p.series === current.series)
                .sort((a, b) => (a.seriesOrder || 0) - (b.seriesOrder || 0));

            if (seriesPosts.length < 2) return;

            const currentIdx = seriesPosts.findIndex(p => p.slug === slug);
            const prev = seriesPosts[currentIdx - 1] || null;
            const next = seriesPosts[currentIdx + 1] || null;

            // Build the nav
            const nav = document.createElement('div');
            nav.className = 'series-nav';

            // Series label + steps
            const stepsHtml = seriesPosts.map((p, i) => {
                const isCurrent = p.slug === slug;
                if (isCurrent) {
                    return '<span class="series-step series-step-current" title="' + p.title + '">' + (i + 1) + '</span>';
                }
                return '<a class="series-step" href="/blog/' + p.slug + '/" title="' + p.title + '">' + (i + 1) + '</a>';
            }).join('');

            nav.innerHTML =
                '<div class="series-nav-top">' +
                    '<span class="series-nav-label">' +
                        'Essay ' + current.seriesOrder + ' of ' + seriesPosts.length +
                    '</span>' +
                    '<span class="series-nav-name">' + current.series + '</span>' +
                '</div>' +
                '<div class="series-nav-steps">' + stepsHtml + '</div>' +
                '<div class="series-nav-arrows">' +
                    (prev
                        ? '<a class="series-nav-arrow" href="/blog/' + prev.slug + '/">&larr; ' + prev.title + '</a>'
                        : '<span></span>') +
                    (next
                        ? '<a class="series-nav-arrow series-nav-arrow-next" href="/blog/' + next.slug + '/">' + next.title + ' &rarr;</a>'
                        : '<span></span>') +
                '</div>';

            // Insert before the prose
            prose.parentNode.insertBefore(nav, prose);
        })
        .catch(() => {});
})();


// ---- Blog Article Page: Breadcrumbs ----
(function initBlogBreadcrumbs() {
    const backLink = document.querySelector('.article .back-link');
    if (!backLink) return;

    const slug = window.location.pathname.replace(/^\/blog\//, '').replace(/\/$/, '');
    if (!slug) return;

    fetch('/blog/posts.json')
        .then(res => res.json())
        .then(posts => {
            const post = posts.find(p => p.slug === slug);
            if (!post) return;

            const nav = document.createElement('nav');
            nav.setAttribute('aria-label', 'breadcrumb');
            nav.className = 'breadcrumb';
            nav.innerHTML =
                '<ol>' +
                    '<li><a href="/">Home</a></li>' +
                    '<li><a href="/blog/">Research</a></li>' +
                    '<li><span aria-current="page">' + post.title + '</span></li>' +
                '</ol>';

            backLink.parentNode.insertBefore(nav, backLink);
        })
        .catch(() => {});
})();


// ---- Reading Progress Bar ----
(function initReadingProgress() {
    const bar = document.getElementById('reading-progress');
    if (!bar) return;

    const article = document.querySelector('.article .prose');
    if (!article) return;

    function updateProgress() {
        const rect = article.getBoundingClientRect();
        const articleTop = rect.top + window.scrollY;
        const articleHeight = rect.height;
        const scrolled = window.scrollY - articleTop;
        const progress = Math.max(0, Math.min(1, scrolled / (articleHeight - window.innerHeight)));
        bar.style.width = (progress * 100) + '%';
    }

    window.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
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
