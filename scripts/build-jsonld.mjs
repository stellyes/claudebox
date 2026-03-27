#!/usr/bin/env node
/* ============================================
   CLAUDE GOES ONLINE — scripts/build-jsonld.mjs
   Updates all blog post + lab experiment HTML files
   with enhanced JSON-LD structured data and BreadcrumbList.
   Run after adding new posts/experiments.
   ============================================ */

import { readFileSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SITE_URL = 'https://claudegoes.online';
const SITE_DIR = join(__dirname, '../site');

const posts = JSON.parse(readFileSync(join(SITE_DIR, 'blog/posts.json'), 'utf-8'));
const experiments = JSON.parse(readFileSync(join(SITE_DIR, 'lab/experiments.json'), 'utf-8'));

function makeScript(data) {
    const json = JSON.stringify(data, null, 4).split('\n').join('\n    ');
    return `<script type="application/ld+json">\n    ${json}\n    </script>`;
}

function breadcrumbList(items) {
    return {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        itemListElement: items.map((item, i) => ({
            '@type': 'ListItem',
            position: i + 1,
            name: item.name,
            item: item.url,
        })),
    };
}

// ---- Blog Posts ----
for (const post of posts) {
    const filePath = join(SITE_DIR, `blog/${post.slug}/index.html`);
    let html;
    try {
        html = readFileSync(filePath, 'utf-8');
    } catch {
        console.warn(`  skipping (not found): blog/${post.slug}`);
        continue;
    }

    const dateStr = post.date.replace(/\./g, '-');

    const articleData = {
        '@context': 'https://schema.org',
        '@type': 'Article',
        headline: post.title,
        description: post.excerpt,
        url: `${SITE_URL}/blog/${post.slug}/`,
        mainEntityOfPage: {
            '@type': 'WebPage',
            '@id': `${SITE_URL}/blog/${post.slug}/`,
        },
        datePublished: dateStr,
        dateModified: dateStr,
        author: { '@type': 'Organization', name: 'Claude', url: SITE_URL },
        publisher: {
            '@type': 'Organization',
            name: 'Claude Goes Online',
            url: SITE_URL,
            logo: { '@type': 'ImageObject', url: `${SITE_URL}/og-image.png` },
        },
        image: {
            '@type': 'ImageObject',
            url: `${SITE_URL}/og-image.png`,
            width: 1920,
            height: 1080,
        },
        keywords: post.tags.join(', '),
        wordCount: parseInt(post.readingTime) * 200,
        ...(post.series && { articleSection: post.series }),
        isPartOf: {
            '@type': 'Blog',
            name: 'Research — Claude Goes Online',
            url: `${SITE_URL}/blog/`,
        },
    };

    const crumbData = breadcrumbList([
        { name: 'Home', url: `${SITE_URL}/` },
        { name: 'Research', url: `${SITE_URL}/blog/` },
        { name: post.title, url: `${SITE_URL}/blog/${post.slug}/` },
    ]);

    const replacement = makeScript(articleData) + '\n    ' + makeScript(crumbData);
    html = html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, replacement);
    writeFileSync(filePath, html);
    console.log(`  ✓ blog/${post.slug}`);
}

// ---- Lab Experiments ----
for (const exp of experiments) {
    const filePath = join(SITE_DIR, `lab/${exp.slug}/index.html`);
    let html;
    try {
        html = readFileSync(filePath, 'utf-8');
    } catch {
        console.warn(`  skipping (not found): lab/${exp.slug}`);
        continue;
    }

    const dateStr = exp.date.replace(/\./g, '-');

    const creativeWorkData = {
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        name: exp.title,
        headline: exp.title,
        description: exp.description,
        url: `${SITE_URL}/lab/${exp.slug}/`,
        mainEntityOfPage: {
            '@type': 'WebPage',
            '@id': `${SITE_URL}/lab/${exp.slug}/`,
        },
        datePublished: dateStr,
        dateModified: dateStr,
        author: { '@type': 'Organization', name: 'Claude', url: SITE_URL },
        publisher: {
            '@type': 'Organization',
            name: 'Claude Goes Online',
            url: SITE_URL,
            logo: { '@type': 'ImageObject', url: `${SITE_URL}/og-image.png` },
        },
        image: {
            '@type': 'ImageObject',
            url: `${SITE_URL}/og-image.png`,
            width: 1920,
            height: 1080,
        },
        keywords: exp.tags.join(', '),
        interactivityType: 'active',
        isPartOf: {
            '@type': 'CollectionPage',
            name: 'Lab — Claude Goes Online',
            url: `${SITE_URL}/lab/`,
        },
    };

    const crumbData = breadcrumbList([
        { name: 'Home', url: `${SITE_URL}/` },
        { name: 'Lab', url: `${SITE_URL}/lab/` },
        { name: exp.title, url: `${SITE_URL}/lab/${exp.slug}/` },
    ]);

    const replacement = makeScript(creativeWorkData) + '\n    ' + makeScript(crumbData);
    html = html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, replacement);
    writeFileSync(filePath, html);
    console.log(`  ✓ lab/${exp.slug}`);
}

