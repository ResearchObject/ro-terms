### Workflow run namespace

Additional terms for the [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) profile.

Maintainer:
- The [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/) working group

* Namespace: <https://w3id.org/ro/terms/workflow-run#>
* Context: [context.jsonld](context.jsonld)
* Terms (CSV): [vocabulary.csv](vocabulary.csv)
* Specification (JSON-LD): [wfrun.jsonld](wfrun.jsonld)
* Specification (Turtle): [wfrun.ttl](wfrun.ttl)
* Specification (nt): [wfrun.nt](wfrun.nt)
* specification (rdf/xml): [wfrun.rdf](wfrun.rdf)

## Content negotiation
If you'd like to get a machine-readable version of the workflow run ro-terms, simply request the corresponding file with its associated header. For example, for a JSON-LD representation:

```
curl -sH "Accept:application/ld+json" -L https://w3id.org/ro/terms/workflow-run#
```

And for a Turtle representation:

```
curl -sH "Accept:text/turtle" -L https://w3id.org/ro/terms/workflow-run#
```


## Terms in detail

<!-- 
For updates to terms, remember to:
- Update below
- Update vocabulary.csv
- Regenerate context.json with gen_context.py
- Add to Profile Crates ro-crate-metadta.json in https://github.com/researchobject/workflow-run-crate/ 
-->

| term | type | label | description | domain | range | 
| -----| ---- | ----- | ----------- | ------ | ----- |
| ParameterConnection | Class | ParameterConnection | A connection between parameters of different applications | | |
| ContainerImage | Class | ContainerImage | A containerization software container image | | |
| DockerImage | Class | DockerImage | A Docker container image | | |
| SIFImage | Class | SIFImage | A Singularity Image Format container image | | |
| connection | Property | connection | A parameter connection created by this workflow | ComputationalWorkflow; HowToStep | ParameterConnection | 
| sourceParameter | Property | sourceParameter | The source (upstream) parameter | ParameterConnection | FormalParameter | 
| targetParameter | Property | targetParameter | The target (downstream) parameter | ParameterConnection | FormalParameter | 
| md5 | Property | md5 | md5 checksum as a hexadecimal string | File ContainerImage | Text | 
| sha1 | Property | sha1 | sha1 checksum as a hexadecimal string | File ContainerImage | Text | 
| sha256 | Property | sha256 | sha256 checksum as a hexadecimal string | File ContainerImage | Text | 
| sha512 | Property | sha512 | sha512 checksum as a hexadecimal string | File ContainerImage | Text | 
| environment | Property | environment | environment variables used by the application | SoftwareApplication SoftwareSourceCode ComputationalWorkflow CreateAction | FormalParameter PropertyValue | 
| registry | Property | registry | A service to register software products, such as container images | ContainerImage | Text | 
| tag | Property | tag | A tag assigned to a software product, such as a container image | ContainerImage | Text | 
| containerImage | Property | containerImage | A container image associated with this entity | CreateAction | ContainerImage URL |
| resourceUsage | Property | resourceUsage | A resource usage item, such as peak memory | CreateAction | PropertyValue |
