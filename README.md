# dekube-indexer-configmap

ConfigMap indexer for [dekube](https://dekube.io) — indexes ConfigMap manifests into `ctx.configmaps` for volume/env resolution.

**The Librarian** — one of the Eight Monks, the founding extensions of the helmfile2compose distribution.

> Heresy level: 0/10 — a faithful scribe, nothing more.

## Type

`IndexerConverter` (priority 50)

## Kinds

- `ConfigMap`

## Install

Via [dekube-manager](https://github.com/dekubeio/dekube-manager):

```sh
python3 dekube-manager.py configmap-indexer
```

Or listed in `distribution.json` — installed automatically when building a distribution.
