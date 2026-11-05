/** Demonstração determinística de ferramenta autorizada; não conecta a LLM. */
export type Result = { status: "ok" | "forbidden" | "invalid_input" | "limit_exceeded" | "unsupported"; message: string };
const horarios: Readonly<Record<string, string>> = { terca: "19:30", domingo: "19:00" };
const allowed = new Set(Object.keys(horarios));

export function consultarHorario(dia: string, permissions: ReadonlySet<string>): Result {
  if (!permissions.has("read:horarios")) return { status: "forbidden", message: "Sem autorização." };
  if (!allowed.has(dia)) return { status: "invalid_input", message: "Dia inválido ou não cadastrado." };
  return { status: "ok", message: `Horário de ${dia}: ${horarios[dia]}.` };
}

export function executar(pergunta: string, permissions: ReadonlySet<string>, maxSteps = 1): Result {
  if (maxSteps < 1) return { status: "limit_exceeded", message: "Limite atingido." };
  const dia = Object.keys(horarios).find((item) => pergunta.toLowerCase().includes(item));
  if (!dia) return { status: "unsupported", message: "Pergunta não reconhecida." };
  return consultarHorario(dia, permissions);
}
