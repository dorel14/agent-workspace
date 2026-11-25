# agent-workspace

Hermes plugin that makes an agent's workspace folder easily configurable via the **dashboard "Plugins & Tools" UI**.

## What it does

1. Declares a `workspace_folder` setting (string) in `config_schema`.
2. The dashboard renders this as a text field in **Plugins & Tools → agent-workspace → Settings**.
3. When you set a path and click **Save**, the plugin loads on next Hermes start (or immediately in development) and **applies it to `terminal.cwd` in your profile's `config.yaml`**.

## Install

```bash
# From GitHub (after publishing)
hermes plugins install <your-org>/agent-workspace

# Or locally during development
hermes plugins install /path/to/agent-workspace
```

## Enable for a profile

```bash
# Enable for the current profile
hermes plugins enable agent-workspace

# Or for a specific agent profile (e.g., lina)
hermes plugins enable agent-workspace --profile lina
```

## Usage

1. Open the Hermes dashboard → **Plugins & Tools** → find **agent-workspace** → **Settings**.
2. Enter the workspace folder path (e.g., `/opt/data/lina-references`).
3. Click **Save**.
4. Restart Hermes (or the profile's gateway) — the agent's `terminal.cwd` is now set.

## How it works

- Plugin kind: `standalone` (loads in the profile's process).
- On load (`register(ctx)`), reads `workspace_folder` from its settings.
- If set, calls `hermes_cli.config.save_config()` to update `terminal.cwd` in the profile's config.yaml.
- Uses `merge_existing=True` to preserve all other config sections.

## Config schema

```yaml
config_schema:
  workspace_folder:
    type: string
    required: false
    description: "Workspace folder for this agent profile. When set, updates terminal.cwd. Leave empty to disable."
```

## Supported types

Dashboard renders these types:
- `string` — text input
- `boolean` — checkbox
- `number` — numeric input
- `enum` — dropdown (add `enum: [...]` to spec)
- `json` — textarea (JSON)
- `secret` — password field (stored encrypted)

## Development

```bash
# Test locally (from plugin dir)
cd /opt/data/plugins/agent-workspace
# Edit __init__.py, then restart Hermes to reload
```
