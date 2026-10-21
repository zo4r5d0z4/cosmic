"""
Configuration handler for Cosmic Executor.
Stores and manages user preferences, theme selection,
ScriptHub bookmarks, and runtime settings.
"""

import json
from pathlib import Path


DEFAULT_CONFIG = {
    "theme": "amethyst",
    "auto_attach": True,
    "auto_update": True,
    "script_hub_enabled": True,
    "multi_instance": False,
    "sunc_mode": "full",
    "output_console": True,
    "recent_scripts": [],
    "bookmarked_scripts": [],
}


class CosmicConfig:
    """Configuration manager for Cosmic Executor."""

    def __init__(self):
        self.config_dir = Path.home() / ".cosmic"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(exist_ok=True)
        self.config = self._load_config()

    def _load_config(self):
        """Load configuration from disk, falling back to defaults."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    saved = json.load(f)
                config = DEFAULT_CONFIG.copy()
                config.update(saved)
                return config
            except (json.JSONDecodeError, IOError):
                return DEFAULT_CONFIG.copy()
        return DEFAULT_CONFIG.copy()

    def save(self):
        """Save current configuration to disk."""
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def reset(self):
        """Reset configuration to defaults."""
        self.config = DEFAULT_CONFIG.copy()
        self.save()

    def set_theme(self, theme_name):
        """Set the UI theme. Returns True if valid, False otherwise."""
        from src.themes import VALID_THEMES
        if theme_name in VALID_THEMES:
            self.config["theme"] = theme_name
            self.save()
            return True
        return False

    def bookmark_script(self, script_name, script_url, category="general"):
        """Add a script to bookmarks."""
        entry = {
            "name": script_name,
            "url": script_url,
            "category": category,
        }
        self.config["bookmarked_scripts"].append(entry)
        self.save()

    def remove_bookmark(self, script_name):
        """Remove a script from bookmarks by name."""
        self.config["bookmarked_scripts"] = [
            b for b in self.config["bookmarked_scripts"]
            if b.get("name") != script_name
        ]
        self.save()

    def add_recent_script(self, script_path):
        """Add a script to recent history (max 50 entries)."""
        recent = self.config["recent_scripts"]
        if script_path in recent:
            recent.remove(script_path)
        recent.append(script_path)
        if len(recent) > 50:
            recent = recent[-50:]
        self.config["recent_scripts"] = recent
        self.save()

    def get_recent_scripts(self, limit=10):
        """Get the most recent scripts."""
        return self.config["recent_scripts"][-limit:]

    def get_bookmarks_by_category(self, category):
        """Get all bookmarks in a specific category."""
        return [
            b for b in self.config["bookmarked_scripts"]
            if b.get("category") == category
        ]
