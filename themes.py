"""
Theme definitions and loader for Cosmic Executor.
Supports 12 built-in themes and custom theme import
via .cosmic-theme.json files.
"""

import json
from pathlib import Path


VALID_THEMES = [
    "amethyst",
    "crimson",
    "ember",
    "gold",
    "forest",
    "mint",
    "ocean",
    "azure",
    "indigo",
    "slate",
    "graphite",
    "light",
]


# Built-in theme color definitions
BUILTIN_THEMES = {
    "amethyst": {
        "primary": "#8b5cf6",
        "secondary": "#a78bfa",
        "background": "#0f0a1a",
        "surface": "#1a1025",
        "accent": "#c4b5fd",
        "text": "#e2e0eb",
        "text_muted": "#8a8690",
    },
    "crimson": {
        "primary": "#dc2626",
        "secondary": "#ef4444",
        "background": "#1a0a0a",
        "surface": "#251010",
        "accent": "#fca5a5",
        "text": "#f5e0e0",
        "text_muted": "#a08686",
    },
    "ember": {
        "primary": "#ea580c",
        "secondary": "#f97316",
        "background": "#1a1005",
        "surface": "#251a08",
        "accent": "#fdba74",
        "text": "#f5e8d0",
        "text_muted": "#a09680",
    },
    "gold": {
        "primary": "#ca8a04",
        "secondary": "#eab308",
        "background": "#1a1505",
        "surface": "#25200a",
        "accent": "#fde047",
        "text": "#f5f0d0",
        "text_muted": "#a0a080",
    },
    "forest": {
        "primary": "#16a34a",
        "secondary": "#22c55e",
        "background": "#051a0a",
        "surface": "#0a2510",
        "accent": "#86efac",
        "text": "#d0f5e0",
        "text_muted": "#80a090",
    },
    "mint": {
        "primary": "#06d6a0",
        "secondary": "#34d399",
        "background": "#051a15",
        "surface": "#0a2520",
        "accent": "#6ee7b7",
        "text": "#d0f5ed",
        "text_muted": "#80a098",
    },
    "ocean": {
        "primary": "#0284c7",
        "secondary": "#0ea5e9",
        "background": "#05101a",
        "surface": "#0a1825",
        "accent": "#7dd3fc",
        "text": "#d0e8f5",
        "text_muted": "#8098a0",
    },
    "azure": {
        "primary": "#2563eb",
        "secondary": "#3b82f6",
        "background": "#050f1a",
        "surface": "#0a1825",
        "accent": "#93c5fd",
        "text": "#d0e2f5",
        "text_muted": "#8090a0",
    },
    "indigo": {
        "primary": "#4f46e5",
        "secondary": "#6366f1",
        "background": "#0a051a",
        "surface": "#150a25",
        "accent": "#a5b4fc",
        "text": "#e0daf5",
        "text_muted": "#8680a0",
    },
    "slate": {
        "primary": "#475569",
        "secondary": "#64748b",
        "background": "#0a0f15",
        "surface": "#121820",
        "accent": "#94a3b8",
        "text": "#e2e8f0",
        "text_muted": "#8090a0",
    },
    "graphite": {
        "primary": "#374151",
        "secondary": "#4b5563",
        "background": "#0a0e14",
        "surface": "#111827",
        "accent": "#9ca3af",
        "text": "#e5e7eb",
        "text_muted": "#808890",
    },
    "light": {
        "primary": "#3b82f6",
        "secondary": "#2563eb",
        "background": "#f8fafc",
        "surface": "#f1f5f9",
        "accent": "#60a5fa",
        "text": "#1e293b",
        "text_muted": "#64748b",
    },
}


class ThemeManager:
    """Manages built-in and custom themes."""

    def __init__(self, themes_dir=None):
        self.themes_dir = themes_dir or (Path.home() / ".cosmic" / "themes")
        self.themes_dir.mkdir(parents=True, exist_ok=True)
        self.custom_themes = self._load_custom_themes()

    def _load_custom_themes(self):
        """Load custom themes from .cosmic-theme.json files."""
        custom = {}
        for theme_file in self.themes_dir.glob("*.cosmic-theme.json"):
            try:
                with open(theme_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                name = data.get("name", theme_file.stem)
                custom[name] = data
            except (json.JSONDecodeError, IOError):
                continue
        return custom

    def get_theme(self, name):
        """Get a theme by name. Returns None if not found."""
        if name in BUILTIN_THEMES:
            return BUILTIN_THEMES[name]
        return self.custom_themes.get(name)

    def list_themes(self):
        """List all available theme names."""
        return VALID_THEMES + list(self.custom_themes.keys())

    def import_theme(self, file_path):
        """Import a custom theme from a JSON file."""
        file_path = Path(file_path)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            name = data.get("name", file_path.stem)
            dest = self.themes_dir / f"{name}.cosmic-theme.json"
            with open(dest, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            self.custom_themes[name] = data
            return name
        except (json.JSONDecodeError, IOError) as e:
            return None
