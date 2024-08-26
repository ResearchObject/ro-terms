## Assumes Apache Jena's Riot installed on path
#RIOT="riot" 
## Assumes Docker is installed on path
RIOT=docker run -v `pwd`:/rdf docker.io/stain/jena:5.1.0 riot

all: clean wfrun.rdf wfrun.nt wfrun.ttl

clean:
	rm -f wfrun.rdf wfrun.nt wfrun.ttl

wfrun.rdf: wfrun.jsonld
	${RIOT} --formatted=rdfxml wfrun.jsonld > wfrun.rdf

wfrun.nt: wfrun.jsonld
	${RIOT} --output=nt wfrun.jsonld > wfrun.nt

wfrun.ttl: wfrun.jsonld
	${RIOT} --formatted=turtle --set ttl:directiveStyle=rdf10 wfrun.jsonld > wfrun.ttl


