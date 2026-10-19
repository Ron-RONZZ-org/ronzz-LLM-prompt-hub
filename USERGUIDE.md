# ronzz.ORG prompt library — user guide

A **prompt** is the instruction you give an AI assistant to tell it what you
want. This library is a shared collection of ready-made prompts for the work we
do at ronzz.ORG — writing and proofreading, research, wiki editing, and software
development. Instead of writing instructions from scratch, open a prompt, copy
it, and adapt it to your task.

You do not need to know anything about programming to use these prompts.

## What you need

An AI assistant to paste the prompt into. At ronzz.ORG that is
**[Veramiko](https://llm.ronzz.org)** — but the prompts are plain text and work
in any assistant (ChatGPT, Claude, Gemini, …).

## Prompt store

Browse and search every prompt at **[prompts.ronzz.org](https://prompts.ronzz.org)** —
grouped by theme, with a one-click copy button.

## Veramiko

If you use [Veramiko](https://wikibase.ronzz.org/wiki/RonzzInt:Veramiko/101), prompts from this repo are readily available there. Simply type `/` in a chat to list the prompts.

## Opencode (recommended desktop coding client)

`dist/opencode/` **is** a complete opencode config directory (`AGENTS.md`,
`agents/`, `opencode.jsonc`, `plugins/`). Link your global config to it — every
`git pull` of this repo updates your agent config:

```bash
# one-time setup — everyone at ronzz.ORG is on Linux
git clone https://forgejo.ronzz.org/ronzz-org/ronzz-LLM-prompt-hub.git ~/ronzz-LLM-prompt-hub
ln -s ~/ronzz-LLM-prompt-hub/dist/opencode ~/.config/opencode
```

For the command prompts, see [Generic client](#generic-client).

## Generic client

Every prompt is plain text, so you can use it anywhere:

1. Open the prompt — from the **[online prompt store](https://prompts.ronzz.org)**
   (search or browse by theme) or from the matching file in this repository.
2. **Copy** the whole prompt.
3. Paste it into your AI assistant, replace the fill-in markers, and send.

## Filling in the markers

Prompts contain markers in double curly brackets, such as `{{TOPIC}}`:

Replace the marker **and** its brackets with your own content. If a prompt says
"the attached document", attach the file to your message before sending. Leave
the rest of the prompt as it is — that wording is what makes it work.

## Advice on AI use

- **Be specific.** The more context you give, the better the answer.
- **Give it the material.** If a prompt asks for a text or a document, provide
  it (paste it in, or attach the file).
- **Iterate.** The first answer is a starting point — reply with what to change
  ("make it shorter", "keep my style", "add sources").
- **Check the facts.** AI assistants can be confidently wrong. Prompts that
  need sources will say so; verify anything important.

## Getting help

Raise an issue on the repo. If you are part of the Ronzz.ORG community, you can also contact the IT team.

## Contributing

- Want to add or improve a prompt? See **[CONTRIBUTING.md](https://forgejo.ronzz.org/ronzz-org/ronzz-LLM-prompt-hub/src/branch/main/CONTRIBUTING.md)**.
