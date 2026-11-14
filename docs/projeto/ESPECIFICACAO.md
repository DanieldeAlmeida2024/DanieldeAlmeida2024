# Perfil GitHub — portfólio público, certificações e visualizações

**1.0.0** · 11/11/2026 · código `1897b6fec6cd693a4008dea9715f466c533963ea`. Levantamento documental; cenários ainda exigem execução visual/funcional.

## Contexto, componentes e requisitos
O repositório `DanieldeAlmeida2024/DanieldeAlmeida2024` **não é uma API**, mas a página de apresentação renderizada pelo GitHub no perfil. Seu `README.md` reúne cabeçalho dark por `capsule-render.vercel.app`, links LinkedIn/GitHub/e-mail, texto animado por `readme-typing-svg.demolab.com`, ícones por `skillicons.dev`, painéis estatísticos de `github-readme-stats.vercel.app` e atividade via `github-readme-activity-graph.vercel.app`.

O conteúdo principal é uma apresentação informal, seleção de projetos com links e certificações AWS em destaque, incluindo dois arquivos de badge em `images.credly.com`. O README histórico contém **o mesmo link de verificação Credly para as duas imagens**; preservar as imagens e a atribuição de AWS Cloud Foundations, mas solicitar validação individual da URL do segundo selo antes de afirmar que ambos representam credenciais distintas. O conteúdo não deve divulgar renda, documentos ou dados privados; apresentar apenas experiências e links publicamente relevantes.

O GitHub aceita Markdown, HTML seguro, imagens externas e `<details>`, mas não executa JavaScript arbitrário nem um aplicativo dinâmico no README. Os gráficos dependem da disponibilidade de serviços externos; se caírem, o conteúdo textual e os links devem continuar úteis. O perfil não tem backend, banco de dados ou suite de aplicação; UML aqui modela **fluxo editorial e dependências de conteúdo**, não entidades inventadas.

Qualquer ajuste de estilo deve respeitar tom de voz simples, links atuais e badges AWS; um PR de revisão deve mostrar screenshots de desktop/mobile da renderização real do Markdown e registrar o commit publicado.

## Verificação
```bash
python -m unittest discover -s tests -v
```

Para rastreabilidade, consulte os [diagramas UML](../uml/README.md), a [matriz de testes](../testes/PLANO_DE_TESTES.md) e o [versionamento](../controle/VERSIONAMENTO.md).
