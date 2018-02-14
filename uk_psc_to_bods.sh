#!/bin/sh
exec jq -s . |
jq '[.[]]' |
jq 'group_by(.data.links.self) |
map(
{entity: {identifiers: [{scheme: "GB-COH", id: .[0].company_number }]},
          interestedParty: map(
            if .data.kind == "individual-person-with-significant-control" then 
                {
                  name: .data.name,
                  type: "naturalPerson",
                  nationalities: [.data.nationality]
                 } 
           elif .data.kind == "corporate-entity-person-with-significant-control" then
                {
                    name: .data.name,
                    type: "registeredEntity"
                }
            elif .data.kind == "legal-person-person-with-significant-control" then
                {
                    name: .data.name,
                    type: "legalEntity"
                }
            else
                null end ),
interests: map( {  details: .data.natures_of_control[] } )})' | 
jq 'group_by(.entity.identifiers[].id) | map(
{statementGroup: {
beneficialOwnershipStatements: [.[]]
}})'