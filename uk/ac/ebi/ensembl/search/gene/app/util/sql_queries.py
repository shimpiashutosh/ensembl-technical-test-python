def get_gene_sql(query, species, limit):
    return "SELECT " \
           "  display_label, " \
           "  species " \
           "FROM " \
           "  gene_autocomplete " \
           "WHERE " \
           "  lower(display_label) like lower('{query}%') " \
           "AND " \
           "  lower(species) = lower('{species}') " \
           "ORDER BY " \
           "  display_label ASC " \
           "LIMIT " \
           "  {limit}".format(query=query, species=species, limit=limit)
