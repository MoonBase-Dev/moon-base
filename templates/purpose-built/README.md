Installation Instructions

Install Starship: curl -sS https://starship.rs/install.sh | sh
Create ~/.config/starship.toml
Copy the relevant config above
Add to your shell profile:

Bash: eval "$(starship init bash)"
Zsh: eval "$(starship init zsh)"
Fish: starship init fish | source
PowerShell: Invoke-Expression (&starship init powershell)



Pro Tips

Mix and match modules from different configs
Adjust truncation_length based on your terminal width
Use starship explain to understand what each symbol means
Customize colors with: black, red, green, yellow, blue, purple, cyan, white
Add bold, italic, underline, or strikethrough for styling
Test configs with starship print-config before applying

Each config is optimized for maximum productivity in its specific domain while maintaining visual appeal and information density!

---

Ultimate Starship Configs Collection
A curated collection of hyper-focused Starship terminal prompts optimized for specific programming languages and IT roles. Each configuration is designed to enhance productivity by displaying the most relevant information for your workflow while maintaining visual appeal and performance.
🎯 Design Philosophy

Hyper-focused: Each config shows only information that matters for that specific technology or role
Performance-first: Optimized for fast loading with minimal system overhead
Visually distinctive: Unique color palettes and symbols for easy identification
Context-aware: Intelligent detection of files, tools, and environments
Production-ready: Real-world tools and metrics that professionals actually use


🖥️ Programming Language Configurations
Python 🐍
Focus: Data science, virtual environments, package management

Features: PyEnv version display, Conda environment detection, virtual environment status, package info
Color Palette: Deep blues and golds (wisdom and power)
Best For: Data scientists, ML engineers, backend developers
Special: Emphasizes environment isolation and package management

C++ ⚡
Focus: High-performance computing, memory awareness, build systems

Features: CMake detection, memory usage monitoring, precise timing, compiler optimization hints
Color Palette: Electric blues and silver (performance and precision)
Best For: Systems programmers, game developers, HPC engineers
Special: Performance metrics prominently displayed

C 🔩
Focus: System-level programming, hardware interaction, minimal overhead

Features: Memory usage tracking, microsecond timing, low-level system indicators
Color Palette: Industrial grays and oranges (bare metal)
Best For: Embedded developers, kernel programmers, system architects
Special: Emphasizes resource awareness and system-level concerns

Java ☕
Focus: Enterprise development, build tools, framework integration

Features: Maven/Gradle detection, Spring framework awareness, enterprise tooling
Color Palette: Rich browns and oranges (coffee culture)
Best For: Enterprise developers, Spring developers, Android developers
Special: Heavy focus on build systems and enterprise frameworks

C# 💜
Focus: Microsoft ecosystem, .NET framework, cross-platform development

Features: .NET version display, NuGet package info, Microsoft tooling integration
Color Palette: Microsoft purples and blues (brand alignment)
Best For: .NET developers, enterprise Microsoft stack developers
Special: Seamless integration with Microsoft development tools

JavaScript 🟨
Focus: Modern web development, package management, Node.js ecosystem

Features: Node.js version, NPM/Yarn detection, package.json awareness, module info
Color Palette: Vibrant yellows and blacks (JS logo colors)
Best For: Full-stack developers, frontend developers, Node.js developers
Special: Comprehensive package manager support and web-focused indicators

Go 🐹
Focus: Cloud-native development, microservices, performance monitoring

Features: Go version display, module info, fast execution timing, memory efficiency
Color Palette: Go's signature cyan and blue (official branding)
Best For: DevOps engineers, microservice developers, cloud engineers
Special: Emphasizes Go's performance characteristics and simplicity

Visual Basic 🔷
Focus: Legacy system maintenance, Windows development, RAD environments

Features: VB file detection, Windows-specific indicators, project structure awareness
Color Palette: Classic Microsoft blues (heritage)
Best For: Legacy system maintainers, Windows application developers
Special: Designed for maintaining and updating existing VB codebases

Delphi/Object Pascal 🏛️
Focus: Desktop applications, database connectivity, RAD development

Features: Pascal file detection, component-based development indicators
Color Palette: Classical architecture blues and whites (stability)
Best For: Desktop application developers, database application developers
Special: Emphasizes the architectural strength and database connectivity

Fortran 🧮
Focus: Scientific computing, numerical analysis, HPC environments

