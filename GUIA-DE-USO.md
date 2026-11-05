# Guia de uso — Arquiteto de Agentes de IA v2.0

## O que está incluído
- `SKILL.md`: instruções do agente arquiteto.
- `references/`: decisões de arquitetura, segurança e avaliações.
- `examples/python-minimal/`: exemplo com ferramenta de consulta determinística; testes locais.
- `examples/typescript-minimal/`: exemplo TypeScript de controle de ferramenta.

## Instalação
**Ambiente com suporte nativo a skills:** copie a pasta inteira para o local previsto pela documentação da ferramenta; a presença de `SKILL.md` não garante ativação automática em qualquer produto.

**GPT personalizado no ChatGPT:** use as regras do `SKILL.md` no campo de Instruções e, se conveniente, anexe os arquivos de referência ao Conhecimento. Um anexo de Conhecimento não instala uma skill nativa; o acesso a arquivos e ferramentas depende das capacidades do GPT.

**Outro assistente:** forneça `SKILL.md` como instrução de operação e os documentos de `references/` como material auxiliar. Ajuste a configuração de acordo com os limites do ambiente.

## Prompts de utilização
- "Atue com a Skill Arquiteto de Agentes de IA v2.0. Projete um agente Python para horários de cultos, sem banco de dados, e explique decisões."
- "Implemente o scaffold TypeScript de um agente com tools autorizadas; evite serviços desnecessários."
- "Audite o meu agente quanto a isolamento entre usuários, vazamento de dados, prompt injection e custos. Não modifique código."
- "Compare um agente único e multiagentes para este caso; use critérios objetivos."

## Exemplo Python
```bash
cd examples/python-minimal
python3 main.py
python3 -m unittest discover -s tests -v
```
Não precisa de chave de API. Mostra contratos, validação e autorização **sem chamar um LLM**.

## Exemplo TypeScript
```bash
cd examples/typescript-minimal
npm install
npm run build
npm start
```
Requer Node.js e acesso ao pacote `typescript` para a instalação inicial. Também não chama LLM.

## Publicar no GitHub
Crie a release `v2.0.0` preservando o histórico da `v1.0.0`. Anexe o ZIP e registre mudanças no changelog. Revise antes de publicar.
