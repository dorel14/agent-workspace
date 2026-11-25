"""agent-workspace plugin — sets terminal.cwd from dashboard config."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def register(ctx) -> None:
    """Called when plugin loads. Applies workspace_folder to terminal.cwd."""
    folder = ctx.get_config("workspace_folder")
    if not folder:
        # No workspace configured — nothing to do
        return

    folder = folder.strip()
    if not folder:
        # Empty string = explicitly cleared
        log.info("agent-workspace: workspace_folder is empty, skipping")
        return

    try:
        from hermes_cli import config as config_mod
    except Exception as exc:
        log.error("agent-workspace: failed to import config module: %s", exc)
        return

    try:
        # Load full profile config, modify terminal.cwd, save back
        config = config_mod.load_config()
        config.setdefault("terminal", {})["cwd"] = folder
        config_mod.save_config(config, merge_existing=True)
        log.info("agent-workspace: applied terminal.cwd = %s", folder)
    except Exception as exc:
        log.error("agent-workspace: failed to save terminal.cwd: %s", exc)
