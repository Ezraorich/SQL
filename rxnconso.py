rxnconso.createTempView("rxnconso")
rxnsat.createTempView("rxnsat")

%sql
create or replace temp view NDC as 
SELECT a.atv as ndc, a.rxcui, a.rxaui,  b.str
FROM rxnsat a, rxnconso b
WHERE a.atn = 'NDC'
AND a.rxaui = b.rxaui
and a.sab = 'RXNORM';

ORDER BY b.str;

%sql
create or replace temp view bla_with_normalised_ndc as
select distinct ndc, a.rxcui, a.rxaui, str, atn from NDC a, rxnsat b
where a.rxcui = b.rxcui
and atn = 'BLA';

select count(distinct ndc) from bla_with_normalised_ndc
