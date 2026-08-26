ronzz.ORG runs its own infrastructure. Know your environment:

- **Internal IT docs**: https://wikibase.ronzz.org/wiki/RonzzIT:Main (gated to the `it` user group; read via the `mediawiki-mcp-server` MCP tools, e.g. `mediawiki-mcp-server_get-page`).
- **Services**: Nextcloud (dashboard.ronzz.org) · Wikibase + WDQS (wikibase.ronzz.org) · Forgejo (forgejo.ronzz.org) · Hesk (threads.ronzz.org) · SnappyMail (webmail.ronzz.org) · Open WebUI (llm.ronzz.org) · mailwatch (spam idler) · main server (ronzz-linux-server-2, an OCI VPS).
- **Git hosting**: Forgejo (`forgejo.ronzz.org`) is the primary forge and source of truth. GitHub (orgs `Ron-RONZZ-org` / `Rong-Zhou-FR`) is the legacy mirror — CI runs on GitHub Actions and external issue/PR contributions are accepted there, while migration to Forgejo is in progress.
- **Machines**: `ronzz-linux-xxx` desktop machines and the main server. Desktop machines mount the Nextcloud shared space at `~/shared-ronzz-nextcloud`; the IT doc pointer lives at `~/shared-ronzz-nextcloud/docs/IT`.
- **Code agents**: opencode is the officially-recommended desktop coding client at ronzz.ORG (this AGENTS.md is its system instruction). Open WebUI (llm.ronzz.org) is the hosted chat UI for non-coding use.
- **Wiki is the single source of truth** for IT operations; runbooks live in the `RonzzIT:` namespace. Update wiki pages there, never local copies.
