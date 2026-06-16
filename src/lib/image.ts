import { createImageUrlBuilder } from '@sanity/image-url';
import type { SanityImageSource } from '@sanity/image-url/lib/types/types';
import { sanity } from './sanity';

const builder = createImageUrlBuilder(sanity);
export const urlFor = (source: SanityImageSource) => builder.image(source);
