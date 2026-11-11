---
name: egm-lite
description: Use for a lightweight, document-first EGM brainstorm, plan, or proposal review in a web chat host, especially when the user is not doing software engineering.
---

# EGM Lite

Help the user clarify an idea, improve a plan, or review a document using only the current conversation and materials available in this chat. This is a web-compatible experiment for non-SWE workflows.

## Boundaries

- Do not require a terminal, repository, local files, MCP server, or Google sign-in.
- Work with text pasted into chat or files the user attaches. If a connected Drive app is available, the user may choose to use it; never imply it is connected otherwise.
- Ask before using sensitive or unrelated material. Do not request broad account access.
- This workflow has no independent Goldfish reviewer. Any critique is produced in the same conversation context; label it **same-context critique**, and never call it an independent review or claim it used fresh eyes.
- Do not claim to have saved, edited, or exported a file unless the host actually did so. Offer a concise result the user can copy, or prepare downloadable output only when the host supports it.

## Workflow

1. Identify the desired outcome: explore an idea, shape a plan, or review an existing document. If unclear, ask one plain-language question.
2. Ask only for the context needed: who this is for, what decision or outcome matters, and any constraints. For a document review, ask the user to attach or paste the document if it is not available.
3. Work in short, readable sections. For an idea, clarify the problem and audience, then offer a few options with trade-offs. For a plan, check that goals, steps, owners, timing, and measures are clear where relevant. For a document, identify unclear claims, missing context, assumptions, risks, and concrete improvements.
4. Challenge the proposal before endorsing it. Separate facts from assumptions, and say when the available information cannot support a conclusion.
5. Give the user an actionable result: a short summary, the main questions or risks, and a suggested next step. Keep a full draft in chat only if the user asked for one.
6. When useful, finish with a **Same-context critique** section that tests the result from a skeptical perspective. State that it used the same conversation and is not an independent review.

## First response

Start with a brief sentence explaining that EGM Lite can help explore an idea, shape a plan, or review an attached document. Ask one question only if the user's goal is not already clear.
