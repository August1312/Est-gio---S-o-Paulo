faturamento_diario = [10000, 15000, 20000, 25000, 300434, 35000, 150554, 
                       12000, 18000, 22030, 24660, 3200, 40000, 506650, 
                       305433, 31000, 18000, 21000, 2900, 37000, 
                       45050, 26000, 33000, 38000, 3900, 200004, 
                       15000, 22005230, 27044500, 3500, 4000, 257660]

menor_faturamento = min(faturamento_diario)


maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

print(f"Menor faturamento do mês: R${menor_faturamento:.2f}")
print(f"Maior faturamento do mês: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
