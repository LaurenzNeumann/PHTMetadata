import rdflib
from rdflib.namespace import RDFS
from rdflib.namespace import SH
from rdflib.namespace import RDF
import argparse

from rdflib.graph import Graph


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Automatically create RDFS definitions from their SHACL counterparts.')
    parser.add_argument('-f','--files',type=str,help='Files containing the shacl definitions',dest='file',required=True,nargs='+')
    args = parser.parse_args()
    filel = args.file
    # Load SHACL definitions    
    graph = rdflib.Graph()
    for file in filel:
        g = Graph()
        g.load(file,format="turtle")
        graph = graph + g
    # The graph which will contain the rfds definition:
    rdfsGraph = rdflib.Graph()
    rdfsGraph.namespace_manager.bind('pht', rdflib.URIRef('https://github.com/LaurenzNeumann/PHTMetadata#'))
    # create RDFS definitions:
    for s,p, classuri in graph.triples((None,SH.targetClass,None)):
        rdfsGraph.add((classuri,RDFS.subClassOf,RDFS.Class))
        # create RDFS property definitions
        for s2,p2,prop in graph.triples((s,SH.property,None)):
            path = next(graph.triples((prop,SH.path,None)),["","",""])[2]
            target = next(graph.triples((prop,SH["class"],None)),["","",None])[2]
            # prevent that xsd datatypes are added as range
            rdfsGraph.add((path,RDF.type,RDF.Property))
            rdfsGraph.add((path,RDFS.domain,classuri))
            if not target == None and not 'xsd' in str(target):
                rdfsGraph.add((path,RDFS.range,target))
    print(rdfsGraph.serialize(format="turtle").decode("UTF-8"))

