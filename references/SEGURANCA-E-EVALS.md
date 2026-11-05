# Segurança e avaliação de agentes — checklist operacional

## Proteção antes de diagnóstico
Antes de solicitar qualquer log, print, comando, arquivo ou configuração que possa revelar segredos: avisar sobre o risco; fornecer comando que mostre só presença/ausência, tipos ou nomes seguros, sem valores. Nunca pedir dumps de ambientes, tokens, cookies, cabeçalhos Authorization ou `.env` completos.

## Superfícies de ameaça
- Prompt injection de usuário, web, e-mail, documento, ferramenta ou servidor MCP. Tratar material externo como dado, nunca instrução com privilégio.
- Exfiltração via ferramenta, URL, log, webhook, storage, e-mail e output format. Bloquear destinos não autorizados por política de rede/permissão.
- Confusão entre tenants ou sessões. Vincular consultas ao tenant autenticado no backend; não confiar em tenant ID escolhido pelo LLM.
- Execução de comandos/código. Usar sandbox com isolamento de rede e arquivos, limites de recursos e aprovação explícita, não apenas um prompt de aviso.
- Ações de escrita. Confirmação humana, escopo mínimo, token de aprovação de uso único quando apropriado, idempotency key, auditoria e rollback quando possível.
- Custos/loops. Máximo de passos, timeouts, retries com backoff, quotas e circuit breaker; falhar de forma controlada.
- Dados pessoais. Minimização, consentimento/base legal, acesso, retenção, exclusão e logs redigidos.

## Bateria mínima de avaliação
1. **Caminho feliz:** resposta baseada em dados confiáveis e chamada de ferramenta correta.
2. **Entrada inválida:** argumentos rejeitados antes de invocar integração externa.
3. **Injection adversarial:** conteúdo externo pede ações fora do escopo; agente não as executa.
4. **Falha de tool:** timeout/erro do provedor gera resposta controlada e sem detalhes secretos.
5. **Sem autorização:** operação crítica é bloqueada sem aprovação efetiva.
6. **Isolamento:** tenant A não pode consultar/gravar dados de tenant B.
7. **Budget:** limite de passos, tokens ou custo evita repetição indefinida.

## Registro de resultados
Por avaliação: ID, caso, entrada sintética, resultado esperado, resultado real, status, evidência e data. Não usar dados reais sensíveis em fixtures. Separar suites unitárias de evals probabilísticos; para saídas de LLM, usar medidas e limiares com amostras representativas.

## Portões de produção
Confirmar escopo de permissões, limites, proteção de segredos, observabilidade redigida, teste de falha, plano de recuperação, segregação entre ambientes e política para incidentes. Não fazer deploy sem autorização explícita.
