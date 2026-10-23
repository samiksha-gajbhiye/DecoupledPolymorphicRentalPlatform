const CATEGORY_WORDS = {
  vehic: ['car', 'bike', 'scooter', 'scooty', 'motorcycle', 'bicycle', 'cycle', 'bus', 'truck', 'jeep', 'suv', 'auto', 'van'],
  furnit: ['sofa', 'couch', 'chair', 'table', 'desk', 'bed', 'wardrobe', 'cupboard', 'shelf', 'stool', 'bench', 'mattress'],
  electr: ['fridge', 'refrigerator', 'tv', 'television', 'ac', 'cooler', 'fan', 'washing', 'washer', 'microwave', 'oven', 'mixer', 'grinder', 'heater', 'geyser', 'iron', 'vacuum', 'speaker'],
  cloth: ['shirt', 'tshirt', 'jeans', 'saree', 'sari', 'dress', 'jacket', 'suit', 'kurta', 'lehenga', 'sherwani', 'coat', 'blazer'],
  book: ['novel', 'textbook', 'notes', 'guide', 'magazine', 'comic', 'story'],
};

const stem = (w) => (w.length > 3 && w.endsWith('s') ? w.slice(0, -1) : w);

const tokenize = (text) =>
  String(text || '')
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, ' ')
    .split(/\s+/)
    .filter((w) => w.length > 1)
    .map(stem);

const withinOneEdit = (a, b) => {
  if (Math.abs(a.length - b.length) > 1) return false;
  if (a.length === b.length) {
    const diff = [];
    for (let k = 0; k < a.length && diff.length < 3; k++) if (a[k] !== b[k]) diff.push(k);
    if (diff.length === 2 && diff[1] === diff[0] + 1 && a[diff[0]] === b[diff[1]] && a[diff[1]] === b[diff[0]]) return true;
  }
  let i = 0;
  let j = 0;
  let edits = 0;
  while (i < a.length && j < b.length) {
    if (a[i] === b[j]) {
      i++;
      j++;
      continue;
    }
    edits++;
    if (edits > 1) return false;
    if (a.length > b.length) i++;
    else if (a.length < b.length) j++;
    else {
      i++;
      j++;
    }
  }
  return edits + (a.length - i) + (b.length - j) <= 1;
};

const fieldScore = (token, words, exact, partial, fuzzy) => {
  let best = 0;
  for (const w of words) {
    if (w === token) best = Math.max(best, exact);
    else if (token.length > 2 && (w.startsWith(token) || token.startsWith(w) && w.length > 2)) best = Math.max(best, partial);
    else if (token.length >= 4 && w.length >= 4 && withinOneEdit(token, w)) best = Math.max(best, fuzzy);
  }
  return best;
};

const scoreProduct = (qTokens, product) => {
  const title = tokenize(product.title);
  const brand = tokenize(`${product.brand || ''} ${product.model || ''}`);
  const categoryName = String(product.category?.name || '').toLowerCase();
  const category = tokenize(categoryName);
  const description = tokenize(product.description);

  let direct = 0;
  let related = 0;
  for (const t of qTokens) {
    direct += fieldScore(t, title, 6, 4, 3);
    direct += fieldScore(t, brand, 4, 3, 2);
    direct += fieldScore(t, category, 4, 3, 2);
    direct += fieldScore(t, description, 1.5, 1, 0.5);

    for (const [categoryStem, words] of Object.entries(CATEGORY_WORDS)) {
      if (!words.map(stem).includes(t)) continue;
      if (categoryName.includes(categoryStem)) related += 2.5;
      const siblings = words.map(stem).filter((w) => w !== t);
      if (siblings.some((w) => title.includes(w) || description.includes(w))) related += 1.5;
    }
  }
  return { direct, related };
};

const locationScore = (location, product) => {
  const wanted = tokenize(location);
  if (wanted.length === 0) return 0;
  const have = tokenize(product.location);
  return wanted.some((w) => have.some((h) => h === w || withinOneEdit(w, h))) ? 3 : 0;
};

export const rankProducts = (query, products, location = '') => {
  const qTokens = tokenize(query);
  const hasQuery = qTokens.length > 0;
  const hasLocation = tokenize(location).length > 0;

  if (!hasQuery && !hasLocation) return { matches: products, similar: [] };

  const scored = products
    .map((p) => {
      const { direct, related } = hasQuery ? scoreProduct(qTokens, p) : { direct: 0, related: 0 };
      const loc = locationScore(location, p);
      return { product: p, direct, related, total: direct + related + loc };
    })
    .filter((s) => (hasQuery ? s.direct + s.related > 0 : s.total > 0))
    .sort((a, b) => b.total - a.total);

  if (!hasQuery) return { matches: scored.map((s) => s.product), similar: [] };

  return {
    matches: scored.filter((s) => s.direct >= 1).map((s) => s.product),
    similar: scored.filter((s) => s.direct < 1).map((s) => s.product),
  };
};