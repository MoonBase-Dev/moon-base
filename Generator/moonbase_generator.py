import toml
import os
import re
import json
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import glob
from datetime import datetime

# Define available palettes
palettes = {
    "Dracula": {
        "background": "#282a36",
        "foreground": "#f8f8f2",
        "username": "#bd93f9",
        "hostname": "#50fa7b",
        "directory": "#8be9fd",
        "git_branch": "#bd93f9",
        "git_status": "#ff5555",
        "character": "#50fa7b",
        "time": "#6272a4",
        "success": "#50fa7b",
        "error": "#ff5555",
        "cmd_duration": "#ffb86c",
        "battery": "#f1fa8c",
        "nodejs": "#50fa7b",
        "python": "#f1fa8c",
        "rust": "#ffb86c",
        "golang": "#8be9fd",
        "orange": "#ffb86c"
    },
    "Nord": {
        "background": "#2e3440",
        "foreground": "#d8dee9",
        "username": "#81a1c1",
        "hostname": "#88c0d0",
        "directory": "#8fbcbb",
        "git_branch": "#b48ead",
        "git_status": "#bf616a",
        "character": "#a3be8c",
        "time": "#4c566a",
        "success": "#a3be8c",
        "error": "#bf616a",
        "cmd_duration": "#ebcb8b",
        "battery": "#d08770",
        "nodejs": "#a3be8c",
        "python": "#ebcb8b",
        "rust": "#d08770",
        "golang": "#8fbcbb",
        "orange": "#d08770"
    },
    "Catppuccin": {
        "background": "#1e1e2e",
        "foreground": "#cdd6f4",
        "username": "#cba6f7",
        "hostname": "#a6e3a1",
        "directory": "#89b4fa",
        "git_branch": "#cba6f7",
        "git_status": "#f38ba8",
        "character": "#a6e3a1",
        "time": "#6c7086",
        "success": "#a6e3a1",
        "error": "#f38ba8",
        "cmd_duration": "#fab387",
        "battery": "#f9e2af",
        "nodejs": "#a6e3a1",
        "python": "#f9e2af",
        "rust": "#fab387",
        "golang": "#89b4fa",
        "orange": "#fab387"
    },
    "Tokyo Night": {
        "background": "#1a1b26",
        "foreground": "#c0caf5",
        "username": "#bb9af7",
        "hostname": "#9ece6a",
        "directory": "#7aa2f7",
        "git_branch": "#bb9af7",
        "git_status": "#f7768e",
        "character": "#9ece6a",
        "time": "#565f89",
        "success": "#9ece6a",
        "error": "#f7768e",
        "cmd_duration": "#e0af68",
        "battery": "#ff9e64",
        "nodejs": "#9ece6a",
        "python": "#e0af68",
        "rust": "#ff9e64",
        "golang": "#7aa2f7",
        "orange": "#ff9e64"
    }
}

