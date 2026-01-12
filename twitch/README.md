# 🎨 Twitch Crayon Bot

A playful Twitch chat bot that lets your viewers control an RGB light crayon via
Home Assistant. Because who doesn't want their chat to turn their lights pink?

## 🚀 What It Does

This bot connects to Twitch chat and listens for `!crayon` commands, allowing
viewers to change the color of an ESPHome-powered RGB light. Supports:

- RGB values (`!crayon 255,0,128`)
- Hex codes (`!crayon #ff0080` or `!crayon #f08`)
- Named colors (`!crayon Magenta`)
- Special effects (`!crayon Rainbow`)

Check out [USAGE.md](../doc/USAGE.md) for the full list of supported colors and
effects.

## 🛠️ Getting Started

### Prerequisites

- Python 3.13+
- [pdm](https://pdm-project.org/) package manager
- A Twitch application (get your credentials at
  [dev.twitch.tv](https://dev.twitch.tv/))
- A Home Assistant instance with an ESPHome RGB light

### Installation

Clone the repo and install dependencies:

```bash
cd twitch
pdm install
```

For development with Jupyter notebook support:

```bash
pdm install --dev
```

### Configuration

Create a `.env` file in the `twitch/` directory with your credentials (see
`.env.template`):

- `APP_ID` & `APP_SECRET`: Your Twitch application credentials
- `TARGET_CHANNEL`: The Twitch channel to join (without the #)
- `USAGE_URL`: Link to usage instructions, for the `!usage` command
- `HATOKEN`: Long-lived access token from Home Assistant
- `HAURL`: Your Home Assistant instance URL (with trailing slash)

### Running the Bot

```bash
pdm run tc
```

The first time you run it, you'll need to authenticate via your browser. Press
Enter in the console to stop the bot.

## 🔧 Development

### The Colors Notebook

The [Colors.ipynb](exploration/Colors.ipynb) notebook is where the magic
happens! It:

- Scrapes french color names from the web
- Filters colors with sufficient brightness for LED display
- Deduplicates visually similar colors
- Generates the final `colors.py` file with normalized names and documentation

Run it to regenerate the color dictionary if you want to tweak the color
selection.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE).

---

_Built with love and way too much time spent picking the perfect shade of cyan._
