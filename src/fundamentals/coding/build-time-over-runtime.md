Shift processing from the browser to the build step whenever the data is known at build time. This is a performance/complexity tradeoff.

**Do at build time:**
- Static data transformations (format conversion, SVG cleaning, image optimization)
- Code that would otherwise run N×M times (charts × visitors)
- Validation, linting, type checking

**Don't force at build time:**
- Features that depend on user context (locale, device, preferences)
- Processing that would significantly complicate the build pipeline
- Optimizations where the runtime cost is negligible and the build-time complexity is high

When in doubt, ask: *"Is this computation per-visitor or per-build?"* If the data is fixed at build time, process it there. If it changes per request, keep it on the client or server.
