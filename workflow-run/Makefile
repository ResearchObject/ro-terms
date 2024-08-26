## Assumes Apache Jena's Riot installed on path
#RIOT="riot" 
## Assumes Docker is installed on path
RIOT=docker run -v `pwd`:/rdf docker.io/stain/jena:5.1.0 riot

all: clean wfrun.rdf wfrun.nt wfrun.jsonld

clean:
	rm -f wfrun.rdf wfrun.nt wfrun.jsonld

wfrun.rdf: wfrun.ttl
	${RIOT} --formatted=rdfxml wfrun.ttl > wfrun.rdf

wfrun.nt: wfrun.ttl
	${RIOT} --formatted=nt wfrun.ttl > wfrun.nt

wfrun.jsonld: wfrun.ttl
	${RIOT} --formatted=jsonld wfrun.ttl > wfrun.jsonld


