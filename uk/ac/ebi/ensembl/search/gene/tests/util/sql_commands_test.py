create_gene_autocomplete_table = "CREATE TABLE gene_autocomplete " \
                                 "(" \
                                 "  species varchar(255) DEFAULT NULL," \
                                 "  display_label varchar(128) DEFAULT NULL" \
                                 ")"

drop_gene_autocomplete_table = "DROP TABLE IF EXISTS gene_autocomplete"

insert_into_gene_autocomplete_table = "INSERT INTO gene_autocomplete " \
                                      "(species, display_label) " \
                                      "VALUES " \
                                      "(?,?)"

truncate_gene_autocomplete_table = "DELETE FROM gene_autocomplete"

select_all_from_gene_autocomplete_table = "SELECT " \
                                          " species, " \
                                          " display_label " \
                                          "FROM " \
                                          " gene_autocomplete"
