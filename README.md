# ro-terms
The purpose of this repository is to allow RO-crate users to create their own RO terms without having to create a new namespace, ontologies, etc.

This way, the RO-crate community can ellaborate vocabularies in a collaborative manner. Users may collaborate to a common vocabulary (vocabulary.csv) or create their own terms.

RO crates use the following namespace: 

`https://w3id.org/ro/terms/YOUR_NAMESPACE`

The namespace for the common terms is: 

`https://w3id.org/ro/terms#`

To download the terms in CSV you can do:

`curl -L https://w3id.org/ro/terms`

And if you want them in json-ld:

`curl -H "accept:application/ld+json" -L https://w3id.org/ro/terms > context.json`

## Contribution guidelines
This repository works in a first-come, first-serve basis. To add your own terms, simply:

1) Fork this repository.
2) Add a new folder to reserve your own namespace. Add a `vocabulary.csv` file with your terms and a short README.md file with your name/project and who the maintainer is. For an example, you can see the `example` folder. If you just have a few terms, you can add them to the `common` namespace (just edit the `vocabulary.csv` file at the root level). When adding your terms, please make sure that each term has a label, type, definition and a domain and range if you are defining a property. 
3) Once done, execute the python script to generate a `context.json` file for your terms. You can do so by doing `python .\gen_context.py .\test\ > context.json`. Copy the `context.json` file to your folder.
4) Open a pull request and a maintainer from ro-terms will assess and merge the changes as soon as possible.

## Why are terms collected in a CSV?
We want to quickly allow contributors to be able to understand and explore existing terms and their definitions. From the CSV we can easily create machine-readable versions of the vocabualry.


