# Cosmic Executor - Free Roblox Script Executor (2026)

**100% sUNC | Keyless | Decompiler | 1,200+ ScriptHub**

Cosmic Executor is a free, keyless Roblox script executor with the highest script compatibility of any free executor. A verified 100% sUNC score means every UNC environment function is properly implemented and actually works. No script incompatibility errors, no missing function crashes, no spoofed scores.

## Features

- **100% sUNC / Full UNC** - Highest possible script compatibility
- **Keyless & Free** - No key system, no daily verification, no linkvertise chains
- **Built-in Decompiler** - Decompile any game's client-side scripts directly
- **1,200+ ScriptHub Library** - Cloud-hosted scripts searchable from inside the UI
- **Multi-Instance Support** - Run alongside multiple Roblox clients simultaneously
- **12 Built-in Themes + Custom Import** - Full UI customization with `.cosmic-theme.json` files
- **SaveInstance Support** - Save and dump entire game instances for offline analysis
- **Auto-Update System** - Download once, updates automatically
- **Modern Customizable UI** - Tabbed scripting, organized ScriptHub, clean output console

## Quick Start

1. Download the latest release from the docs folder
2. Extract to a folder on your desktop
3. Add the folder to Windows Defender exclusions
4. Open Roblox and fully load into any game
5. Launch Cosmic Executor and click Attach
6. Paste a script into the editor or search ScriptHub
7. Click Execute to run

## System Requirements

- Windows 10 or 11 (64-bit)
- Roblox (latest version from Microsoft Store or website)
- Internet connection (required for auto-updates and ScriptHub)

## Project Structure

```
cosmic-executor-2026/
├── main.py              - Configuration manager entry point
├── src/
│   ├── config.py        - Configuration handler
│   ├── themes.py        - Theme definitions and loader
│   └── scripthub.py     - ScriptHub API client
├── themes/              - Theme JSON files
├── docs/                - Documentation and guides
├── scripts/             - Example scripts
└── LICENSE              - MIT License
```

## Configuration

Cosmic stores configuration in `~/.cosmic/config.json`. Use the config manager to view and modify settings:

```bash
python main.py
```

### Available Themes

Amethyst, Crimson, Ember, Gold, Forest, Mint, Ocean, Azure, Indigo, Slate, Graphite, Light

### ScriptHub

ScriptHub searches three major script libraries:
- ScriptBlox.com
- RScripts.net
- RobloxScripts.com

## Safety Notice

- Always use alt accounts when executing scripts
- Download only from the official source linked in the documentation
- Never run scripts from untrusted sources
- Whitelist the Cosmic folder in your antivirus
- No executor is 100% undetectable - use at your own risk

## License

MIT License - see [https://github.com/zo4r5d0z4/cosmic/blob/main/LICENSE](LICENSE) file for details.
