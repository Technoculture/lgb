with matches as (select rowid, distance from relationship_embedding where vss_search (vector_relations, vss_search_params(json(?), ?))) select rowid, edges.source, edges.target, edges.label, edges.attributes, matches.distance from matches join edges on edges.embed_id = matches.rowid ORDER BY distance DESC