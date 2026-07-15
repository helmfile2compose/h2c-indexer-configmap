"""ConfigMap indexer — populates ctx.configmaps."""

from dekube import ConverterResult, IndexerConverter  # pylint: disable=import-error  # h2c resolves at runtime


class ConfigMapIndexer(IndexerConverter):  # pylint: disable=too-few-public-methods  # contract: one class, one method
    """Index ConfigMap manifests by name for volume/env resolution."""
    name = "configmap"
    kinds = ["ConfigMap"]

    def convert(self, _kind, manifests, ctx):
        """Index ConfigMap manifests into ctx.configmaps."""
        for m in manifests:
            if not m:
                continue
            meta = m.get("metadata") or {}
            name = meta.get("name", "")
            if name:
                ctx.configmaps[name] = m
        return ConverterResult()
