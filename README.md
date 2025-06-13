![moon-base logo](https://github.com/MoonBase-Dev/moon-base/blob/main/site_res/mb40.png) 
Moon Base is a visual editor designed to help you create, customize, and manage your [Starship](https://starship.rs/) prompt configuration files (`starship.toml`)                               with ease. It provides a user-friendly interface to tweak various settings, modules, and palettes, offering a live preview of both your                               prompt and the generated TOML output.



## ✨ Features

*   **Visual Configuration**: Interactively edit Starship settings without directly writing TOML.
*   **Predefined Templates**: Start quickly with a selection of common Starship prompt templates.
*   **Live Prompt Preview**: See an estimated visual representation of your prompt as you make changes.
*   **Real-time TOML Output**: View the generated `starship.toml` content, updated instantly.
*   **Global Settings Editor**: Configure top-level settings like `format`, `right_format`, `add_newline`, etc.
*   **Module Customization**:
    *   Enable or disable individual modules.
    *   Modify module `format` and `style` strings.
    *   Adjust module-specific properties (e.g., `truncation_length` for `directory`, symbols for `git_status`).
    *   Easy access to official module documentation.
*   **Palette Management**:
    *   Choose from predefined color palettes (e.g., Nord, Solarized Dark, Gruvbox).
    *   Create and manage custom palette variables for consistent styling.
    *   Color pickers for easy color selection.
*   **Import/Export**:
    *   Import an existing `starship.toml` file to edit visually.
    *   Export your configuration as a `starship.toml` file.
*   **Responsive Design**: Usable across different screen sizes.
*   **In-App Help**: A comprehensive help section guides you through Starship concepts and editor usage.
*   **Direct Links**: Quick links to Starship's official documentation and GitHub repository.
*   **Branding Logo**: Displays the "Moon Base" logo in the UI.

## 🚀 How to Use

Moon Base is designed to be intuitive. Here's a general workflow:

1.  **Project Setup**:
    *   Ensure you have an `assets` directory at the root of your project.
    *   Place the application logo, named `image.png`, inside this `assets` folder. The application expects it at `./assets/image.png`.

2.  **Access the Application**: Open `index.html` in your web browser.

3.  **Select a Template (Optional)**:
    *   On the left panel, under "Templates," you can choose a predefined template from the dropdown menu.
    *   The Moon Base logo (the `image.png` you added) is displayed below this section.
    *   Details of the selected template will appear below the dropdown.
    *   This is a great starting point if you're new or want a base to customize.

4.  **Customize Global Settings**:
    *   In the central panel, expand the "Global Settings" section.
    *   Modify settings like "Global Prompt Format" (`format`), "Right Prompt Format" (`right_format`), "Add Newline," etc.
    *   These settings define the overall structure and behavior of your prompt.

5.  **Configure Modules**:
    *   Scroll down to the "Modules" section in the central panel.
    *   Each available Starship module is listed (e.g., `directory`, `git_branch`, `nodejs`).
    *   **Enable/Disable**: Use the toggle switch next to each module name to enable or disable it.
    *   **Expand Module**: Click on a module's header to expand its settings.
    *   **Format & Style**: Adjust the `format` string (how the module's information is displayed) and the `style` string (its colors and text attributes).
    *   **Module-Specific Properties**: Configure individual properties for the module (e.g., `truncation_length` for the directory module, symbols for git status indicators). Tooltips and descriptions are provided.
    *   **Documentation**: Click the link icon next to the module name to visit the official Starship documentation for that module.

6.  **Manage Palettes**:
    *   In the "Palettes" section (above Modules), you can define color variables.
    *   **Predefined Palettes**: Select a predefined palette like "Nord" or "Solarized Dark" from the dropdown. This will populate the variables.
    *   **Custom Variables**:
        *   Add new variables by entering a name (e.g., `my_custom_blue`) and a value (e.g., `#5e81ac bold` or `blue underline`).
        *   Use the color picker to easily select colors, which will then be combined with other style attributes (like `bold`).
        *   These variables can then be used in your module `style` strings (e.g., `style = "$my_custom_blue"`).

7.  **Observe Previews**:
    *   **Live Preview Panel** (bottom left): Shows an approximation of how your prompt will look. This preview uses dummy data for module variables.
    *   **TOML Preview Panel** (bottom right): Displays the `starship.toml` content that is generated based on your current configuration. This is what you'll save and use with Starship.

8.  **Import Existing Configuration**:
    *   Click the "Import" icon (upward arrow) in the header.
    *   Select your local `starship.toml` file. The editor will load its configuration.
    *   The template selector will indicate "Imported Configuration".

9.  **Export Your Configuration**:
    *   Once you're happy with your setup, click the "Export" icon (downward arrow) in the header.
    *   This will download a `starship.toml` file containing your current configuration.
    *   Save this file to `~/.config/starship.toml` (or the appropriate location for your OS) for Starship to use it.

10. **Get Help**:
    *   Click the "Help" icon (question mark) in the header to open a modal with guidance on Starship concepts, formatting, styling, and Nerd Fonts.

## 💡 Tips for Starship

*   **Nerd Fonts**: For many icons and symbols to display correctly in your terminal (and in the Live Preview), you'll need a [Nerd Font](https://www.nerdfonts.com/) installed and configured in your terminal emulator.
*   **Format Strings**:
    *   Variables like `$directory`, `$git_branch` are replaced by module output.
    *   Use `[]` to make a section optional (it only appears if the variables inside it have content). E.g., `[on $hostname]`.
*   **Style Strings**:
    *   Combine colors (e.g., `green`, `fg:#ff0000`, `bg:blue`) and attributes (e.g., `bold`, `italic`, `underline`, `dimmed`).
    *   Refer to the [Starship documentation on styling](https://starship.rs/config/#styling) for all options.
*   **Palettes**: Using the `[palette]` table (managed via the Palette Editor) is highly recommended for defining reusable color variables, making your configuration cleaner and easier to maintain.

## Local Development Assets
*   If building localy, be sure you have an `assets` folder in the root of the project.
*   Place the application logo, named `example.png`, inside this `assets` folder as it's referenced by `App.tsx` via the path `./assets/image.png`.

## 🤝 Contributing & Feedback

This project is an evolving tool. If you have suggestions, find bugs, or want to contribute, please check the project's repository (if available) for contribution guidelines or to open an issue.

## 📄 License
GPL v3
availavle @ [License](https://github.com/MoonBase-Dev/moon-base/blob/main/MoonBase/LICENSE).

---
Enjoy crafting your perfect Starship prompt with Moon Base!

---

# 20 Sxxxxxtarship.toml Configurations + Right Prompt Collection

TODO

---

# Symbol Reference Table

## Git Symbols
| Symbol | Unicode | Description | Example Usage |
|--------|---------|-------------|---------------|
| 🌿 | U+1F33F | Git branch (nature) | `symbol = "🌿 "` |
| 🚀 | U+1F680 | Git branch (rocket) | `symbol = "🚀 "` |
| 🌸 | U+1F338 | Git branch (flower) | `symbol = "🌸 "` |
| ⚡ | U+26A1 | Git branch (lightning) | `symbol = "⚡"` |
| 🔥 | U+1F525 | Git status (fire) | `symbol = "🔥"` |
| ⭐ | U+2B50 | Git branch (star) | `symbol = "⭐ "` |
| 🎯 | U+1F3AF | Git branch (target) | `symbol = "🎯 "` |
| 🛸 | U+1F6F8 | Git branch (UFO) | `symbol = "🛸 "` |
| █ | U+2588 | Git branch (block) | `symbol = "█ "` |
| ◆ | U+25C6 | Git branch (diamond) | `symbol = "◆ "` |

## Directory Symbols
| Symbol | Unicode | Description | Example Usage |
|--------|---------|-------------|---------------|
| 📁 | U+1F4C1 | Folder | `format = "[📁 $path]($style)"` |
| 📂 | U+1F4C2 | Open folder | `format = "[📂 $path]($style)"` |
| 🌌 | U+1F30C | Space/universe | `format = "[🌌 $path]($style)"` |
| 🏠 | U+1F3E0 | Home | `format = "[🏠 $path]($style)"` |
| 📍 | U+1F4CD | Location pin | `format = "[📍 $path]($style)"` |
| 🗂️ | U+1F5C2 | File cabinet | `format = "[🗂️ $path]($style)"` |
| 💼 | U+1F4BC | Briefcase | `format = "[💼 $path]($style)"` |
| 🎪 | U+1F3AA | Circus tent | `format = "[🎪 $path]($style)"` |

## Character/Prompt Symbols
| Symbol | Unicode | Description | Example Usage |
|--------|---------|-------------|---------------|
| ❯ | U+276F | Right arrow | `success_symbol = "[❯](bold green)"` |
| → | U+2192 | Right arrow | `success_symbol = "[→](bold white)"` |
| ▶ | U+25B6 | Play button | `success_symbol = "[▶](bold green)"` |
| ➜ | U+279C | Right arrow curved | `success_symbol = "[➜](bold green)"` |
| ⚡ | U+26A1 | Lightning | `success_symbol = "[⚡](bold green)"` |
| 🚀 | U+1F680 | Rocket | `success_symbol = "[🚀](bold green)"` |
| ✨ | U+2728 | Sparkles | `success_symbol = "[✨](bold yellow)"` |
| 💫 | U+1F4AB | Dizzy star | `error_symbol = "[💫](bold red)"` |
| 💥 | U+1F4A5 | Explosion | `error_symbol = "[💥](bold red)"` |
| 🔴 | U+1F534 | Red circle | `error_symbol = "[🔴](bold red)"` |
| ✗ | U+2717 | X mark | `error_symbol = "[✗](bold red)"` |
| ❌ | U+274C | Cross mark | `error_symbol = "[❌](bold red)"` |
| 💀 | U+1F480 | Skull | `error_symbol = "[💀](bold red)"` |
| 🌈 | U+1F308 | Rainbow | `success_symbol = "[🌈](bold magenta)"` |
| λ | U+03BB | Lambda | `success_symbol = "[λ](bold green)"` |
| ⟩ | U+27E9 | Angle bracket | `success_symbol = "[⟩](bold green)"` |
| ● | U+25CF | Bullet | `success_symbol = "[●](white)"` |
| # | U+0023 | Hash | `success_symbol = "[#](bold green)"` |
| $ | U+0024 | Dollar | `success_symbol = "[$](bold white)"` |
| > | U+003E | Greater than | `success_symbol = "[>](white)"` |

## Language/Tool Symbols
| Symbol | Unicode | Description | Tool |
|--------|---------|-------------|------|
| ⬢ | U+2B22 | Hexagon | Node.js |
| 🐍 | U+1F40D | Snake | Python |
| 🦀 | U+1F980 | Crab | Rust |
| 🐹 | U+1F439 | Hamster | Go |
| ☕ | U+2615 | Coffee | Java |
| 🐳 | U+1F433 | Whale | Docker |
| ☸ | U+2638 | Wheel | Kubernetes |
| 📦 | U+1F4E6 | Package | Package managers |
| 💎 | U+1F48E | Diamond | Ruby |
| 🔧 | U+1F527 | Wrench | Tools/Jobs |
| ⚙️ | U+2699 | Gear | Configuration |
| 🏗️ | U+1F3D7 | Construction | Build tools |

## Status/Info Symbols
| Symbol | Unicode | Description | Usage |
|--------|---------|-------------|-------|
| 🔋 | U+1F50B | Battery | Battery status |
| 🕐 | U+1F550 | Clock | Time |
| ⏱️ | U+23F1 | Stopwatch | Command duration |
| ⏰ | U+23F0 | Alarm clock | Time/Duration |
| 🧠 | U+1F9E0 | Brain | Memory usage |
| 💾 | U+1F4BE | Floppy disk | Storage |
| 📊 | U+1F4CA | Bar chart | Statistics |
| 🌡️ | U+1F321 | Thermometer | Temperature/CPU |
| 📡 | U+1F4E1 | Satellite | Network |
| 🔒 | U+1F512 | Lock | Security/SSH |
| 🌐 | U+1F310 | Globe | Network/Web |
| 💻 | U+1F4BB | Computer | Hostname |
| 👤 | U+1F464 | User | Username |
| 🎮 | U+1F3AE | Game controller | Gaming theme |

## Decorative Symbols
| Symbol | Unicode | Description | Usage |
|--------|---------|-------------|-------|
| ◆ | U+25C6 | Diamond | Decorative |
| ◇ | U+25C7 | White diamond | Decorative |
| ◈ | U+25C8 | Diamond outline | Decorative |
| ◉ | U+25C9 | Circle dot | Decorative |
| ◎ | U+25CE | Bullseye | Decorative |
| ★ | U+2605 | Star | Decorative |
| ☆ | U+2606 | White star | Decorative |
| ▲ | U+25B2 | Triangle up | Decorative |
| ▼ | U+25BC | Triangle down | Decorative |
| ■ | U+25A0 | Square | Decorative |
| □ | U+25A1 | White square | Decorative |
| ⬢ | U+2B22 | Hexagon | Decorative |
| ⬡ | U+2B21 | White hexagon | Decorative |

## Usage Tips
- Use `symbol = "🚀 "` with a space for proper spacing
- Combine symbols: `format = "[🌿 git:$branch]($style) "`
- Test symbols in your terminal to ensure proper rendering
- Some symbols may require specific fonts (Nerd Fonts recommended)
- Use Unicode escapes if needed: `\u{1F680}` for 🚀
