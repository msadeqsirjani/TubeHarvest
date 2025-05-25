#!/bin/bash
# TubeHarvest Wiki Sync Script
# Automatically syncs documentation from docs/ to GitHub Wiki
#
# Usage:
#   ./scripts/sync-wiki.sh            # Normal sync
#   ./scripts/sync-wiki.sh --dry-run  # Show what would be done without doing it

set -e

# Configuration
REPO_URL="https://github.com/msadeqsirjani/TubeHarvest.wiki.git"
WIKI_DIR="./TubeHarvest.wiki"
DOCS_DIR="./docs"

# Parse command line arguments
DRY_RUN=false
if [ "$1" == "--dry-run" ]; then
    DRY_RUN=true
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if we're in the right directory
if [ ! -d "$DOCS_DIR" ]; then
    log_error "docs/ directory not found. Please run this script from the TubeHarvest root directory."
    exit 1
fi

if [ "$DRY_RUN" = true ]; then
    log_info "Starting TubeHarvest Wiki sync (DRY RUN - no changes will be made)..."
else
    log_info "Starting TubeHarvest Wiki sync..."
fi

# Clone or update wiki repository
if [ "$DRY_RUN" = false ]; then
    if [ ! -d "$WIKI_DIR" ]; then
        log_info "Cloning wiki repository..."
        git clone "$REPO_URL" "$WIKI_DIR"
        if [ $? -eq 0 ]; then
            log_success "Wiki repository cloned successfully"
        else
            log_error "Failed to clone wiki repository"
            exit 1
        fi
    else
        log_info "Updating existing wiki repository..."
        cd "$WIKI_DIR"
        git pull origin main
        if [ $? -eq 0 ]; then
            log_success "Wiki repository updated"
        else
            log_warning "Failed to update wiki repository, continuing anyway..."
        fi
        cd ..
    fi
else
    log_info "Would clone/update wiki repository from $REPO_URL"
    # Create temporary directory for dry run
    if [ ! -d "$WIKI_DIR" ]; then
        mkdir -p "$WIKI_DIR"
    fi
fi

# Copy documentation files
log_info "Copying documentation files..."

# Files to exclude from copying (add any files you don't want in the wiki)
exclude_files=()

# Function to check if file should be excluded
should_exclude() {
    local file="$1"
    for exclude in "${exclude_files[@]}"; do
        if [[ "$file" == "$exclude" ]]; then
            return 0  # Should exclude
        fi
    done
    return 1  # Should not exclude
}

log_info "Auto-detecting documentation files in $DOCS_DIR/"

