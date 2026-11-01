#!/usr/bin/env python3
"""Gera os dados do Painel da Formação ICC a partir de .ai-tutor/ e curriculum.md."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "painel"
SITUACAO = {"not_started": "Não iniciado", "in_progress": "Em andamento", "mastered": "Dominado"}
ITEM = re.compile(r"^- \[[ x]\] \*\*(\d+\.\d+) .+\(`lesson_\w+` / `(topic_\w+)`\)")
FASE = re.compile(r"^### Fase (\d+) — (.+)$")
ENTREGA = re.compile(r"^\*\*Entrega da fase:\*\* (.+)\.$")
SEM_SESSAO = {"sessao": "—", "data": "—", "situacao": "—", "objetivo": "Nenhuma sessão registrada ainda.", "evidencias": 0}


def carregar(nome: str) -> dict:
    return json.loads((ROOT / ".ai-tutor" / nome).read_text(encoding="utf-8"))


def ler_curriculo() -> tuple[list[dict], dict[str, tuple[str, int]]]:
    fases: list[dict] = []
    itens: dict[str, tuple[str, int]] = {}
    for linha in (ROOT / "curriculum.md").read_text(encoding="utf-8").splitlines():
        if casou := FASE.match(linha):
            fases.append({"fase": int(casou[1]), "nome": casou[2], "entrega": ""})
        elif casou := ENTREGA.match(linha):
            fases[-1]["entrega"] = casou[1]
        elif casou := ITEM.match(linha):
            itens[casou[2]] = (casou[1], fases[-1]["fase"])
    return fases, itens


def salvar(nome: str, linhas: list[dict]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(linhas, ensure_ascii=False, indent=2) + "\n"
    (OUT / nome).write_text(texto, encoding="utf-8", newline="\n")


def main() -> None:
    estado = carregar("state.json")
    cards = carregar("cards.json")["cards"]
    fases, itens = ler_curriculo()

    temas = [
        {
            "item": itens[t["topic_id"]][0],
            "fase": itens[t["topic_id"]][1],
            "tema": t["name"],
            "dominio": t["mastery"],
            "situacao": SITUACAO[t["status"]],
            "evidencias": len(t["evidence_ids"]),
        }
        for t in estado["topics"]
    ]
    for fase in fases:
        da_fase = [t for t in temas if t["fase"] == fase["fase"]]
        fase["temas"] = len(da_fase)
        fase["concluidos"] = sum(t["dominio"] >= 80 for t in da_fase)
        fase["dominio_medio"] = round(sum(t["dominio"] for t in da_fase) / len(da_fase))

    sessoes = [
        {
            "sessao": s["session_id"],
            "data": s["started_at"][:10],
            "situacao": s["status"],
            "objetivo": s.get("objective", ""),
            "evidencias": len(s.get("evidence_ids", [])),
        }
        for s in reversed(estado["sessions"])
    ]
    foco = next((t for t in estado["topics"] if t["mastery"] < 80), None)
    resumo = [{
        "temas": len(temas),
        "concluidos": sum(t["dominio"] >= 80 for t in temas),
        "dominio_medio": round(sum(t["dominio"] for t in temas) / len(temas)),
        "sessoes": len(sessoes),
        "evidencias_autonomas": sum(
            e.get("autonomous") is True and e.get("result") == "correct" for e in estado["evidences"]
        ),
        "cards": len(cards),
        "proximo_tema": foco["name"] if foco else "Formação concluída",
        "atualizado_em": estado["updated_at"][:10],
    }]

    salvar("temas.json", temas)
    salvar("fases.json", fases)
    # O painel recusa fonte sem linhas; o contador do resumo segue vindo do estado real.
    salvar("sessoes.json", sessoes or [SEM_SESSAO])
    salvar("resumo.json", resumo)
    print(f"{len(temas)} temas, {len(fases)} fases, {len(sessoes)} sessões em {OUT}")


if __name__ == "__main__":
    main()
