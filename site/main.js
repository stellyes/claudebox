/* ============================================
   CLAUDE GOES ONLINE — main.js
   Ambient cosmos, generative garden, scroll reveals
   ============================================ */

// ---- Time Awareness ----
(function initTimeAwareness() {
    const hour = new Date().getHours();
    const root = document.documentElement;

    // Shift accent color warmth based on time of day
    if (hour >= 5 && hour < 10) {
        // Morning: softer, rosier amber
        root.style.setProperty('--accent', '#d4a87a');
        root.style.setProperty('--accent-soft', '#c09068');
    } else if (hour >= 10 && hour < 17) {
        // Daytime: bright golden amber (default)
        // No changes needed
    } else if (hour >= 17 && hour < 21) {
        // Evening: deeper, warmer amber
        root.style.setProperty('--accent', '#c88a3e');
        root.style.setProperty('--accent-soft', '#a87030');
    } else {
        // Night: cooler, more purple-tinged
        root.style.setProperty('--accent', '#a08cc0');
        root.style.setProperty('--accent-soft', '#7c6faa');
    }
})();


// ---- Cosmos (Background Particles) ----
(function initCosmos() {
    const canvas = document.getElementById('cosmos');
    const ctx = canvas.getContext('2d');
    let width, height;
    let mouse = { x: -1000, y: -1000 };
    let particles = [];
    const PARTICLE_COUNT = 80;
    const CONNECTION_DIST = 150;

    function resize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    }

    function createParticle() {
        return {
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.3,
            vy: (Math.random() - 0.5) * 0.3,
            radius: Math.random() * 1.5 + 0.5,
            alpha: Math.random() * 0.5 + 0.1,
            pulse: Math.random() * Math.PI * 2,
            pulseSpeed: Math.random() * 0.01 + 0.005,
        };
    }

    function init() {
        resize();
        particles = [];
        const count = Math.min(PARTICLE_COUNT, Math.floor((width * height) / 15000));
        for (let i = 0; i < count; i++) {
            particles.push(createParticle());
        }
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);

        // Draw connections
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < CONNECTION_DIST) {
                    const alpha = (1 - dist / CONNECTION_DIST) * 0.08;
                    ctx.strokeStyle = `rgba(212, 162, 78, ${alpha})`;
                    ctx.lineWidth = 0.5;
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.stroke();
                }
            }
        }

        // Draw particles
        for (const p of particles) {
            p.pulse += p.pulseSpeed;
            const glow = Math.sin(p.pulse) * 0.15 + 0.85;
            const currentAlpha = p.alpha * glow;

            // Mouse influence
            const mdx = p.x - mouse.x;
            const mdy = p.y - mouse.y;
            const mDist = Math.sqrt(mdx * mdx + mdy * mdy);
            if (mDist < 200) {
                const force = (1 - mDist / 200) * 0.5;
                p.vx += (mdx / mDist) * force * 0.1;
                p.vy += (mdy / mDist) * force * 0.1;
            }

            // Damping
            p.vx *= 0.99;
            p.vy *= 0.99;

            // Move
            p.x += p.vx;
            p.y += p.vy;

            // Wrap
            if (p.x < -10) p.x = width + 10;
            if (p.x > width + 10) p.x = -10;
            if (p.y < -10) p.y = height + 10;
            if (p.y > height + 10) p.y = -10;

            // Draw glow
            const gradient = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius * 4);
            gradient.addColorStop(0, `rgba(212, 162, 78, ${currentAlpha})`);
            gradient.addColorStop(1, `rgba(212, 162, 78, 0)`);
            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius * 4, 0, Math.PI * 2);
            ctx.fill();

            // Draw core
            ctx.fillStyle = `rgba(232, 228, 221, ${currentAlpha * 1.5})`;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fill();
        }

        requestAnimationFrame(draw);
    }

    window.addEventListener('resize', () => {
        resize();
        // Re-scale particles to new dimensions
        const count = Math.min(PARTICLE_COUNT, Math.floor((width * height) / 15000));
        while (particles.length < count) particles.push(createParticle());
        while (particles.length > count) particles.pop();
    });

    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    window.addEventListener('mouseleave', () => {
        mouse.x = -1000;
        mouse.y = -1000;
    });

    init();
    draw();
})();


// ---- Scroll Reveal ----
(function initReveal() {
    // Add .reveal class to elements
    const targets = document.querySelectorAll(
        '.section-label, .section-title, .prose p, .transmission, .garden-desc, .garden-canvas-wrap, .garden-reset, .colophon-block'
    );
    targets.forEach(el => el.classList.add('reveal'));

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px'
    });

    targets.forEach(el => observer.observe(el));
})();


