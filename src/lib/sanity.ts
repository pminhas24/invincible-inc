import { createClient } from '@sanity/client';

export const sanity = createClient({
  projectId: import.meta.env.PUBLIC_SANITY_PROJECT_ID,
  dataset: import.meta.env.PUBLIC_SANITY_DATASET,
  apiVersion: import.meta.env.PUBLIC_SANITY_API_VERSION,
  useCdn: false, // fetch fresh published content at build time (webhook-triggered builds must not get stale CDN data); drafts still require a token (not used in Phase 1)
});
