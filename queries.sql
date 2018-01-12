select tipo, ano, sum(valor) as total from despesa group by tipo, ano order by tipo ASC, ano ASC; #tipo_ano_total
select tipo, ano, mes, sum(valor) as total from despesa group by tipo, ano, mes order by tipo ASC, ano ASC, mes ASC; #tipo_ano_mes_total
select deputado, tipo, sum(valor) as total from despesa group by deputado, tipo order by deputado ASC; #deputado_tipo_total
select deputado, tipo, ano, sum(valor) as total from despesa group by deputado, tipo, ano order by deputado ASC, ano ASC; #deputado_tipo_ano_total
select deputado, tipo, ano, mes, sum(valor) as total from despesa group by deputado, tipo, ano, mes order by deputado ASC, ano ASC, mes ASC; #deputado_fornecedor_tipo_ano_mes_total
select ano, sum(valor) as total from despesa group by ano order by ano ASC; #ano_valor
select ano, mes, sum(valor) as total from despesa group by ano, mes; #ano_mes_valor
select deputado, fornecedor, tipo, ano, sum(valor) as total from despesa group by deputado, fornecedor, tipo, ano order by deputado ASC, ano ASC; #deputado_tipo_ano_total