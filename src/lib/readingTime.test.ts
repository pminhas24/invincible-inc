import { describe, it, expect } from 'vitest';
import { readingTimeMinutes } from './readingTime';

const block = (text: string) => ({
  _type: 'block',
  children: [{ _type: 'span', text }],
});

describe('readingTimeMinutes', () => {
  it('returns at least 1 minute for short content', () => {
    expect(readingTimeMinutes([block('hello world')])).toBe(1);
  });

  it('counts ~200 words per minute, rounding up', () => {
    const words = Array(450).fill('word').join(' ');
    expect(readingTimeMinutes([block(words)])).toBe(3);
  });

  it('ignores non-block content (e.g. images)', () => {
    expect(readingTimeMinutes([{ _type: 'image' }, block('one two three')])).toBe(1);
  });
});
