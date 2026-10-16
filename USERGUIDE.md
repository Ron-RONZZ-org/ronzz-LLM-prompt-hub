# ronzz.ORG prompt library — user guide

A **prompt** is the instruction you give an AI assistant to tell it what you
want. This library is a shared collection of ready-made prompts for the work we
do at ronzz.ORG — writing and proofreading, research, wiki editing, and software
development. Instead of writing instructions from scratch, open a prompt, copy
it, and adapt it to your task.

You do not need to know anything about programming to use these prompts.

## What you need

An AI assistant to paste the prompt into. At ronzz.ORG that is
**[Open WebUI](https://llm.ronzz.org)** (also reachable as "Veramiko"), but the
prompts are plain text and work in any assistant (ChatGPT, Claude, Gemini, …).

## The easiest way: Open WebUI

1. Sign in at **https://llm.ronzz.org**.
2. Start a new chat.
3. Type **`/`** in the message box — a list of the library's prompts appears.
   Keep typing to filter, then pick one.
4. The prompt is inserted into the message box. **Replace the fill-in markers**
   (see below) and add anything else you want the assistant to know.
5. Press send.

Some prompts come as **Models** instead — specialised assistants with a built-in
role. Switch to one from the model picker at the top of the chat:

| Model | What it is for |
| --- | --- |
| **Veramiko Science** | Scientific research: literature review, analysis, drafting, citations. |
| **RonzzWikiCowriter** | Writing and editing pages on the ronzz wiki (wikibase.ronzz.org). |

## The portable way: copy and paste

Every prompt is plain text, so you can use it anywhere:

1. Open the prompt — from the **online prompt store** (search or browse by
   theme) or from the matching file in this repository.
2. **Copy** the whole prompt.
3. Paste it into your AI assistant, replace the fill-in markers, and send.

## Filling in the markers

Prompts contain markers in double curly brackets, such as:

- `{{TOPIC}}` — the subject you want to work on
- `{{article}}` — where your text should go
- `{{TARGET}}` — what the assistant should act on

Replace the marker **and** its brackets with your own content. If a prompt says
"the attached document", attach the file to your message before sending. Leave
the rest of the prompt as it is — that wording is what makes it work.

## Getting good results

- **Be specific.** The more context you give, the better the answer.
- **Give it the material.** If a prompt asks for a text or a document, provide
  it (paste it in, or attach the file).
- **Iterate.** The first answer is a starting point — reply with what to change
  ("make it shorter", "keep my style", "add sources").
- **Check the facts.** AI assistants can be confidently wrong. Prompts that
  need sources will say so; verify anything important.
- **Stay in your voice.** Prompts such as *proofread* or *rewrite* deliberately
  preserve your own writing style — say so if a change feels wrong.

## Finding the right prompt

- **Online prompt store** — a searchable website listing every prompt, grouped
  by theme, with a one-click copy button.
- **Open WebUI** — type `/` in the chat box to list the slash commands.
- **This repository** — browse the folders under `src/` (each file is the
  source of one prompt).

## Getting help

- Can't find a prompt for your task, or one gives poor results? Ask the
  ronzz.ORG IT team, or see the wiki: https://wikibase.ronzz.org/wiki/RonzzIT:Main
- Want to add or improve a prompt? See **[CONTRIBUTING.md](CONTRIBUTING.md)**.
