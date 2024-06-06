"""\
Parse a CSV namespace and generate the corresponding JSON-LD context.
"""

import argparse
import csv
import json
import sys
from pathlib import Path


RO_CRATE_VERSION = "1.1"
RO_TERMS_PREFIX = "https://w3id.org/ro/terms"
VOCAB_FN = "vocabulary.csv"


def build_context(namespace, vocab_path, ro_crate_version=RO_CRATE_VERSION):
    ro_crate_context = f"https://w3id.org/ro/crate/{ro_crate_version}/context"
    add_terms = {}
    with open(vocab_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not "term" in row:
                raise RuntimeError("Unexpected keys in CSV %s, try: term,type,label,description,domain,range" % row.keys())
            k = row["term"]
            if not k:
                continue # empty line!
            add_terms[k] = f"{RO_TERMS_PREFIX}/{namespace}#{k}"
    return {"@context": [ro_crate_context, add_terms]}


def main(args):
    ns_dir = Path(args.ns_dir)
    vocab_path = ns_dir / VOCAB_FN
    if not vocab_path.is_file():
        raise RuntimeError(f"{vocab_path} not found")
    context = build_context(ns_dir.name, vocab_path,
                            ro_crate_version=args.ro_crate_version)
    if not args.output:
        args.output = ns_dir / "context.jsonld"
    with open(args.output, "wt", encoding="utf8") as f:
        json.dump(context, f, ensure_ascii=False, indent=4, sort_keys=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ns_dir", metavar="NAMESPACE", help="namespace dir")
    parser.add_argument("-v", "--ro-crate-version", metavar="string",
                        default=RO_CRATE_VERSION, help="RO-Crate version")
    parser.add_argument('-o', '--output', metavar="FILE")
    main(parser.parse_args(sys.argv[1:]))
