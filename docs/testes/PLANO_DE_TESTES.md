# Testes — Perfil GitHub — portfólio público, certificações e visualizações

**1.0.0** · 11/11/2026 · código `1897b6fec6cd693a4008dea9715f466c533963ea`. Levantamento documental; cenários ainda exigem execução visual/funcional.

| ID | Verificação | Resultado de aceitação | Evidência |
|---|---|---|---|
| PROFILE-01 | Visualizar README em modo claro e escuro | Texto e links legíveis | A coletar |
| PROFILE-02 | Validar 2 imagens AWS | Imagens e alt presentes e sem substituição | A coletar |
| PROFILE-03 | Verificação Credly por selo | Links correspondem ao badge correto | A coletar |
| PROFILE-04 | Links de projetos | Repositórios existem e destino correto | A coletar |
| PROFILE-05 | Links sociais e mailto | Sem URL quebrada | A coletar |
| PROFILE-06 | Gráficos externos offline | Descrição e links permanecem úteis | A coletar |
| PROFILE-07 | HTML details/summary | Seções expandem corretamente no GitHub | A coletar |
| PROFILE-08 | Renderização mobile 375px | Banner e tabelas sem corte grave | A coletar |
| PROFILE-09 | Acessibilidade de imagens | Alt descritivo nas peças principais | A coletar |
| PROFILE-10 | Nenhum dado sensível | Sem endereço privado, tokens ou CPF | A coletar |
| PROFILE-11 | Linguagem do perfil | Texto simples e sem exageros de experiência | A coletar |
| PROFILE-12 | Atualização de projetos | Informações batem com repositórios reais | A coletar |

## Procedimento de validação
Realizar renderização e testes com navegador/viewport, inspecionar console/rede e salvar screenshot quando aplicável. Validar links públicos com cuidado para não publicar tokens. `tests/test_documentacao.py` cobre apenas a estrutura, não interface ou latência. Registrar SHA, navegador, resolução, entradas e status do teste.
