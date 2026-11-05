# 🧠 Arquiteto de Agentes de IA — Skill v2.0.0

Skill para orientar GPTs e agentes compatíveis no **projeto, implementação, ensino, evolução e auditoria** de sistemas de IA em Python e TypeScript.

**Novidades v2.0:** arquitetura proporcional ao problema, MCP e function calling, RAG opcional, multiagentes quando justificados, guardrails por código, validação de ferramentas, política de aprovação humana, observabilidade, evals e exemplos demonstrativos executáveis.

## Comece aqui
1. Leia `SKILL.md` (instrução operacional).
2. Consulte `GUIA-DE-USO.md` (instalação e exemplos).
3. Veja `references/` (segurança e decisões arquiteturais).
4. Execute os exemplos de `examples/` (demonstrações **sem LLM real**).

## Princípio
**Não adicionar complexidade que o problema não exige.** Segurança e permissões devem existir no código e infraestrutura, não somente em prompts.

## Diferenças da v1.0
- Mais detalhe em MCP, RAG, multiagentes e contratos.
- Checklist de segurança e sete cenários mínimos de avaliação.
- Exemplos Python e TypeScript separados, com execução e escopo explícitos.
- Regras de compatibilidade, custo, privacidade e aprovação humana.

## Limitação
A skill não fornece contas, chaves API, acesso a ferramentas ou instalação automática em GPTs personalizados. O código de exemplo não integra um provedor LLM: demonstra controles de arquitetura sem dependências de nuvem.

## Autor
Madson Cabral

## Licença
MIT. Consulte `LICENSE`.