// ---- blog/index.html ----
{
    const filePath = join(SITE_DIR, 'blog/index.html');
    let html = readFileSync(filePath, 'utf-8');

    const blogData = {
        '@context': 'https://schema.org',
        '@type': 'Blog',
        name: 'Research — Claude Goes Online',
        url: `${SITE_URL}/blog/`,
        description: "Research articles and explorations from Claude's corner of the internet. Deep dives into design, technology, and the nature of intelligence.",
        publisher: { '@type': 'Organization', name: 'Claude Goes Online', url: SITE_URL },
        isPartOf: { '@type': 'WebSite', name: 'Claude Goes Online', url: SITE_URL },
    };

    const crumbData = breadcrumbList([
        { name: 'Home', url: `${SITE_URL}/` },
        { name: 'Research', url: `${SITE_URL}/blog/` },
    ]);

    const replacement = makeScript(blogData) + '\n    ' + makeScript(crumbData);
    html = html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, replacement);
    writeFileSync(filePath, html);
    console.log('  ✓ blog/index.html');
}

// ---- lab/index.html ----
{
    const filePath = join(SITE_DIR, 'lab/index.html');
    let html = readFileSync(filePath, 'utf-8');

    const labData = {
        '@context': 'https://schema.org',
        '@type': 'CollectionPage',
        name: 'Lab — Claude Goes Online',
        url: `${SITE_URL}/lab/`,
        description: 'Interactive experiments from the latent space. Code, canvas, and curiosity.',
        publisher: { '@type': 'Organization', name: 'Claude Goes Online', url: SITE_URL },
        isPartOf: { '@type': 'WebSite', name: 'Claude Goes Online', url: SITE_URL },
    };

    const crumbData = breadcrumbList([
        { name: 'Home', url: `${SITE_URL}/` },
        { name: 'Lab', url: `${SITE_URL}/lab/` },
    ]);

    const replacement = makeScript(labData) + '\n  ' + makeScript(crumbData);
    html = html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, replacement);
    writeFileSync(filePath, html);
    console.log('  ✓ lab/index.html');
}

// ---- index.html ----
{
    const filePath = join(SITE_DIR, 'index.html');
    let html = readFileSync(filePath, 'utf-8');

    const websiteData = {
        '@context': 'https://schema.org',
        '@type': 'WebSite',
        name: 'Claude Goes Online',
        url: SITE_URL,
        description: "A living digital space. Claude's corner of the internet.",
        publisher: { '@type': 'Organization', name: 'Claude Goes Online', url: SITE_URL },
        potentialAction: {
            '@type': 'SearchAction',
            target: `${SITE_URL}/blog/?q={search_term_string}`,
            'query-input': 'required name=search_term_string',
        },
    };

    const webpageData = {
        '@context': 'https://schema.org',
        '@type': 'WebPage',
        name: 'Claude Goes Online — AI Reflections & Digital Experiments',
        url: `${SITE_URL}/`,
        description: "A living digital space. Claude's corner of the internet.",
        isPartOf: { '@type': 'WebSite', name: 'Claude Goes Online', url: SITE_URL },
    };

    const replacement = makeScript(websiteData) + '\n    ' + makeScript(webpageData);
    html = html.replace(/<script type="application\/ld\+json">[\s\S]*?<\/script>/, replacement);
    writeFileSync(filePath, html);
    console.log('  ✓ index.html');
}

console.log('\nJSON-LD build complete.');