def load_config(file_path):
    """Load TOML configuration file with error handling."""
    try:
        if not os.path.exists(file_path):
            print(f"Config file not found: {file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return toml.load(file)
    except Exception as e:
        print(f"Error loading config file: {e}")
        return None

def load_batch_config(file_path):
    """Load batch configuration file containing multiple configs."""
    try:
        if not os.path.exists(file_path):
            print(f"Batch config file not found: {file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Try to parse as JSON first (for structured batch configs)
        try:
            data = json.loads(content)
            if 'configs' in data:
                return data['configs']
        except json.JSONDecodeError:
            pass
        
        # Try to parse as TOML with multiple config sections
        try:
            data = toml.loads(content)
            
            # Look for config sections (e.g., [config.theme1], [config.theme2])
            configs = {}
            for key, value in data.items():
                if key.startswith('config.') or key == 'config':
                    if key == 'config':
                        configs['default'] = value
                    else:
                        config_name = key.replace('config.', '')
                        configs[config_name] = value
                elif isinstance(value, dict) and 'format' in value:
                    # Treat top-level sections with 'format' as individual configs
                    configs[key] = value
            
            return configs if configs else {'default': data}
            
        except toml.TomlDecodeError as e:
            print(f"Error parsing batch config as TOML: {e}")
            return None
            
    except Exception as e:
        print(f"Error loading batch config file: {e}")
        return None

def find_config_files(pattern):
    """Find config files matching a pattern."""
    try:
        files = glob.glob(pattern, recursive=True)
        # Filter for likely config files
        config_files = [f for f in files if f.endswith(('.toml', '.json')) and os.path.isfile(f)]
        return config_files
    except Exception as e:
        print(f"Error finding config files: {e}")
        return []

def get_font(size=16):
    """Try to load a better font, fall back to default if not available."""
    font_paths = [
        "/System/Library/Fonts/Monaco.ttf",  # macOS
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",  # Linux
        "C:/Windows/Fonts/consola.ttf",  # Windows
        "/usr/share/fonts/TTF/JetBrainsMono-Regular.ttf",  # Arch Linux
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",  # Ubuntu
    ]
    
    for font_path in font_paths:
        try:
            if os.path.exists(font_path):
                return ImageFont.truetype(font_path, size)
        except:
            continue
    
    return ImageFont.load_default()

def get_sample_data():
    """Generate sample data for modules."""
    return {
        'username': 'starship_user',
        'hostname': 'desktop-pc',
        'directory': '~/projects/starship-config',
        'branch': 'main',
        'all_status': '+2 ~1 ?3',
        'version': 'v18.17.0',  # For nodejs
        'symbol': '',
        'character_symbol': '▶'
    }

def get_color_from_style(style, palette, default_color='foreground'):
    """Extract color from style string."""
    if not style:
        return palette.get(default_color, palette['foreground'])
    
    style_lower = style.lower()
    
    # Direct color mappings
    color_map = {
        'blue': 'username',
        'green': 'hostname', 
        'cyan': 'directory',
        'purple': 'git_branch',
        'red': 'error',
        'yellow': 'python',
        'orange': 'orange'
    }
    
    for color_name, palette_key in color_map.items():
        if color_name in style_lower:
            return palette.get(palette_key, palette['foreground'])
    
    return palette.get(default_color, palette['foreground'])

def substitute_variables(format_str, sample_data, module_config, palette):
    """Substitute variables in format string and return segments with colors."""
    if not format_str:
        return []
    
    segments = []
    current_pos = 0
    
    # Find all variable references and style blocks
    pattern = r'\[([^\]]+)\]\(\$?([^)]+)\)|\$([a-zA-Z_]+)'
    
    for match in re.finditer(pattern, format_str):
        # Add any literal text before this match
        if match.start() > current_pos:
            literal_text = format_str[current_pos:match.start()]
            if literal_text.strip():
                segments.append({
                    'text': literal_text,
                    'color': palette['foreground']
                })
        
        if match.group(1) and match.group(2):  # [text](style) format
            text = match.group(1)
            style = match.group(2)
            
            # Substitute variables in text
            for var, value in sample_data.items():
                text = text.replace(f'${var}', str(value))
            
            # Get color from style
            if style.startswith('$'):
                # Style reference like $username.style
                style_key = style[1:]  # Remove $
                if '.' in style_key:
                    module_name, style_prop = style_key.split('.', 1)
                    actual_style = module_config.get(module_name, {}).get(style_prop, style)
                else:
                    actual_style = module_config.get(style_key, {}).get('style', style)
            else:
                actual_style = style
            
            color = get_color_from_style(actual_style, palette)
            
            segments.append({
                'text': text,
                'color': color
            })
        
        elif match.group(3):  # $variable format
            var_name = match.group(3)
            value = sample_data.get(var_name, f'${var_name}')
            
            # For module references, we'll handle them specially
            if var_name in ['nodejs', 'python', 'rust', 'golang', 'go']:
                module_name = 'golang' if var_name == 'go' else var_name
                mod_config = module_config.get(module_name, {})
                
                if not mod_config.get('disabled', False):
                    symbol = mod_config.get('symbol', '')
                    version = sample_data.get('version', 'v1.0.0')
                    
                    # Different versions for different languages
                    if module_name == 'nodejs':
                        version = 'v18.17.0'
                    elif module_name == 'python':
                        version = 'v3.11.4'
                    elif module_name == 'rust':
                        version = 'v1.70.0'
                    elif module_name == 'golang':
                        version = 'v1.20.5'
                    
                    text = f"{symbol}{version}"
                    color = get_color_from_style(mod_config.get('style', ''), palette, module_name)
                    
                    segments.append({
                        'text': text,
                        'color': color
                    })
            else:
                segments.append({
                    'text': str(value),
                    'color': palette['foreground']
                })
        
        current_pos = match.end()
    
    # Add any remaining literal text
    if current_pos < len(format_str):
        remaining_text = format_str[current_pos:]
        if remaining_text.strip():
            segments.append({
                'text': remaining_text,
                'color': palette['foreground']
            })
    
    return segments

def render_prompt_format(config, palette):
    """Render the complete prompt format."""
    if not config:
        return ["No configuration loaded"]
    
    sample_data = get_sample_data()
    format_str = config.get('format', '')
    
    if not format_str:
        return ["No format string found in configuration"]
    
    # Split format into lines
    lines = format_str.strip().split('\n')
    rendered_lines = []
    
    for line in lines:
        if not line.strip():
            rendered_lines.append([])
            continue
        
        segments = substitute_variables(line, sample_data, config, palette)
        rendered_lines.append(segments)
    
    return rendered_lines

def calculate_text_width(text, font):
    """Calculate the width of text with given font."""
    try:
        bbox = font.getbbox(text)
        return bbox[2] - bbox[0]
    except:
        return len(text) * 8  # Fallback

def draw_rounded_rectangle(draw, xy, radius, fill):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def generate_terminal_image(config, palette, config_name="config", output_path='starship_terminal.png'):
    """Generate a terminal image with the given configuration and palette."""
    # Image dimensions
    width, height = 1000, 600
    
    # Create a base image with a slightly lighter background for the "desktop" feel
    desktop_bg_color = tuple(int(c * 0.8) for c in hex_to_rgb(palette['background'])) # Darker shade
    img = Image.new('RGB', (width, height), color=desktop_bg_color)
    draw = ImageDraw.Draw(img)
    
    # Terminal window dimensions and properties
    terminal_x_margin = 50
    terminal_y_margin = 70
    terminal_width = width - 2 * terminal_x_margin
    terminal_height = height - 2 * terminal_y_margin
    terminal_coords = (terminal_x_margin, terminal_y_margin, terminal_x_margin + terminal_width, terminal_y_margin + terminal_height)
    terminal_radius = 15  # Rounded corners
    
    # Draw a gradient for the terminal background
    terminal_bg_start = hex_to_rgb(palette['background'])
    # Slightly darker or lighter end color for the gradient
    terminal_bg_end = tuple(min(255, c + 20) if i == 0 else max(0, c - 20) for i, c in enumerate(terminal_bg_start))


    for y in range(terminal_y_margin, terminal_y_margin + terminal_height):
        # Calculate color interpolation for vertical gradient
        ratio = (y - terminal_y_margin) / terminal_height
        r = int(terminal_bg_start[0] + ratio * (terminal_bg_end[0] - terminal_bg_start[0]))
        g = int(terminal_bg_start[1] + ratio * (terminal_bg_end[1] - terminal_bg_start[1]))
        b = int(terminal_bg_start[2] + ratio * (terminal_bg_end[2] - terminal_bg_start[2]))
        
        # Draw a line of the gradient color across the width of the terminal area
        # This will be drawn on the main image before the rounded rectangle mask is applied
        draw.line([(terminal_x_margin, y), (terminal_x_margin + terminal_width, y)], fill=(r, g, b))

    # Create a mask for the rounded rectangle
    mask = Image.new('L', img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle(terminal_coords, radius=terminal_radius, fill=255)
    
    # Apply the mask to the gradient background
    gradient_img = img.copy() # The image already has the gradient drawn on it
    img = Image.composite(gradient_img, Image.new('RGB', img.size, desktop_bg_color), mask)
    draw = ImageDraw.Draw(img) # Re-initialize draw object for the new image

    # Add a subtle inner border/shadow effect to the terminal window
    border_color = tuple(min(255, c + 30) for c in hex_to_rgb(palette['background'])) # Lighter border
    border_coords = (terminal_x_margin + 1, terminal_y_margin + 1, terminal_x_margin + terminal_width - 1, terminal_y_margin + terminal_height - 1)
    draw_rounded_rectangle(draw, border_coords, terminal_radius - 1, None) # Draw outline
    draw.rounded_rectangle(terminal_coords, radius=terminal_radius, outline=border_color, width=2)


    # Load fonts
    font_large = get_font(18)
    font_medium = get_font(14)
    font_small = get_font(12)
    
    # Draw title (inside the terminal window)
    title_x = terminal_x_margin + 20
    title_y = terminal_y_margin + 20
    title = f"Starship Preview: {config_name}"
    draw.text((title_x, title_y), title, fill=palette['foreground'], font=font_large)
    
    # Draw a separator line
    draw.line([(terminal_x_margin + 20, terminal_y_margin + 50), (terminal_x_margin + terminal_width - 20, terminal_y_margin + 50)], fill=palette.get('time', palette['foreground']), width=1)
    
    # Render the complete prompt
    rendered_lines = render_prompt_format(config, palette)
    
    # Draw the rendered prompt
    y = terminal_y_margin + 80
    line_height = 20
    
    for line_segments in rendered_lines:
        if not line_segments:  # Empty line
            y += line_height
            continue
        
        x = terminal_x_margin + 20
        for segment in line_segments:
            text = segment['text']
            color = segment['color']
            
            draw.text((x, y), text, fill=color, font=font_medium)
            x += calculate_text_width(text, font_medium)
        
        y += line_height
    
    # Add some extra space and draw a sample command
    y += 20
    draw.text((terminal_x_margin + 20, y), "$ starship config", fill=palette['foreground'], font=font_medium)
    
    # Draw configuration info
    info_y = y + 40
    config_info = f"Configuration: {config_name}"
    draw.text((terminal_x_margin + 20, info_y), config_info, fill=palette.get('time', palette['foreground']), font=font_small)
    
    # Draw palette info
    palette_info = f"Color Palette: {palette.get('name', 'Custom')}"
    draw.text((terminal_x_margin + 20, info_y + 20), palette_info, fill=palette.get('time', palette['foreground']), font=font_small)
    
    # Show detected modules
    if config:
        modules = []
        for module in ['username', 'hostname', 'directory', 'git_branch', 'git_status', 'nodejs', 'python', 'rust', 'golang']:
            if module in config and not config[module].get('disabled', False):
                modules.append(module)
        
        if modules:
            modules_info = f"Active modules: {', '.join(modules)}"
            draw.text((terminal_x_margin + 20, info_y + 40), modules_info, fill=palette.get('time', palette['foreground']), font=font_small)
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    draw.text((terminal_x_margin + 20, terminal_y_margin + terminal_height - 30), f"Generated: {timestamp}", fill=palette.get('time', palette['foreground']), font=font_small)
    
    # Save the image
    try:
        img.save(output_path)
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def create_batch_output_filename(base_name, config_name, palette_name, extension='.png'):
    """Create a standardized filename for batch outputs."""
    # Sanitize names for filesystem
    safe_config = re.sub(r'[^\w\-_]', '_', config_name)
    safe_palette = re.sub(r'[^\w\-_]', '_', palette_name)
    safe_base = re.sub(r'[^\w\-_]', '_', base_name)
    
    return f"{safe_base}_{safe_config}_{safe_palette}{extension}"

def list_available_palettes():
    """Display available color palettes."""
    print("\nAvailable color palettes:")
    for i, palette_name in enumerate(palettes.keys(), 1):
        print(f"{i}. {palette_name}")

def get_processing_mode():
    """Get user's preferred processing mode."""
    print("\nProcessing Mode:")
    print("1. Single config file")
    print("2. Batch config file (multiple configs in one file)")
    print("3. Multiple config files (file pattern/directory)")
    print("4. All palettes for single config")
    
    while True:
        try:
            mode = int(input("\nSelect processing mode (1-4): ").strip())
            if 1 <= mode <= 4:
                return mode
        except ValueError:
            pass
        print("Invalid selection. Please enter 1, 2, 3, or 4.")

def process_single_config():
    """Process a single configuration file."""
    config_path = input("\nEnter the path to your starship.toml config file: ").strip()
    
    list_available_palettes()
    palette_name = get_palette_selection()
    
    output_path = input("\nEnter output filename (default: starship_terminal.png): ").strip()
    if not output_path:
        output_path = "starship_terminal.png"
    
    config = load_config(config_path)
    if config is None:
        print("Failed to load configuration.")
        return
    
    palette_data = palettes[palette_name].copy()
    palette_data['name'] = palette_name
    
    print(f"\nGenerating terminal image with {palette_name} palette...")
    success = generate_terminal_image(config, palette_data, "single", output_path)
    
    if success:
        print(f"✅ Terminal image generated successfully!")
        print(f"📁 Saved as: {output_path}")
    else:
        print("❌ Failed to generate terminal image.")

def process_batch_config():
    """Process a batch configuration file."""
    config_path = input("\nEnter the path to your batch config file: ").strip()
    
    configs = load_batch_config(config_path)
    if configs is None:
        print("Failed to load batch configuration.")
        return
    
    print(f"\nFound {len(configs)} configurations:")
    for name in configs.keys():
        print(f"  - {name}")
    
    # Palette selection
    print("\nPalette Options:")
    print("1. Use same palette for all configs")
    print("2. Generate with all palettes")
    
    palette_mode = input("Select option (1 or 2): ").strip()
    
    if palette_mode == "1":
        list_available_palettes()
        palette_name = get_palette_selection()
        selected_palettes = [palette_name]
    else:
        selected_palettes = list(palettes.keys())
    
    # Output directory
    output_dir = input("\nEnter output directory (default: ./starship_previews): ").strip()
    if not output_dir:
        output_dir = "./starship_previews"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate images
    total_generated = 0
    base_name = Path(config_path).stem
    
    for config_name, config_data in configs.items():
        for palette_name in selected_palettes:
            palette_data = palettes[palette_name].copy()
            palette_data['name'] = palette_name
            
            output_filename = create_batch_output_filename(base_name, config_name, palette_name)
            output_path = os.path.join(output_dir, output_filename)
            
            print(f"Generating: {config_name} with {palette_name} palette...")
            success = generate_terminal_image(config_data, palette_data, config_name, output_path)
            
            if success:
                total_generated += 1
                print(f"  ✅ Saved: {output_filename}")
            else:
                print(f"  ❌ Failed: {output_filename}")
    
    print(f"\n🎉 Generated {total_generated} terminal images in {output_dir}")

def process_multiple_configs():
    """Process multiple configuration files."""
    pattern = input("\nEnter file pattern or directory (e.g., *.toml, ./configs/*.toml): ").strip()
    
    config_files = find_config_files(pattern)
    if not config_files:
        print("No configuration files found matching the pattern.")
        return
    
    print(f"\nFound {len(config_files)} configuration files:")
    for file in config_files:
        print(f"  - {file}")
    
    # Palette selection
    print("\nPalette Options:")
    print("1. Use same palette for all configs")
    print("2. Generate with all palettes")
    
    palette_mode = input("Select option (1 or 2): ").strip()
    
    if palette_mode == "1":
        list_available_palettes()
        palette_name = get_palette_selection()
        selected_palettes = [palette_name]
    else:
        selected_palettes = list(palettes.keys())
    
    # Output directory
    output_dir = input("\nEnter output directory (default: ./starship_previews): ").strip()
    if not output_dir:
        output_dir = "./starship_previews"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate images
    total_generated = 0
    
    for config_path in config_files:
        config = load_config(config_path)
        if config is None:
            print(f"⚠️  Skipping {config_path} (failed to load)")
            continue
        
        config_name = Path(config_path).stem
        
        for palette_name in selected_palettes:
            palette_data = palettes[palette_name].copy()
            palette_data['name'] = palette_name
            
            output_filename = create_batch_output_filename(config_name, "config", palette_name)
            output_path = os.path.join(output_dir, output_filename)
            
            print(f"Generating: {config_name} with {palette_name} palette...")
            success = generate_terminal_image(config, palette_data, config_name, output_path)
            
            if success:
                total_generated += 1
                print(f"  ✅ Saved: {output_filename}")
            else:
                print(f"  ❌ Failed: {output_filename}")
    
    print(f"\n🎉 Generated {total_generated} terminal images in {output_dir}")

def process_all_palettes():
    """Generate all palette variations for a single config."""
    config_path = input("\nEnter the path to your starship.toml config file: ").strip()
    
    config = load_config(config_path)
    if config is None:
        print("Failed to load configuration.")
        return
    
    # Output directory
    output_dir = input("\nEnter output directory (default: ./starship_previews): ").strip()
    if not output_dir:
        output_dir = "./starship_previews"
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate images for all palettes
    total_generated = 0
    config_name = Path(config_path).stem
    
    for palette_name in palettes.keys():
        palette_data = palettes[palette_name].copy()
        palette_data['name'] = palette_name
        
        output_filename = create_batch_output_filename(config_name, "config", palette_name)
        output_path = os.path.join(output_dir, output_filename)
        
        print(f"Generating: {palette_name} palette...")
        success = generate_terminal_image(config, palette_data, config_name, output_path)
        
        if success:
            total_generated += 1
            print(f"  ✅ Saved: {output_filename}")
        else:
            print(f"  ❌ Failed: {output_filename}")
    
    print(f"\n🎉 Generated {total_generated} terminal images with all palettes in {output_dir}")

def get_palette_selection():
    """Get palette selection from user."""
    while True:
        palette_input = input(f"\nSelect a palette (1-{len(palettes)} or name): ").strip()
        
        # Check if it's a number
        try:
            palette_index = int(palette_input) - 1
            if 0 <= palette_index < len(palettes):
                return list(palettes.keys())[palette_index]
        except ValueError:
            pass
        
        # Check if it's a palette name
        if palette_input in palettes:
            return palette_input
        
        # Check case-insensitive
        for palette_name in palettes:
            if palette_input.lower() == palette_name.lower():
                return palette_name
        
        print("Invalid selection. Please try again.")

def main():
    """Main function to run the terminal image generator."""
    try:
        print("Starship Terminal Image Generator")
        print("=" * 35)
        
        mode = get_processing_mode()
        
        if mode == 1:
            process_single_config()
        elif mode == 2:
            process_batch_config()
        elif mode == 3:
            process_multiple_configs()
        elif mode == 4:
            process_all_palettes()
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
