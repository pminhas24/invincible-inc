export const postsListQuery = `
*[_type == "post" && defined(slug.current)] | order(coalesce(featured, false) desc, publishedAt desc){
  title,
  "slug": slug.current,
  excerpt,
  publishedAt,
  featured,
  featuredImage,
  "category": category->{title, "slug": slug.current}
}`;

export const postSlugsQuery = `*[_type == "post" && defined(slug.current)].slug.current`;

export const postBySlugQuery = `
*[_type == "post" && slug.current == $slug][0]{
  title,
  "slug": slug.current,
  excerpt,
  body,
  publishedAt,
  _updatedAt,
  featuredImage,
  ogImage,
  seoTitle,
  seoDescription,
  "category": category->{title, "slug": slug.current},
  "author": author->{name, role, photo, bio}
}`;