Features: Fortran standard detection, scientific computing indicators, precision focus
Color Palette: Scientific greens and blues (research environment)
Best For: Scientists, researchers, numerical analysts, HPC developers
Special: Highlights scientific computing capabilities and standards compliance

Ada 🛡️
Focus: Safety-critical systems, military/aerospace applications, reliability

Features: Ada standard compliance, safety indicators, reliability metrics
Color Palette: Military greens (safety and reliability)
Best For: Aerospace engineers, defense contractors, safety-critical developers
Special: Emphasizes safety, security, and reliability aspects

SQL 🗃️
Focus: Database operations, query optimization, data management

Features: Database connection indicators, query performance hints, schema awareness
Color Palette: Database blues and grays (data storage)
Best For: Database developers, data engineers, analysts
Special: Focus on database operations and data integrity

Perl 🐪
Focus: Text processing, system administration, legacy script maintenance

Features: Perl version display, CPAN module awareness, regex optimization hints
Color Palette: Desert tans and purples (Perl camel heritage)
Best For: System administrators, text processing specialists, legacy maintainers
Special: Emphasizes Perl's text processing strengths and module ecosystem

R 📈
Focus: Statistical analysis, data visualization, research computing

Features: R version, package library status, statistical computing indicators
Color Palette: Statistical blues and data visualization colors
Best For: Data scientists, statisticians, researchers, analysts
Special: Heavy focus on statistical packages and data analysis workflows

PHP 🐘
Focus: Web development, server-side scripting, CMS development

Features: PHP version, Composer package management, web framework detection
Color Palette: PHP's signature purple and blue
Best For: Web developers, WordPress developers, backend developers
Special: Web-focused with emphasis on package management and frameworks

Scratch 🧩
Focus: Educational programming, visual coding, teaching environments

Features: Project file detection, colorful visual indicators, learning-friendly display
Color Palette: Colorful and playful (educational environment)
Best For: Educators, students, programming instructors
Special: Designed to be encouraging and visually engaging for learners

MATLAB 🔬
Focus: Scientific computing, engineering analysis, mathematical modeling

Features: MATLAB version, toolbox awareness, scientific computation indicators
Color Palette: Scientific oranges and blues (engineering focus)
Best For: Engineers, scientists, researchers, mathematicians
Special: Emphasizes scientific and engineering computing capabilities

Rust 🦀
Focus: Systems programming, memory safety, performance optimization

Features: Cargo package info, memory safety indicators, performance metrics
Color Palette: Rust's signature orange and black
Best For: Systems programmers, web assembly developers, performance-critical developers
Special: Highlights Rust's memory safety and performance characteristics

Assembly ⚙️
Focus: Low-level programming, hardware optimization, embedded systems

Features: Architecture detection, memory layout awareness, cycle counting
Color Palette: Mechanical grays and blues (hardware level)
Best For: Embedded developers, reverse engineers, performance optimizers
Special: Ultra-minimal with focus on hardware-level concerns

COBOL 🏛️
Focus: Legacy system maintenance, business applications, mainframe computing

Features: COBOL dialect detection, mainframe indicators, business logic focus
Color Palette: Legacy system greens and yellows (institutional)
Best For: Mainframe developers, legacy system maintainers, business application developers
Special: Designed for maintaining critical business systems


👨‍💻 IT Role Configurations
1. System Administrator 🖥️
Focus: Server management, system monitoring, infrastructure maintenance

Key Features:

Hostname and user privilege display
Memory usage monitoring with alerts
Command execution timing for performance tracking
System status indicators
Real-time clock for incident logging


Color Palette: Server room blues and warning oranges
Special Strengths: Infrastructure health monitoring, privilege awareness, performance tracking
Best For: Managing multiple servers, troubleshooting system issues, monitoring infrastructure health

2. Network Administrator 🌐
Focus: Network connectivity, bandwidth monitoring, routing management

Key Features:

Network gateway detection
Bandwidth usage monitoring (with vnstat)
Connection status indicators
SSH session awareness
Network performance timing


Color Palette: Network greens and connection blues
Special Strengths: Network topology awareness, connectivity monitoring, performance analysis
Best For: Managing network infrastructure, troubleshooting connectivity, monitoring traffic

3. Database Administrator (DBA) 🗄️
Focus: Database management, performance optimization, data integrity

Key Features:

MySQL/PostgreSQL version detection
Database connection status
Memory usage monitoring for database performance
Query execution timing
Data integrity indicators


Color Palette: Data blues and integrity greens
Special Strengths: Database-specific tooling, performance monitoring, multi-DBMS support
Best For: Managing database clusters, optimizing queries, monitoring database health

