# 🚀 Starship Terminal Image Generator

> Generate beautiful terminal preview images for your Starship configurations

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Starship](https://img.shields.io/badge/Starship-Compatible-purple.svg)](https://starship.rs)

## ✨ Features

- 🎨 **Multiple Color Palettes**: Dracula, Nord, Catppuccin, Tokyo Night
- 📁 **Batch Processing**: Process multiple configurations at once
- 🔧 **Flexible Input**: Single config, batch config, or file patterns
- 🖼️ **High-Quality Output**: PNG images with gradient backgrounds and rounded corners
- 🎯 **Accurate Rendering**: Faithful reproduction of Starship prompt formats
- 🌈 **Module Support**: Username, hostname, directory, git, language modules
- 📊 **Configuration Analysis**: Shows active modules and settings
- 🕒 **Timestamped**: Includes generation timestamp

## 🛠️ Dependencies

### Required Python Packages

```bash
pip install pillow toml
```

### System Dependencies

The generator automatically detects and uses system fonts:

**macOS:**
- Monaco (default terminal font)

**Linux:**
- DejaVu Sans Mono
- JetBrains Mono
- Liberation Mono

**Windows:**
- Consolas

## 📦 Installation

1. **Clone or download** the script
2. **Install dependencies:**
   ```bash
   pip install pillow toml
   ```
3. **Run the generator:**
   ```bash
   python starship_generator.py
   ```

## 🚀 Usage

### Interactive Mode

Run the script and follow the prompts:

```bash
python starship_generator.py
```

### Processing Modes

The generator offers four processing modes:

#### 1. 🎯 Single Config File
Generate one image from a single `starship.toml` configuration.

#### 2. 📦 Batch Config File
Process multiple configurations from a single file with sections like:
```toml
[config.theme1]
format = "your format here"
# ... other settings

[config.theme2]
format = "another format"
# ... other settings
```

#### 3. 🗂️ Multiple Config Files
Process all config files matching a pattern:
- `*.toml` - All TOML files in current directory
- `./configs/*.toml` - All TOML files in configs directory
- Recursive patterns supported

#### 4. 🌈 All Palettes
Generate images for all available color palettes from a single config.

## 🎨 Available Color Palettes

| Palette | Description |
|---------|-------------|
| 🧛 **Dracula** | Dark theme with purple accents |
| 🧊 **Nord** | Arctic-inspired color scheme |
| 🐱 **Catppuccin** | Pastel theme with warm colors |
| 🌃 **Tokyo Night** | Inspired by Tokyo's neon lights |

## 📋 Configuration Format

The generator supports standard Starship configuration format:

```toml
format = """
[[$username]($username.style)[@$hostname]($hostname.style):[$directory]($directory.style)]($style)\
[$git_branch$git_status]($git_branch.style)\
[$nodejs$python$rust$golang]($nodejs.style)\
$character
"""

[username]
style = "blue bold"
show_always = true

[hostname]
style = "green bold"

[directory]
style = "cyan"

[git_branch]
style = "purple"

[character]
success_symbol = "[▶](green)"
error_symbol = "[▶](red)"
```

## 🎯 Supported Modules

- 👤 **username** - Current user
- 🖥️ **hostname** - System hostname  
- 📁 **directory** - Current directory
- 🌿 **git_branch** - Git branch name
- 📊 **git_status** - Git status indicators
- 🟢 **nodejs** - Node.js version
- 🐍 **python** - Python version
- 🦀 **rust** - Rust version
- 🐹 **golang** - Go version
- ⚡ **character** - Prompt character

## 📁 Output Structure

Generated images are saved with descriptive filenames:

```
starship_previews/
├── config_theme1_Dracula.png
├── config_theme1_Nord.png
├── config_theme2_Catppuccin.png
└── config_theme2_Tokyo_Night.png
```

## 🔧 Configuration Examples

### Basic Configuration
```toml
format = "[$username@$hostname]($style) [$directory]($directory.style) $character"

[username]
style = "blue bold"

[hostname]  
style = "green bold"

[directory]
style = "cyan"
```

### Advanced Configuration
```toml
format = """
[$username]($username.style)\
[@$hostname]($hostname.style)\
[($directory)]($directory.style)\
[$git_branch$git_status]($git_branch.style)\
[$nodejs]($nodejs.style)\
$character
"""

[username]
style = "purple bold"

[hostname]
style = "green bold"

[directory]
style = "cyan"
truncation_length = 3

[git_branch]
style = "purple"

[nodejs]
style = "green"
```

## 🐛 Troubleshooting

### Common Issues

**Font not found:**
- The generator will fall back to default fonts if system fonts aren't available
- Install JetBrains Mono or DejaVu Sans Mono for better results

**Config file not loading:**
- Ensure the file path is correct
- Check TOML syntax with a validator
- Verify file encoding is UTF-8

**Empty output:**
- Check that the format string is not empty
- Ensure modules are not all disabled

## 🤝 Contributing

Contributions are welcome! Please feel free to:

- 🐛 Report bugs
- 💡 Suggest new features  
- 🎨 Add new color palettes
- 📝 Improve documentation
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Starship](https://starship.rs) - The cross-shell prompt
- [Dracula Theme](https://draculatheme.com)
- [Nord Theme](https://nordtheme.com)
- [Catppuccin](https://catppuccin.com)
- [Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme)

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with:
   - Your configuration file
   - Error messages
   - System information (OS, Python version)

---

**Made with ❤️ for the Starship community**
