import json

faturamento_json = '''
{
    "dias": [100, 200, 0, 50, 300, 400, 150, 0, 120, 500, 0, 250, 100, 150, 0, 0, 200, 450, 600, 0, 300]
}
'''

faturamento = json.loads(faturamento_json)["dias"]

faturamento_filtrado = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)

media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

dias_acima_media = len([valor for valor in faturamento_filtrado if valor > media_mensal])

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Número de dias com faturamento superior à média: {dias_acima_media}")