4. Help Desk Technician 🎧
Focus: User support, ticket management, system diagnostics

Key Features:

Friendly user identification
System uptime display
Ticket status reminders
Support session indicators
Quick diagnostic information


Color Palette: Support greens and friendly blues
Special Strengths: User-friendly display, support workflow integration, diagnostic helpers
Best For: Providing user support, tracking tickets, diagnosing user issues

5. Cybersecurity Analyst 🛡️
Focus: Threat detection, security monitoring, incident response

Key Features:

Security-first visual design
Threat monitoring indicators
User privilege highlighting
UTC timestamp for logs
Security alert symbols
Enhanced status monitoring


Color Palette: Security reds and protection blues
Special Strengths: Security-focused alerts, threat awareness, audit trail support
Best For: Monitoring security events, incident response, threat hunting

6. Cloud Engineer ☁️
Focus: Multi-cloud management, containerization, infrastructure as code

Key Features:

AWS/Azure/GCP context switching
Kubernetes cluster awareness
Docker container status
Terraform state tracking
Cloud resource monitoring


Color Palette: Cloud whites and sky blues
Special Strengths: Multi-cloud support, container orchestration, IaC integration
Best For: Managing cloud infrastructure, container deployments, infrastructure automation

7. Desktop Administrator 🖥️
Focus: Endpoint management, user workstation support, desktop deployment

Key Features:

Desktop environment detection
Active user monitoring
Battery status for mobile devices
Memory usage for workstation health
Desktop management indicators


Color Palette: Desktop blues and management greens
Special Strengths: Endpoint monitoring, user session tracking, mobile device support
Best For: Managing user workstations, desktop deployments, endpoint security

8. Software Engineer 👨‍💻
Focus: Code development, version control, build systems

Key Features:

Advanced Git status with branch indicators
Package management across languages
Build system detection
Development environment awareness
Code quality indicators


Color Palette: Code greens and development blues
Special Strengths: Multi-language support, Git workflow optimization, development tooling
Best For: Software development, version control management, multi-language projects

9. Data Analyst 📊
Focus: Data processing, statistical analysis, visualization workflows

Key Features:

Python/R statistical environment detection
Jupyter notebook integration
Data package management (Conda)
Analysis workflow indicators
Statistical computing context


Color Palette: Data visualization colors (blues, greens, purples)
Special Strengths: Statistical computing focus, notebook integration, data science tooling
Best For: Data analysis workflows, statistical computing, research projects

10. Web Developer 🌐
Focus: Full-stack web development, modern frameworks, responsive design

Key Features:

Multi-language web stack detection (HTML/CSS/JS)
Node.js and package manager support
Web framework awareness
Development server indicators
Asset pipeline monitoring


Color Palette: Web rainbow (HTML red, CSS blue, JS yellow)
Special Strengths: Full-stack awareness, modern web tooling, framework detection
Best For: Web application development, frontend/backend integration, modern web workflows


🚀 Quick Start

Install Starship:
bashcurl -sS https://starship.rs/install.sh | sh

Choose Your Config:

Copy the relevant configuration from the collection
Save to ~/.config/starship.toml


Initialize in Your Shell:
bash# Bash
echo 'eval "$(starship init bash)"' >> ~/.bashrc

# Zsh
echo 'eval "$(starship init zsh)"' >> ~/.zshrc

# Fish
echo 'starship init fish | source' >> ~/.config/fish/config.fish

# PowerShell
Add-Content $PROFILE "Invoke-Expression (&starship init powershell)"

Restart Your Terminal and enjoy your optimized prompt!

🛠️ Customization Tips

Mix Configs: Combine modules from different configurations for hybrid workflows
Adjust Performance: Modify min_time values based on your system's performance
Custom Colors: Use bold, italic, underline, or hex colors like "#ff6b6b"
Test First: Use starship explain to understand what each symbol represents
Environment Specific: Use different configs for different projects or environments

📋 Requirements

Starship: Latest version recommended
Nerd Font: Required for proper symbol display
Shell: Bash, Zsh, Fish, or PowerShell
Optional Tools: Language-specific tools for full functionality (git, docker, etc.)

🤝 Contributing
Each configuration is battle-tested in real-world scenarios. If you have suggestions for improvements or additional role-specific configurations, contributions are welcome!
📝 License
These configurations are provided as-is for the community. Use, modify, and share freely!

Optimized for productivity, designed for professionals, crafted with care. ⭐
