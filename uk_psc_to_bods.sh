#!/bin/sh
exec jq -s . |
jq '[.[]]' |
jq 'group_by(.data.links.self) |
map(
{entity: {identifiers: [{scheme: "GB-COH", id: .[0].company_number }]}, 
interestedParty: 
    {
        name: .[].data.name,
        type: map(if .data.kind == "individual-person-with-significant-control"
                  	then "naturalPerson"
                  elif .data.kind == "corporate-entity-person-with-significant-control"
                  	then "registeredEntity"
                  elif .data.kind == "legal-person-person-with-significant-control"  
        		  then "legalEntity" else null end),
        nationalities: [.[].data.nationality]
    },
interests: map( {  details: .data.natures_of_control[] } )})' | 
jq 'group_by(.entity.identifiers[].id) | map(
{statementGroup: {
beneficialOwnershipStatements: [.[]]
}})'