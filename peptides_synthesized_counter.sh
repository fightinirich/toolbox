#!/usr/bin/env bash

DB="{PATH_TO_peptide_catalog}.db"
DATE="$(date +%F)"
OUTFILE="peptide_counts_${DATE}.txt"

SQL="SELECT month, SUM(peptide_count) AS total_peptide_count FROM (SELECT strftime('%Y-%m', s.DATE) AS month, s.SYNTHESIS_ID, COUNT(p.PEPTIDE_ID) AS peptide_count FROM synthesis s JOIN peptide_synthesis_junction p ON s.SYNTHESIS_ID = p.SYNTHESIS_ID WHERE s.SUPPLIER LIKE '%{#supplier_name#}%' GROUP BY month, s.SYNTHESIS_ID) GROUP BY month ORDER BY month;"

sqlite3 -header -separator '	' "$DB" "$SQL" > "$OUTFILE"

echo "Wrote counts to: $OUTFILE"
