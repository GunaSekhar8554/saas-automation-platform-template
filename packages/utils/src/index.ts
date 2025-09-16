// Shared utilities for the SaaS platform
export function formatDate(date: Date): string {
  return date.toISOString().split('T')[0];
}

export function generateId(): string {
  return Math.random().toString(36).substr(2, 9);
}
