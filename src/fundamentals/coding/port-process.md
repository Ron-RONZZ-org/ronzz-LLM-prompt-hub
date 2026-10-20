- **Check before using a port** — Run `ss -tlnp` to verify a port is free before starting any server. Do not assume a port is available.
- **Use a free port** — If the desired port is occupied by a foreign process, pick a different port. Most dev servers accept `--port <N>`. Adjust test-script URLs accordingly.
- **Find a free port dynamically** — Instead of guessing which port is free, allocate one:
  ```bash
  PORT=$(python3 -c "import socket; s=socket.socket(); s.bind(('',0)); print(s.getsockname()[1]); s.close()")
  ```
- **Own cleanup only** — The only time it's acceptable to kill a process on a port is when you are cleaning up a server *you started* in a prior session. Use targeted methods: `fuser -k <port>/tcp` — never `pkill -f` or wildcard `kill`.
- **When in doubt, ask** — If you cannot determine whether a process on a port belongs to you or the user, stop and ask rather than killing it.
