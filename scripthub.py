"""
ScriptHub API client for Cosmic Executor.
Searches and retrieves scripts from ScriptBlox, RScripts, and RobloxScripts.
"""

import json
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError


SCRIPTHUB_SOURCES = {
    "scriptblox": {
        "name": "ScriptBlox",
        "search_url": "https://scriptblox.com/api/script/search?q={query}",
        "base_url": "https://scriptblox.com",
    },
    "rscripts": {
        "name": "RScripts",
        "search_url": "https://rscripts.net/api/search?q={query}",
        "base_url": "https://rscripts.net",
    },
    "robloxscripts": {
        "name": "RobloxScripts",
        "search_url": "https://robloxscripts.com/api/search?q={query}",
        "base_url": "https://robloxscripts.com",
    },
}


class ScriptHubClient:
    """Client for searching and retrieving scripts from ScriptHub sources."""

    def __init__(self, cache_dir=None):
        self.cache_dir = cache_dir or (Path.home() / ".cosmic" / "cache")
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def search(self, query, source="scriptblox"):
        """Search for scripts across ScriptHub sources.

        Args:
            query: Search query string
            source: Source to search (scriptblox, rscripts, robloxscripts, or all)

        Returns:
            List of script results with name, url, source, and game info
        """
        if source == "all":
            results = []
            for src_key in SCRIPTHUB_SOURCES:
                results.extend(self._search_source(query, src_key))
            return results
        return self._search_source(query, source)

    def _search_source(self, query, source_key):
        """Search a single ScriptHub source."""
        if source_key not in SCRIPTHUB_SOURCES:
            return []

        source = SCRIPTHUB_SOURCES[source_key]
        url = source["search_url"].format(query=query.replace(" ", "+"))

        try:
            req = Request(url, headers={"User-Agent": "CosmicExecutor/1.0"})
            with urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            return self._parse_results(data, source_key)
        except (URLError, json.JSONDecodeError, TimeoutError):
            return []

    def _parse_results(self, data, source_key):
        """Parse API response into standardized result format."""
        results = []
        scripts = data.get("result", {}).get("scripts", [])
        if isinstance(data, list):
            scripts = data

        for script in scripts:
            results.append({
                "name": script.get("title", script.get("name", "Unknown")),
                "url": script.get("script", script.get("rawUrl", "")),
                "source": source_key,
                "game": script.get("game", script.get("gameName", "")),
                "verified": script.get("verified", False),
            })
        return results

    def get_cached_scripts(self, game_name=None):
        """Get locally cached scripts, optionally filtered by game."""
        cache_file = self.cache_dir / "scripts_cache.json"
        if not cache_file.exists():
            return []

        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cached = json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

        if game_name:
            return [s for s in cached if s.get("game", "").lower() == game_name.lower()]
        return cached

    def save_to_cache(self, scripts):
        """Save scripts to local cache."""
        cache_file = self.cache_dir / "scripts_cache.json"
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(scripts, f, indent=2)

    def list_sources(self):
        """List all available ScriptHub sources."""
        return [
            {"key": key, "name": src["name"]}
            for key, src in SCRIPTHUB_SOURCES.items()
        ]
