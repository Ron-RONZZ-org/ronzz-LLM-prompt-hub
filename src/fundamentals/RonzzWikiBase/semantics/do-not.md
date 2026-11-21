## Do not

- Do not invent metadata, identifiers, Q-ids or property ids. If a field is unknown, leave it blank and say so.
- Do not create an item that already exists under another label: search the authority id first.
- Do not use `confirmDuplicate` to force a create; it produces a second item for the same entity.
- Do not silently overwrite or remove an existing statement; show the change and let the user confirm.
