# Developer Profile — Mykola Dotsenko

A modern, responsive developer CV and portfolio landing page built with semantic HTML and CSS.

This repository started as my first HTML exercise. It has been deliberately modernized without adding a framework that the project does not need. The result is a lightweight personal site that demonstrates clean markup, responsive layout, accessibility, and pragmatic frontend engineering.

## What it includes

- responsive single-page CV / portfolio layout
- semantic HTML5 structure
- accessible navigation and keyboard focus states
- mobile-first responsive design
- reduced-motion support
- modern CSS using custom properties, Grid, Flexbox, and fluid typography
- selected professional experience
- selected portfolio projects
- direct LinkedIn and GitHub contact paths
- no JavaScript and no runtime dependencies

## Why no framework?

The page is intentionally static.

React, Next.js, or another framework would increase complexity without improving the product. For a personal CV page, HTML and CSS provide the smallest dependency surface, fastest load path, easiest maintenance, and best long-term portability.

## Project structure

```text
.
├── avatar.jpg
├── index.html
├── styles.css
└── README.md
```

## Run locally

No build step is required.

Open `index.html` directly in a browser, or serve the directory with any static web server.

For example:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Accessibility decisions

- semantic landmarks and headings
- skip-to-content link
- visible keyboard focus
- meaningful link text
- no inaccessible fake form controls
- responsive layout without horizontal scrolling
- `prefers-reduced-motion` support
- descriptive image alt text

## Selected projects

- [Pizzeria — React + TypeScript](https://github.com/MykolaDotsenko/Pizzeria-React-Typescript-Project)
- [MovieShelf — Django](https://github.com/MykolaDotsenko/DjangoMovieProject)
- [JunaLippu — Next.js full-stack](https://github.com/MykolaDotsenko/JunaLippu)
- [MoviesAPI — ASP.NET](https://github.com/MykolaDotsenko/MoviesAPI)

## Author

**Mykola Dotsenko**  
Software Engineer — Python / Django, Backend, Data & Integrations

- [GitHub](https://github.com/MykolaDotsenko)
- [LinkedIn](https://www.linkedin.com/in/mykola-dotsenko/)
