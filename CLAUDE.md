# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Lucas Propfirm is a static landing page website for a trading prop firm affiliate. The site promotes Phidias Propfirm using the affiliate code "LUCAS" and is written entirely in French.

## Project Structure

The entire site is contained in a single file:
- `lucas-propfirm-site.html` - Complete HTML/CSS/JavaScript in one file (no external dependencies)

## Development

This is a static HTML site with no build system, package manager, or external dependencies. All CSS and JavaScript are inline within the HTML file.

**To preview:** Open `lucas-propfirm-site.html` directly in a web browser.

## Architecture Notes

- **Styling:** All CSS is embedded in a `<style>` block in the document head
- **JavaScript:** Vanilla JS at the bottom of the file handles smooth scrolling, scroll-based animations (IntersectionObserver), and clipboard copy functionality
- **Responsive:** Media queries handle mobile layouts (breakpoint at 768px)
- **Animations:** CSS keyframe animations for gradient effects, pulsing elements, and rotating backgrounds
