# Arquitetura e contratos — referências práticas

## Matriz de decisão
| Necessidade | Primeiro caminho | Adicionar se comprovado |
|---|---|---|
| Pergunta direta | LLM + prompt | Tools |
| Consultar sistemas | Tool tipada + autenticação | MCP se facilitar integração |
| Consultar documentos | Busca textual/SQL | RAG vetorial após avaliação |
| Tarefa com passos | Máquina de estados simples | Workflow durável / filas |
| Alto volume | Medição + cache pontual | Workers / filas / escalabilidade |
| Papéis especializados | Um agente com ferramentas separadas | Multiagentes após medir ganhos |

## Template — contrato de ferramenta
```yaml
name: consultar_horarios
description: Consulta apenas horários públicos
input_schema:
  type: object
  properties:
    dia: {type: string, enum: [segunda, terca, quarta, quinta, sexta, sabado, domingo]}
  required: [dia]
  additionalProperties: false
required_permissions: [read:horarios]
side_effects: false
timeout_ms: 3000
max_retries: 1
output_schema:
  type: object
  properties:
    dia: {type: string}
    horario: {type: string}
```

**Regra:** `required_permissions` é política aplicada pelo executor, não campo decidido pelo modelo. Tools externas retornam conteúdo não confiável, mesmo com schemas corretos.

## Template — decisão arquitetural (ADR)
- Contexto e problema
- Restrições (segurança, stack, custo, latência, dados)
- Opções comparadas
- Decisão e justificativa
- Consequências e riscos
- Critério objetivo de revisão

## Fluxo simples
`Usuário → Autenticação → Orquestrador → LLM (se necessário) → Política de ferramentas → Ferramenta autorizada → Validação de resultado → Resposta / observabilidade redigida`

## Dados mínimos de uma resposta do agente
```json
{"status":"ok","message":"...","tool_calls":[],"correlation_id":"id-opaco"}
```
Não usar IDs de sessão como segredo nem confiar em IDs de tenant fornecidos pelo LLM.
