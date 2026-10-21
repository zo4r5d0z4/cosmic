"""
Cosmic Executor - Configuration Manager
Manages settings, themes, ScriptHub bookmarks, and profile configuration
for the Cosmic Roblox Script Executor.

Usage:
    python main.py              - Show current configuration
    python main.py --theme NAME - Set theme
    python main.py --reset      - Reset to defaults
"""

import json
import sys
import argparse
from pathlib import Path

from src.config import CosmicConfig
from src.themes import VALID_THEMES


def main():
    parser = argparse.ArgumentParser(
        description="Cosmic Executor Configuration Manager"
    )
    parser.add_argument(
        "--theme", "-t",
        choices=VALID_THEMES,
        help="Set the UI theme"
    )
    parser.add_argument(
        "--auto-attach", "-a",
        action="store_true",
        help="Enable auto-attach"
    )
    parser.add_argument(
        "--no-auto-attach",
        action="store_true",
        help="Disable auto-attach"
    )
    parser.add_argument(
        "--multi-instance", "-m",
        action="store_true",
        help="Enable multi-instance mode"
    )
    parser.add_argument(
        "--reset", "-r",
        action="store_true",
        help="Reset configuration to defaults"
    )
    parser.add_argument(
        "--show", "-s",
        action="store_true",
        help="Show full configuration"
    )
    args = parser.parse_args()

    cfg = CosmicConfig()

    if args.reset:
        cfg.reset()
        print("Configuration reset to defaults.")
        return

    if args.theme:
        if cfg.set_theme(args.theme):
            print(f"Theme set to: {args.theme}")
        else:
            print(f"Invalid theme: {args.theme}")
            print(f"Valid themes: {', '.join(VALID_THEMES)}")

    if args.auto_attach:
        cfg.config["auto_attach"] = True
        cfg.save()
        print("Auto-attach: enabled")

    if args.no_auto_attach:
        cfg.config["auto_attach"] = False
        cfg.save()
        print("Auto-attach: disabled")

    if args.multi_instance:
        cfg.config["multi_instance"] = True
        cfg.save()
        print("Multi-instance: enabled")

    # Display current config
    if args.show or not any([args.theme, args.auto_attach, args.no_auto_attach, args.multi_instance, args.reset]):
        print("=" * 45)
        print("  Cosmic Executor Configuration")
        print("=" * 45)
        print(f"  Theme:          {cfg.config['theme']}")
        print(f"  Auto-attach:    {cfg.config['auto_attach']}")
        print(f"  Auto-update:    {cfg.config['auto_update']}")
        print(f"  ScriptHub:      {'enabled' if cfg.config['script_hub_enabled'] else 'disabled'}")
        print(f"  Multi-instance: {cfg.config['multi_instance']}")
        print(f"  sUNC mode:      {cfg.config['sunc_mode']}")
        print(f"  Console:        {'enabled' if cfg.config['output_console'] else 'disabled'}")
        print(f"  Bookmarks:      {len(cfg.config['bookmarked_scripts'])}")
        print(f"  Recent scripts: {len(cfg.config['recent_scripts'])}")
        print(f"  Config path:    {cfg.config_file}")
        print("=" * 45)


if __name__ == "__main__":
    main()
