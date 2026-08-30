- Define custom error classes in one centralised location (see existing module if already defined)
- **Fatal errors** — always raise with a specific error type and clear message; never use generic exceptions or swallow silently.
- **Non-fatal errors** — never swallow silently (`except: pass` is forbidden). Log at WARNING level with diagnostic context so failures are observable without crashing.
- Examples:   ```
  # BAD — swallowed, invisible
  except: pass

  # BAD — generic, no context
  except Exception: log("error")

  # BAD — fatal error silently downgraded to log
  except ValidationError: log.warning("invalid input")

  # GOOD — fatal, specific, informative
  except ValidationError as e:       raise InvalidConfigError(f"bad value for {key}: {e}")

  # GOOD — non-fatal, logged with context
  except TimeoutError:       log.warning("request to %s timed out after %ds", url, timeout)   ```
