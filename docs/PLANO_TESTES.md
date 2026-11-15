# Plano de verificações do perfil · 15/11/2026

O README é uma apresentação visual pública. O workflow `.github/workflows/verificar-perfil.yml` roda testes **offline** de integridade em pull requests e na `main`.

| Caso | Automatizado | Expectativa |
| --- | --- | --- |
| PERFIL-01 | Sim | Projetos em destaque identificados; não exibir o repositório privado Casa Conceito como público |
| PERFIL-02 | Sim | Cloud Foundations e re/Start na mesma linha centralizada, sem tabela ou mensagens genéricas |
| PERFIL-03 | Sim | `assets/aws-cloud-banner.svg` existe e tem XML SVG válido |
| PERFIL-04 | Sim | Links relativos `./` em `src`/`href` resolvem para arquivos existentes |
| PERFIL-05 | Sim | Diagrama UML documental tem marcadores PlantUML |
| PERFIL-06 | Manual | Conferir existência/validade de credenciais Credly e uso autorizado das imagens |
| PERFIL-07 | Manual | Conferir disponibilidade de links e aparência de imagens externas (shields/estatísticas/ícones) em desktop e mobile |

**Atenção:** um badge renderizado não comprova certificação, nem o teste documental verifica o emissor Credly. O teste preserva o layout e referências, não inventa links de validação. O fluxo não publica site, não modifica projetos destacados e não consulta APIs de terceiros.
