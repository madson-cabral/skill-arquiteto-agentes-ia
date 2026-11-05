# 🧠 Arquiteto de Agentes de IA — Skill v2.0.0

## 📥 Download da Skill v2.0.0

**[Baixar Skill Arquiteto de Agentes de IA PRO — v2.0.0](https://github.com/madson-cabral/skill-arquiteto-agentes-ia/releases/download/v2.0.0/skill-arquiteto-agentes-ia-v2.0.0.zip)**

## 📁 Exemplos e documentação

- [Exemplo Python](examples/python-minimal/main.py)
- [Testes Python](examples/python-minimal/tests/test_agent.py)
- [Exemplo TypeScript](examples/typescript-minimal/)
- [Arquitetura e contratos](references/ARQUITETURA-E-CONTRATOS.md)
- [Segurança e avaliações](references/SEGURANCA-E-EVALS.md)

Os exemplos demonstram conceitos de arquitetura e execução de ferramentas sem conexão com modelos de IA reais.

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
