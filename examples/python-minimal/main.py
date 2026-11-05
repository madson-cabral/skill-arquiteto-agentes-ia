"""Demonstração determinística de execução de ferramentas; NÃO usa LLM."""
from dataclasses import dataclass
from typing import Mapping

HORARIOS: Mapping[str, str] = {"terca": "19:30", "domingo": "19:00"}


@dataclass(frozen=True)
class ToolResult:
    status: str
    message: str


def consultar_horario(dia: str, permissions: frozenset[str]) -> ToolResult:
    """Exemplo de validação de entrada e autorização no executor."""
    if "read:horarios" not in permissions:
        return ToolResult("forbidden", "Sem autorização para consultar horários.")
    if not isinstance(dia, str) or dia not in HORARIOS:
        return ToolResult("invalid_input", "Dia inválido ou não cadastrado.")
    return ToolResult("ok", f"Horário de {dia}: {HORARIOS[dia]}.")


def executar(pergunta: str, permissions: frozenset[str], max_steps: int = 1) -> ToolResult:
    """Roteamento de demonstração, sem inferência de modelo ou rede."""
    if max_steps < 1:
        return ToolResult("limit_exceeded", "Limite de execução atingido.")
    texto = pergunta.lower()
    dia = next((d for d in HORARIOS if d in texto), None)
    if dia is None:
        return ToolResult("unsupported", "Pergunta não reconhecida nesta demonstração.")
    return consultar_horario(dia, permissions)


if __name__ == "__main__":
    print(executar("Qual é o horário de terça (terca)?", frozenset({"read:horarios"})))
