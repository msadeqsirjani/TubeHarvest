# 📚 TubeHarvest Documentation

This directory contains comprehensive documentation for TubeHarvest, designed to be used with GitHub Wiki.

## 📁 Documentation Structure

```
docs/
├── README.md               # This file
├── _Sidebar.md            # GitHub Wiki sidebar navigation
├── Home.md                # Main wiki homepage
├── Installation-Guide.md  # Complete installation instructions
├── Quick-Start.md         # Get started quickly
├── Interactive-Mode.md    # Interactive GUI documentation
├── CLI-Reference.md       # Command line reference
├── Troubleshooting.md     # Common issues and solutions
└── Developer-Guide.md     # Contributing and development
```

## 🌐 GitHub Wiki Setup

To set up these docs as a GitHub Wiki:

### Method 1: Manual Upload
1. Go to your GitHub repository
2. Click on the **Wiki** tab
3. Click **Create the first page**
4. Copy content from `Home.md` into the homepage
5. Create new pages for each markdown file
6. Copy content from `_Sidebar.md` to create the sidebar

### Method 2: Git Clone (Recommended)
```bash
# Clone the wiki repository
git clone https://github.com/msadeqsirjani/TubeHarvest.wiki.git

# Copy documentation files
cp docs/*.md TubeHarvest.wiki/

# Commit and push
cd TubeHarvest.wiki
git add .
git commit -m "Add comprehensive documentation"
git push origin master
```

### Method 3: Automated Script
```bash
# Create a simple script to sync docs
#!/bin/bash
# File: scripts/sync-wiki.sh

WIKI_DIR="../TubeHarvest.wiki"

if [ ! -d "$WIKI_DIR" ]; then
    git clone https://github.com/msadeqsirjani/TubeHarvest.wiki.git "$WIKI_DIR"
fi

# Copy all markdown files
cp docs/*.md "$WIKI_DIR/"

# Commit and push changes
cd "$WIKI_DIR"
git add .
git commit -m "Update documentation $(date)"
git push origin master

echo "Wiki updated successfully!"
```

## 📋 Documentation Pages

### 🚀 Getting Started
- **[Home](Home.md)** - Main overview and navigation
- **[Installation Guide](Installation-Guide.md)** - Complete setup instructions  
- **[Quick Start](Quick-Start.md)** - Essential commands and examples

### 📖 User Guides
- **[Interactive Mode](Interactive-Mode.md)** - Beautiful GUI interface
- **[CLI Reference](CLI-Reference.md)** - Complete command line documentation

### 🛠️ Development
- **[Developer Guide](Developer-Guide.md)** - Contributing and development setup

### 🆘 Help & Support  
- **[Troubleshooting](Troubleshooting.md)** - Common issues and solutions

## 🎯 Usage Guidelines

### For Users
1. Start with **[Quick Start](Quick-Start.md)** for immediate usage
2. Explore **[Interactive Mode](Interactive-Mode.md)** for the best experience
3. Reference **[CLI Guide](CLI-Reference.md)** for advanced usage
4. Check **[Troubleshooting](Troubleshooting.md)** if you encounter issues

### For Contributors
1. Read **[Developer Guide](Developer-Guide.md)** for setup instructions
2. Follow coding standards and testing requirements
3. Update documentation when adding features

### For Maintainers
1. Keep documentation in sync with code changes
2. Update version numbers and examples
3. Review and improve clarity regularly

## ✏️ Contributing to Documentation

### Writing Guidelines
- **Clear and concise** language
- **Step-by-step** instructions with examples
- **Consistent formatting** with markdown
- **Visual elements** like emojis and code blocks
- **Cross-references** between related pages

### Style Conventions
- Use **emoji** for section headers (🚀, 📖, 🔧, etc.)
- Include **code examples** for all features
- Add **troubleshooting** sections where relevant
- Link to **related documentation** frequently

### Content Structure
```markdown
# Page Title

Brief introduction explaining what this page covers.

## Section 1
Content with examples...

## Section 2  
More content...

## Next Steps
- Link to related pages
- Suggested workflows

---
*Footer with helpful links*
```

## 🔄 Keeping Documentation Updated

### Regular Updates
- **Version releases** - Update version numbers and new features
- **Bug fixes** - Update troubleshooting guides
- **User feedback** - Improve clarity and add missing information
- **Code changes** - Ensure examples remain accurate

### Automation
Consider setting up GitHub Actions to:
- **Validate links** in documentation
- **Check spelling** and grammar
- **Auto-sync** with wiki on changes
- **Generate** API documentation from code

## 📊 Documentation Metrics

Track documentation effectiveness:
- **User feedback** on clarity and completeness
- **Common support questions** (indicates missing docs)
- **Wiki page views** and engagement
- **Contribution patterns** from community

## 🔗 External Resources

### Helpful Links
- [GitHub Wiki Documentation](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
- [Markdown Guide](https://www.markdownguide.org/)
- [Writing Good Documentation](https://www.writethedocs.org/)

### Tools
- **Markdown editors**: Typora, Mark Text, VS Code
- **Diagram tools**: Mermaid, Draw.io
- **Screenshot tools**: For visual guides

---

*📝 This documentation structure ensures comprehensive coverage of TubeHarvest functionality while remaining easy to navigate and maintain.* 