# CLAUDE.md - AI Assistant Guidelines for Lucas PropFirm

## Project Overview

**Lucas PropFirm** is a static promotional landing page for affiliate marketing of Phidias Propfirm (a prop trading firm). The site promotes prop trading accounts and encourages sign-ups using the affiliate code "LUCAS".

- **Type**: Static single-page website
- **Language**: French (targeting French-speaking audience)
- **Purpose**: Affiliate marketing landing page with promotional content

## Repository Structure

```
lucaspropfirm/
├── lucas-propfirm-site.html   # Complete website (HTML + CSS + JS)
├── CLAUDE.md                   # This file
└── .git/                       # Git repository metadata
```

This is an ultra-minimal repository with all code contained in a single HTML file (~920 lines).

## Technology Stack

| Technology | Usage |
|------------|-------|
| **HTML5** | Semantic document structure |
| **CSS3** | Embedded styles (~620 lines) |
| **Vanilla JavaScript** | Embedded scripts (~55 lines) |
| **No Dependencies** | Zero external libraries or frameworks |
| **No Build System** | Direct file editing, no compilation |

### Key Browser Features Used
- CSS Grid and Flexbox layouts
- CSS animations and keyframes
- CSS gradients (linear and radial)
- Backdrop filters
- Intersection Observer API
- Clipboard API
- Media queries for responsiveness

## Development Workflow

### No Build Process Required
This project has no build system, package manager, or development dependencies. Development is straightforward:

1. Edit `lucas-propfirm-site.html` directly
2. Open the file in a browser to preview changes
3. Commit changes to git
4. Deploy by copying the HTML file to the hosting server

### Testing Changes
- Open `lucas-propfirm-site.html` in a browser
- Test responsiveness by resizing the browser window (breakpoint at 768px)
- Verify all interactive features work:
  - Smooth scroll navigation
  - Copy-to-clipboard for affiliate code
  - Scroll-triggered animations

## Code Conventions

### HTML Structure
- **Semantic HTML5**: Uses `<header>`, `<nav>`, `<section>`, `<footer>`
- **BEM-inspired classes**: `.nav-links`, `.feature-card`, `.account-card`
- **French anchor IDs**: `#accueil`, `#avantages`, `#comptes`, `#contact`

### CSS Conventions
- **Mobile-first responsive design**
- **Breakpoint**: 768px for mobile/desktop switch
- **Color palette**:
  - Primary gold: `#FFD700`
  - Orange accent: `#FFA500`
  - Sky blue: `#87CEEB`
  - Dark backgrounds: `#0a0a0a`, `#1a1a2e`, `#16213e`
- **Design patterns**: Card-based layouts, gradient overlays, hover effects

### JavaScript Conventions
- **Vanilla JavaScript only** (no jQuery or frameworks)
- **Modern syntax**: Arrow functions, template literals
- **Performance-optimized**: Intersection Observer for scroll animations
- **Event-driven**: Listeners for user interactions

## Page Sections

1. **Header/Navigation**: Sticky navbar with logo and navigation links
2. **Hero Section**: Main CTA with affiliate code display
3. **Partner Badge**: Phidias Propfirm branding
4. **Promo Section**: Winter Launch Sale promotional content
5. **Features Section**: 6 feature cards highlighting benefits
6. **Stats Section**: 4 statistics about Phidias
7. **Account Options**: 3 account type cards (Static 25K, Fundamental, Swing)
8. **CTA Section**: Final call-to-action
9. **Footer**: Branding and copyright

## Key Interactive Features

### 1. Smooth Scroll Navigation
Anchor links (`<a href="#section">`) scroll smoothly to their targets.

### 2. Copy-to-Clipboard
Clicking the affiliate code box copies "LUCAS" to clipboard with visual feedback ("COPIÉ ✓").

### 3. Scroll Animations
Elements fade in and slide up when scrolling into view using Intersection Observer.

## Important Files and Line References

| Feature | Location |
|---------|----------|
| CSS Styles | `lucas-propfirm-site.html:7-625` |
| HTML Content | `lucas-propfirm-site.html:627-860` |
| JavaScript | `lucas-propfirm-site.html:862-917` |
| Smooth Scroll | `lucas-propfirm-site.html:865-873` |
| Scroll Animations | `lucas-propfirm-site.html:875-894` |
| Clipboard Copy | `lucas-propfirm-site.html:896-916` |

## Affiliate Marketing Details

- **Affiliate Code**: LUCAS
- **Partner**: Phidias Propfirm
- **External Links**: All CTAs link to `https://phidiaspropfirm.com/product-category/comptes/?ref=LUCAS`
- **Promotional Period**: Winter Launch Sale (dates specified in content)

## Making Changes

### Adding New Sections
1. Add HTML structure in the appropriate location (lines 627-860)
2. Add corresponding CSS styles in the `<style>` tag (lines 7-625)
3. If interactive, add JavaScript in the `<script>` tag (lines 862-917)

### Modifying Styles
- All CSS is in a single `<style>` block at the top of the document
- Maintain the existing color palette for consistency
- Test responsiveness at 768px breakpoint

### Updating Content
- Promotional dates and percentages are in the promo section
- The affiliate code "LUCAS" appears in multiple locations - search and replace all instances if changing

## Deployment

This is a static site with no server-side requirements:
1. Upload `lucas-propfirm-site.html` to any web server or static hosting
2. No build step required
3. No environment variables or configuration needed

## Git Workflow

- **Main development**: Direct commits to feature branches
- **No CI/CD**: Manual deployment
- **Commit messages**: Descriptive of changes made

## Notes for AI Assistants

1. **Single file architecture**: All changes go in `lucas-propfirm-site.html`
2. **No package.json**: Don't suggest npm commands
3. **No TypeScript**: Pure JavaScript only
4. **French content**: Maintain French language for all user-facing text
5. **Affiliate integrity**: Don't modify affiliate code or external links without explicit request
6. **Mobile-first**: Test changes for both mobile and desktop views
7. **Performance**: Keep the site lightweight - avoid adding external dependencies