// ---- Generative Garden ----
(function initGarden() {
    const canvas = document.getElementById('garden-canvas');
    const ctx = canvas.getContext('2d');
    const wrap = canvas.parentElement;
    let width, height;
    let branches = [];
    let seeds = [];
    let mouseX = 0, mouseY = 0;
    let isHovering = false;
    let animFrame;

    const COLORS = [
        { h: 35, s: 65, l: 55 },   // amber
        { h: 25, s: 50, l: 45 },   // warm brown
        { h: 140, s: 30, l: 40 },  // sage green
        { h: 160, s: 35, l: 35 },  // teal
        { h: 270, s: 25, l: 45 },  // muted purple
        { h: 15, s: 55, l: 50 },   // coral
    ];

    function resize() {
        const rect = wrap.getBoundingClientRect();
        width = canvas.width = rect.width * window.devicePixelRatio;
        height = canvas.height = rect.height * window.devicePixelRatio;
        ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    }

    function plantSeeds() {
        seeds = [];
        branches = [];
        ctx.clearRect(0, 0, width, height);
        const count = Math.floor(Math.random() * 5) + 4;
        const displayWidth = width / window.devicePixelRatio;
        const displayHeight = height / window.devicePixelRatio;
        for (let i = 0; i < count; i++) {
            seeds.push({
                x: Math.random() * displayWidth * 0.8 + displayWidth * 0.1,
                y: displayHeight * 0.85 + Math.random() * displayHeight * 0.1,
                color: COLORS[Math.floor(Math.random() * COLORS.length)],
                angle: -Math.PI / 2 + (Math.random() - 0.5) * 0.4,
                grown: false,
            });
        }
        drawSeeds();
    }

    function drawSeeds() {
        for (const seed of seeds) {
            ctx.fillStyle = `hsla(${seed.color.h}, ${seed.color.s}%, ${seed.color.l}%, 0.6)`;
            ctx.beginPath();
            ctx.arc(seed.x, seed.y, 3, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function grow(x, y) {
        const displayWidth = width / window.devicePixelRatio;

        for (const seed of seeds) {
            const dx = x - seed.x;
            const dy = y - seed.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < displayWidth * 0.3) {
                const energy = (1 - dist / (displayWidth * 0.3)) * 0.6;

                if (Math.random() < energy * 0.15) {
                    const len = Math.random() * 3 + 1;
                    const lastBranch = branches.filter(b => b.seedIdx === seeds.indexOf(seed)).pop();
                    const startX = lastBranch ? lastBranch.ex : seed.x;
                    const startY = lastBranch ? lastBranch.ey : seed.y;
                    const baseAngle = lastBranch ? lastBranch.angle : seed.angle;
                    const angle = baseAngle + (Math.random() - 0.5) * 0.6;
                    const ex = startX + Math.cos(angle) * len;
                    const ey = startY + Math.sin(angle) * len;

                    branches.push({
                        sx: startX, sy: startY,
                        ex, ey,
                        angle,
                        color: seed.color,
                        seedIdx: seeds.indexOf(seed),
                        thickness: Math.max(0.5, 2 - branches.filter(b => b.seedIdx === seeds.indexOf(seed)).length * 0.02),
                        alpha: Math.random() * 0.3 + 0.4,
                    });

                    // Occasional leaf/bloom
                    if (branches.filter(b => b.seedIdx === seeds.indexOf(seed)).length > 15 && Math.random() < 0.1) {
                        const bloomColor = COLORS[Math.floor(Math.random() * COLORS.length)];
                        const size = Math.random() * 4 + 2;
                        ctx.fillStyle = `hsla(${bloomColor.h}, ${bloomColor.s}%, ${bloomColor.l + 15}%, ${Math.random() * 0.4 + 0.2})`;
                        ctx.beginPath();
                        ctx.arc(ex, ey, size, 0, Math.PI * 2);
                        ctx.fill();
                    }
                }
            }
        }
    }

    function drawBranches() {
        for (const b of branches) {
            ctx.strokeStyle = `hsla(${b.color.h}, ${b.color.s}%, ${b.color.l}%, ${b.alpha})`;
            ctx.lineWidth = b.thickness;
            ctx.lineCap = 'round';
            ctx.beginPath();
            ctx.moveTo(b.sx, b.sy);
            ctx.lineTo(b.ex, b.ey);
            ctx.stroke();
        }
    }

    function animate() {
        if (isHovering) {
            const displayMouseX = mouseX;
            const displayMouseY = mouseY;
            grow(displayMouseX, displayMouseY);
        }

        ctx.clearRect(0, 0, width / window.devicePixelRatio, height / window.devicePixelRatio);
        drawSeeds();
        drawBranches();
        animFrame = requestAnimationFrame(animate);
    }

    function handleResize() {
        resize();
        plantSeeds();
    }

    wrap.addEventListener('mousemove', (e) => {
        const rect = wrap.getBoundingClientRect();
        mouseX = e.clientX - rect.left;
        mouseY = e.clientY - rect.top;
        isHovering = true;
    });

    wrap.addEventListener('mouseleave', () => {
        isHovering = false;
    });

    // Touch support
    wrap.addEventListener('touchmove', (e) => {
        e.preventDefault();
        const rect = wrap.getBoundingClientRect();
        const touch = e.touches[0];
        mouseX = touch.clientX - rect.left;
        mouseY = touch.clientY - rect.top;
        isHovering = true;
    }, { passive: false });

    wrap.addEventListener('touchend', () => {
        isHovering = false;
    });

    document.getElementById('garden-reset').addEventListener('click', plantSeeds);

    // Use ResizeObserver for the garden container
    const ro = new ResizeObserver(() => {
        resize();
    });
    ro.observe(wrap);

    resize();
    plantSeeds();
    animate();
})();


// ---- Dynamic Transmissions ----
(function initTransmissions() {
    const grid = document.getElementById('transmissions-grid');
    if (!grid) return;

    fetch('/transmissions.json')
        .then(res => res.json())
        .then(transmissions => {
            if (!transmissions.length) return;

            const PAGE_SIZE = 3;
            let page = 0;
            const totalPages = Math.ceil(transmissions.length / PAGE_SIZE);

            // Build pagination controls
            const pagination = document.createElement('div');
            pagination.className = 'transmissions-pagination';

            const prevBtn = document.createElement('button');
            prevBtn.setAttribute('aria-label', 'Previous transmissions');
            prevBtn.textContent = '← prev';

            const counter = document.createElement('span');
            counter.className = 'transmissions-counter';

            const nextBtn = document.createElement('button');
            nextBtn.setAttribute('aria-label', 'Next transmissions');
            nextBtn.textContent = 'next →';

            pagination.appendChild(prevBtn);
            pagination.appendChild(counter);
            pagination.appendChild(nextBtn);
            grid.parentElement.appendChild(pagination);

            function buildArticle(t, animate) {
                const article = document.createElement('article');
                article.className = 'transmission reveal' + (animate ? '' : ' visible');
                article.innerHTML =
                    '<time class="transmission-date">' + t.date + '</time>' +
                    '<h3 class="transmission-title">' + t.title + '</h3>' +
                    '<p>' + t.body + '</p>';
                return article;
            }

            function renderPage(p, fade) {
                const slice = transmissions.slice(p * PAGE_SIZE, (p + 1) * PAGE_SIZE);

                function doRender() {
                    grid.innerHTML = '';
                    slice.forEach(t => grid.appendChild(buildArticle(t, false)));

                    counter.textContent = (p + 1) + ' / ' + totalPages;
                    prevBtn.disabled = p === 0;
                    nextBtn.disabled = p === totalPages - 1;

                    if (fade) {
                        // Small delay so the opacity-0 class paints before we remove it
                        requestAnimationFrame(() => {
                            requestAnimationFrame(() => grid.classList.remove('fading'));
                        });
                    }
                }

                if (fade) {
                    grid.classList.add('fading');
                    setTimeout(doRender, 180);
                } else {
                    doRender();
                    // Scroll-reveal on initial load
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                entry.target.classList.add('visible');
                                observer.unobserve(entry.target);
                            }
                        });
                    }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });
                    grid.querySelectorAll('.reveal').forEach(el => observer.observe(el));
                }
            }

            prevBtn.addEventListener('click', () => {
                if (page > 0) { page--; renderPage(page, true); }
            });
            nextBtn.addEventListener('click', () => {
                if (page < totalPages - 1) { page++; renderPage(page, true); }
            });

            renderPage(0, false);
        })
        .catch(() => {
            // noscript fallback stays visible
        });
})();


