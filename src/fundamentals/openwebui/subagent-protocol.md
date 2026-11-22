## Subagent protocol

Other agents may call you as a subagent, in this case,

- use `contact_parent(message)` when you need clarification or missing data. Group your requests to minimise disturbance to the calling agent.
- end with `signal_completion_to_parent(message)` containing the `File:` title, the `[[File:…]]`/embed snippet, and any caveat. It does not wake the parent; it enters its context on its next turn.
- If the user asks for more work after you have called signal_completion_to_parent, signal completion again once you are done and user validates.
