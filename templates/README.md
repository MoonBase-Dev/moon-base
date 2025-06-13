## Box Bar Configurations
1. Classic Box
```toml
format = """[┌───── $directory ─────┐]$line_break[│]$character[│]"""
```
2. Rounded Box
```toml
format = """[╭───── $directory ─────╮]$line_break[│]$character[│]"""
```
3. Double Line Box
```toml
format = """[╔═════ $directory ═════╗]$line_break[║]$character[║]"""
```
4. Dashed Box
```toml
format = """[┌╌╌╌╌╌ $directory ═════┐]$line_break[╎]$character[╎]"""
```
5. Shadow Box
```toml
format = """[▛▀▀▀▀▀ $directory ▀▀▀▀▀▜]$line_break[▌]$character[▐]"""
```
6. ASCII Art Box
```toml
format = """[.-~-~-~- $directory -~-~-~-.]$line_break[|]$character[|]"""
```
7. Corner Box
```toml
format = """[🭰──────── $directory ────────🭯]$line_break[ ]$character[ ]"""
```
8. Bubble Box
```toml
format = """[🭶 $directory 🭷]$line_break[🭴]$character[🭵]"""
```
9. Heavy Box
```toml
format = """[▄▄▄▄▄ $directory ▄▄▄▄▄]$line_break[█]$character[█]"""
```
10. Arrow Box
```toml
format = """[◀━━━━━ $directory ━━━━━▶]$line_break[◇]$character[◇]"""
```

---

## Power Bar Configurations
1. Classic Powerline
```toml
format = """$directory$git_branch$git_status$line_break$character"""
[directory]
style = "bold blue"
format = "[]$style[ $path ]($style)[](bg:blue fg:green)"
```
2. Double Powerline
```toml
format = """[]$os[]$directory[]$git_branch[]$line_break$character"""
[os]
style = "bg:red fg:white"
```
3. Round Powerline
```toml
format = """[]$directory[]$git_branch[]$line_break$character"""
[directory]
style = "bg:blue fg:white"
```
4. Sharp Powerline
```toml
format = """[]$directory[]$git_branch[]$line_break$character"""
[directory]
style = "bg:purple fg:white"
```
5. Thin Powerline
```toml
format = """[]$directory[]$git_branch[]$line_break$character"""
[directory]
style = "bg:green fg:black"
```
6. Block Powerline
```toml
format = """[█▓▒░]$directory[░▒▓█]$git_branch[░▒▓█]$line_break$character"""
[directory]
style = "bg:yellow fg:black"
```
7. Gradient Powerline
```toml
format = """[░▒▓]$directory[▓▒░]$git_branch[▓▒░]$line_break$character"""
[directory]
style = "bg:#005fff fg:white"
```
8. Arrow Powerline
```toml
format = """[➤]$directory[➤]$git_branch[➤]$line_break$character"""
[directory]
style = "bg:cyan fg:black"
```
9. Bubble Powerline
```toml
format = """[🭶]$directory[🭷]$git_branch[🭷]$line_break$character"""
[directory]
style = "bg:magenta fg:white"
```
10. Lightning Powerline
```toml
format = """[⚡]$directory[⚡]$git_branch[⚡]$line_break$character"""
[directory]
style = "bg:bright-black fg:yellow"
```

---

## Themed Power Bars:

```Ocean Wave: [🌊]$directory[🌊] with blue gradient```

```Fire Storm: [🔥]$directory[🔥] with red gradient```

```Nature: [🌿]$directory[🌿] with green gradient```

```Cyberpunk: []$directory[] with purple-pink gradient```

```Retro: [🕹]$directory[🕹] with scanline effect```

```Neon: []$directory[] with bright cyan glow```

```Matrix: []$directory[] with green-black fade```

```Galaxy: [🌌]$directory[🌌] with starry background```

```Lava Lamp: [♨]$directory[♨] with animated blobs```

```Hacker: []$directory[] with terminal matrix effect```

---

##  Unique Cursors

1. Sword Cursor
```toml
[character]
success_symbol = "[⚔](bold green)"
error_symbol = "[⚔](bold red)"
```
2. Wizard Staff
```toml
[character]
success_symbol = "[⋆⁺₊⋆](bold purple)"
error_symbol = "[⋆⁺₊⋆](bold red)"
```
3. Dragon
```toml
[character]
success_symbol = "[🐉](bold green)"
error_symbol = "[🐉](bold red)"
```
4. Spaceship
```toml
[character]
success_symbol = "[🛸](bold blue)"
error_symbol = "[🛸](bold red)"
```
5. Ninja Star
```toml
[character]
success_symbol = "[☆](bold white)"
error_symbol = "[☆](bold red)"
```
6. Poison
```toml
[character]
success_symbol = "[☠](bold green)"
error_symbol = "[☠](bold red)"
```
7. Magic Wand
```toml
[character]
success_symbol = "[✨](bold yellow)"
error_symbol = "[✨](bold red)"
```
8. Alien
```toml
[character]
success_symbol = "[👽](bold green)"
error_symbol = "[👽](bold red)"
```
9. Lightning Bolt
```toml
[character]
success_symbol = "[⚡](bold yellow)"
error_symbol = "[⚡](bold red)"
```
10. Black Hole
```toml
[character]
success_symbol = "[🕳](bold black)"
error_symbol = "[🕳](bold red)"
```

---
