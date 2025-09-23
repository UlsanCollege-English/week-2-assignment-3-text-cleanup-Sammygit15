"""Text Cleanup — Implemented

You are processing a short list of words from a form.
Implement without mutating inputs.
"""
from typing import List


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return first occurrences only (case-sensitive)."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return up to k words ordered by frequency (high to low).

    For ties, earlier first-appearance wins.
    If k <= 0, raise ValueError.
    """
    if k <= 0:
        raise ValueError("k must be positive")

    counts = {}
    first_idx = {}
    for idx, word in enumerate(words):
        counts[word] = counts.get(word, 0) + 1
        if word not in first_idx:
            first_idx[word] = idx

    # Sort by frequency descending, then by first occurrence
    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], first_idx[w]))
    return sorted_words[:k]


def redact_words(words: List[str], banned: List[str]) -> List[str]:
    """Return a new list where every word in `banned` is replaced by "***".

    Exact matches only; case-sensitive.
    """
    banned_set = set(banned)
    return ["***" if w in banned_set else w for w in words]
