type Span = { _type: string; text?: string };
type Block = { _type: string; children?: Span[] };

const WORDS_PER_MINUTE = 200;

export function readingTimeMinutes(body: Block[]): number {
  const words = (body ?? [])
    .filter((b) => b._type === 'block')
    .flatMap((b) => b.children ?? [])
    .map((c) => c.text ?? '')
    .join(' ')
    .split(/\s+/)
    .filter(Boolean).length;
  return Math.max(1, Math.ceil(words / WORDS_PER_MINUTE));
}
