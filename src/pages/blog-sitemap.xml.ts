import type { APIRoute } from 'astro';
import { sanity } from '../lib/sanity';

const SITE = 'https://invinciblesecuritygroup.com';

export const GET: APIRoute = async () => {
  const posts: { slug: string; _updatedAt: string }[] = await sanity.fetch(
    `*[_type == "post" && defined(slug.current)]{ "slug": slug.current, _updatedAt }`
  );
  const urls = [
    `<url><loc>${SITE}/blog</loc></url>`,
    ...posts.map(
      (p) => `<url><loc>${SITE}/blog/${p.slug}</loc><lastmod>${new Date(p._updatedAt).toISOString()}</lastmod></url>`
    ),
  ].join('');
  const xml = `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml' } });
};
