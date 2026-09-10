// Shared display formatters so every page renders dates and money the same way.

/**
 * Formats an ISO-ish date string ("2026-08-20") or a Date object as dd/mm/yyyy.
 * Falls back to returning the original value if it can't be parsed.
 */
export const formatDate = (value) => {
  if (!value) return '';
  const date = value instanceof Date ? value : new Date(value);
  if (isNaN(date.getTime())) return String(value);

  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
};

/**
 * Formats a number as an Indian Rupee amount, e.g. 124500 -> "₹1,24,500".
 * Pass { decimals: true } for paise-level precision.
 */
export function formatCurrency(amount, { decimals = false } = {}) {
  const value = Number(amount) || 0;
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    minimumFractionDigits: decimals ? 2 : 0,
    maximumFractionDigits: decimals ? 2 : 0,
  }).format(value);
}