# Show what files will be processed
md_files=("$DOCS_DIR"/*.md)
other_files=("$DOCS_DIR"/*.{txt,rst})

total_files=0
if [ ${#md_files[@]} -gt 0 ] && [ -f "${md_files[0]}" ]; then
    total_files=$((total_files + ${#md_files[@]}))
fi

# Count other files that actually exist
for file in "${other_files[@]}"; do
    if [ -f "$file" ]; then
        total_files=$((total_files + 1))
    fi
done

log_info "Found $total_files documentation files to process"

copied_count=0
skipped_count=0
shopt -s nullglob  # Handle case where no .md files exist

# Copy all markdown files
for file_path in "$DOCS_DIR"/*.md; do
    if [ -f "$file_path" ]; then
        filename=$(basename "$file_path")
        
        if should_exclude "$filename"; then
            log_warning "Skipped $filename (excluded)"
            ((skipped_count++))
            continue
        fi
        
        if [ "$DRY_RUN" = true ]; then
            log_info "Would copy $filename"
        else
            cp "$file_path" "$WIKI_DIR/"
            log_success "Copied $filename"
        fi
        ((copied_count++))
    fi
done

# Also copy any additional documentation files (txt, rst, etc.)
for file_path in "$DOCS_DIR"/*.{txt,rst}; do
    if [ -f "$file_path" ]; then
        filename=$(basename "$file_path")
        base_name="${filename%.*}"
        
        if should_exclude "$filename"; then
            log_warning "Skipped $filename (excluded)"
            ((skipped_count++))
            continue
        fi
        
        # Convert to markdown extension for wiki compatibility
        if [ "$DRY_RUN" = true ]; then
            log_info "Would copy $filename as ${base_name}.md"
        else
            cp "$file_path" "$WIKI_DIR/${base_name}.md"
            log_success "Copied $filename as ${base_name}.md"
        fi
        ((copied_count++))
    fi
done

# Copy any images or assets that might be referenced in documentation
if [ -d "$DOCS_DIR/images" ]; then
    if [ "$DRY_RUN" = true ]; then
        log_info "Would copy images directory"
    else
        log_info "Copying images directory..."
        cp -r "$DOCS_DIR/images" "$WIKI_DIR/"
        log_success "Copied images directory"
    fi
fi

if [ -d "$DOCS_DIR/assets" ]; then
    if [ "$DRY_RUN" = true ]; then
        log_info "Would copy assets directory"
    else
        log_info "Copying assets directory..."
        cp -r "$DOCS_DIR/assets" "$WIKI_DIR/"
        log_success "Copied assets directory"
    fi
fi

shopt -u nullglob

log_info "Copied $copied_count documentation files"
if [ $skipped_count -gt 0 ]; then
    log_info "Skipped $skipped_count files"
fi

# Check if there are any changes
if [ "$DRY_RUN" = false ]; then
    cd "$WIKI_DIR"

    if git diff --quiet && git diff --cached --quiet; then
        log_info "No changes detected in wiki"
        cd ..
        exit 0
    fi

    # Show changes
    log_info "Changes detected:"
    git status --porcelain

    # Commit and push changes
    log_info "Committing changes..."

    # Add all changes
    git add .

    # Create commit message with timestamp
    commit_message="Update documentation $(date '+%Y-%m-%d %H:%M:%S')"

    # Get the current version from pyproject.toml if available
    if [ -f "../pyproject.toml" ]; then
        version=$(grep '^version = ' ../pyproject.toml | sed 's/version = "\(.*\)"/\1/')
        if [ ! -z "$version" ]; then
            commit_message="Update documentation for v$version - $(date '+%Y-%m-%d %H:%M:%S')"
        fi
    fi

    git commit -m "$commit_message"

    # Push changes
    log_info "Pushing changes to GitHub Wiki..."
    git push origin main

    if [ $? -eq 0 ]; then
        log_success "Wiki updated successfully!"
        log_info "View your updated wiki at: https://github.com/msadeqsirjani/TubeHarvest/wiki"
    else
        log_error "Failed to push changes to wiki"
        cd ..
        exit 1
    fi

    cd ..
else
    log_info "Would check for changes and commit/push to wiki"
    log_info "Commit message would be: 'Update documentation $(date '+%Y-%m-%d %H:%M:%S')'"
fi

# Cleanup option
if [ "$DRY_RUN" = false ]; then
    read -p "🗑️  Remove local wiki directory? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$WIKI_DIR"
        log_success "Local wiki directory removed"
    else
        log_info "Local wiki directory kept at: $WIKI_DIR"
    fi
else
    # Clean up dry run directory
    if [ -d "$WIKI_DIR" ] && [ "$WIKI_DIR" != "./TubeHarvest.wiki" ]; then
        rm -rf "$WIKI_DIR"
    fi
fi

if [ "$DRY_RUN" = true ]; then
    log_success "Dry run completed! 🎉"
    echo ""
    echo "📋 Summary:"
    echo "   • Found $total_files documentation files"
    echo "   • Would copy $copied_count files"
    if [ $skipped_count -gt 0 ]; then
        echo "   • Would skip $skipped_count files"
    fi
    echo ""
    echo "🚀 To actually sync the wiki, run without --dry-run flag"
else
    log_success "Wiki sync completed! 🎉"
    echo ""
    echo "📚 Next steps:"
    echo "   • Visit the wiki: https://github.com/msadeqsirjani/TubeHarvest/wiki"
    echo "   • Check that all pages display correctly"
    echo "   • Update any internal links if needed"
    echo "   • Share the documentation with users!"
fi 