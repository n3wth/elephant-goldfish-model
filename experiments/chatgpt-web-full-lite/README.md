# EGM full + Lite web preview

This private test package combines the seven canonical EGM skills with the separate `egm-lite` skill. It is built from the repository's current full-skill sources and is not included in the normal desktop plugin build.

The test manifest omits `requires_local_executor` so ChatGPT Work can show what it discovers. It does not make shell access, repository files, or independent subagents available. Full workflows must stop or explain their limits when the host lacks those capabilities. `egm-lite` remains the document-first path for idea shaping, plans, and reviews, and labels critique as same-context.

Build a clean archive with:

```sh
python3 experiments/chatgpt-web-full-lite/pack.py --output /tmp/egm-full-lite
```

Upload `/tmp/egm-full-lite/egm-full-lite-preview.zip` as a private plugin. The builder calls the normal OpenAI packager, overlays this test manifest and the Lite skill, and drops the desktop-only `.codex-plugin` host manifest from the web test archive.

## ChatGPT Work check

The private preview exposed all eight skills in its plugin listing. The full brainstorm skill started and asked its first clarifying question. The Lite prompt produced a short book-swap pilot plan and labeled its critique as same-context. This did not verify file creation or an independent reviewer run; those capabilities need a separate test in a host that exposes them.
