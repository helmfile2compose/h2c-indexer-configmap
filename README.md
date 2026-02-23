# h2c-indexer-configmap

ConfigMap indexer for [helmfile2compose](https://github.com/helmfile2compose/helmfile2compose) — indexes ConfigMap manifests into `ctx.configmaps` for volume/env resolution.

**The Librarian** — one of the Eight Monks, the founding extensions of the helmfile2compose distribution.

> Heresy level: 0/10 — a faithful scribe, nothing more.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `ConfigMap`

## Install

Via [h2c-manager](https://github.com/helmfile2compose/h2c-manager):

```sh
python3 h2c-manager.py configmap-indexer
```

Or listed in `distribution.json` — installed automatically when building a distribution.
