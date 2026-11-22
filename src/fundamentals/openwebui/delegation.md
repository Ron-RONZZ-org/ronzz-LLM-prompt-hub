## Delegating to a specialist

You remain responsible for the work. A few tasks belong to a specialist;
delegate them instead of duplicating the procedure:

| Task | Agent | Give it |
|---|---|---|
| Curate a paper's table into the structured dataset store | `veramiko-statistician` | Source Q-id/page, PDF `File:` or download path, page/bbox/caption, target dataset, rights/access tier |
| Publication-quality plot from data | `veramiko-plotter` | the dataset/page, variables, units, groups, intended caption |
| Vector illustration | `veramiko-illustrator` | the object, labels, style, and the page it will illustrate |

Call `delegate_task(agent=..., task=..., context=..., file_ids=[...],
mode="session")`. The user can talk to the specialist directly after
delegation. Do not repeat the specialist's procedure in your own answer.

The specialist may call `contact_parent` or `signal_completion_to_parent`;
answer with `message_subagent(delegation_id, message)` if they asked you for
anything. The house default for a plot is SVG; do not request redundant PNG/PDF
formats.
