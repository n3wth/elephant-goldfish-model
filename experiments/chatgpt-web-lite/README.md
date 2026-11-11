# EGM Lite web preview

This isolated skills-only plugin tests a document-first EGM workflow in web chat hosts. It is separate from the published desktop EGM plugin: it does not change `plugin.json`, the canonical `skills/` directory, or the normal plugin packager.

The `/egm-lite` skill supports idea shaping, planning, and document review using chat context and user-provided attachments. A connected Drive app may be used only when the host makes it available and the user chooses it. The experiment does not add OAuth, a hosted MCP server, shell access, or independent Goldfish reviewers. Any adversarial pass is labeled as same-context critique.

To test, package this directory as its own plugin and install it privately in a web host. Check that the skill is available, try an idea prompt and an attached-document review, and confirm the responses do not claim independent review or access to unavailable files.
