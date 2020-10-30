"""\
Parse a CSV namespace and generate the corresponding JSON-LD context.
"""

import argparse
import csv
import json
import sys
from pathlib import Path


RO_CRATE_VERSION = "1.1"
RO_CRATE_CONTEXT = f"https://w3id.org/ro/crate/{RO_CRATE_VERSION}/context"
RO_TERMS_PREFIX = "https://w3id.org/ro/terms"
VOCAB_FN = "vocabulary.csv"


def build_context(namespace, vocab_path):
    add_terms = {}
    with open(vocab_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            k = row["term"]
            add_terms[k] = f"{RO_TERMS_PREFIX}/{namespace}#{k}"
    return [RO_CRATE_CONTEXT, add_terms]


def main(args):
    ns_dir = Path(args.ns_dir)
    vocab_path = ns_dir / VOCAB_FN
    if not vocab_path.is_file():
        raise RuntimeError(f"{vocab_path} not found")
    context = build_context(ns_dir.name, vocab_path)
    print(json.dumps(context, indent=4, sort_keys=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ns_dir", metavar="NAMESPACE", help="namespace dir")
    main(parser.parse_args(sys.argv[1:]))
