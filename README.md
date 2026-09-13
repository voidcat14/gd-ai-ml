# AIChater

AIChater is a self-hosted, provider-agnostic AI chat platform. This repository started as `gd-ai-ml` and is being rebuilt into AIChater incrementally.

## Demo

The web demo is deployed to GitHub Pages. GitHub Pages hosts the frontend only; real model API keys stay on the owner's backend.

## Providers

The planned backend supports:

- OpenRouter
- Anthropic Claude
- Google Gemini
- Ollama
- llama.cpp
- OpenAI-compatible APIs

The server owner chooses the provider, model, endpoint, and API key. Visitors never need the owner's secret key.

## Architecture

```text
GitHub Pages / Web UI
        |
        v
AIChater API (FastAPI)
        |
        +-- OpenRouter
        +-- Claude
        +-- Gemini
        +-- Ollama
        +-- llama.cpp
        +-- OpenAI-compatible
```

## GitHub Pages

The `site/` directory contains the static demo. `.github/workflows/pages.yml` automatically deploys it on pushes to `master`.

In GitHub, enable **Settings → Pages → Source: GitHub Actions** if Pages is not already enabled for the repository.

## Security

Never put provider API keys in `site/`, frontend JavaScript, GitHub Pages, or any public repository file. Keys belong in the server environment or a server-side secret manager.

## Development

The frontend is plain JavaScript/HTML/CSS for the first demo. The production backend is planned in Python/FastAPI with PostgreSQL and optional C++/CUDA local inference through llama.cpp.
