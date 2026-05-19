# samadhanmishra.com

Personal site and portfolio for Samadhan Mishra, published via [GitHub Pages](https://pages.github.com/) at [samadhanmishra.com](https://samadhanmishra.com).

## Structure

```
frontend/     React portfolio (source)
blog/         Blog (static HTML)
ai-learning/  AI learning content
portfolio/    Legacy portfolio pages
posts/        Long-form posts
assets/       Shared static assets
```

## Deploy

Pushes to `main` run [.github/workflows/deploy.yml](.github/workflows/deploy.yml), which builds the React app and publishes to GitHub Pages.

**Required (one-time):** In repo **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions** — not “Deploy from branch”. If Source is branch-based, GitHub serves `README.md` at the root instead of the Vite build.

## Local development

```bash
cd frontend
npm install
npm start
```

Production build:

```bash
cd frontend
npm run build
```

Use Node.js 20 LTS. The site is built with **Vite** (not Create React App).