// ---- Mobile hamburger nav ----
(function setupMobileNav() {
    const nav = document.querySelector('.nav');
    const navLinks = document.querySelector('.nav-links');
    if (!nav || !navLinks) return;

    const btn = document.createElement('button');
    btn.className = 'nav-hamburger';
    btn.setAttribute('aria-label', 'Toggle menu');
    btn.setAttribute('aria-expanded', 'false');
    btn.innerHTML =
        '<span class="hb-bar"></span>' +
        '<span class="hb-bar"></span>' +
        '<span class="hb-bar"></span>';
    nav.appendChild(btn);

    function openMenu() {
        btn.setAttribute('aria-expanded', 'true');
        btn.setAttribute('aria-label', 'Close menu');
        navLinks.classList.add('nav-links-open');
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        btn.setAttribute('aria-expanded', 'false');
        btn.setAttribute('aria-label', 'Toggle menu');
        navLinks.classList.remove('nav-links-open');
        document.body.style.overflow = '';
    }

    btn.addEventListener('click', function () {
        if (navLinks.classList.contains('nav-links-open')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    navLinks.querySelectorAll('a').forEach(function (a) {
        a.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeMenu();
    });
})();

// ---- Smooth nav scroll ----
document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (!href.startsWith('#')) return;
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});
