const sequenceEl = document.getElementById("sequence");
const methodEl = document.getElementById("method");
const randomNEl = document.getElementById("random-n");
const randomMinEl = document.getElementById("random-min");
const randomMaxEl = document.getElementById("random-max");
const messageEl = document.getElementById("message");
const resultsPanel = document.getElementById("results-panel");
const sortedOutput = document.getElementById("sorted-output");
const methodBlurbEl = document.getElementById("method-blurb");
const resultsHeadRow = document.getElementById("results-head-row");
const resultsBody = document.querySelector("#results-table tbody");

/** @type {Map<string, {id: string, name: string, complexity_average: string, stable: boolean, blurb: string}>} */
const methodsById = new Map();

const QUADRATIC_IDS = new Set(["bubble", "selection", "insertion"]);
const LARGE_N_WARNING_THRESHOLD = 1000;

function setMessage(text, kind = "error") {
  messageEl.textContent = text || "";
  messageEl.classList.remove("is-error", "is-muted", "is-warn");
  if (!text) return;
  if (kind === "warn") {
    messageEl.classList.add("is-warn");
  } else if (kind === "muted") {
    messageEl.classList.add("is-muted");
  } else {
    messageEl.classList.add("is-error");
  }
}

function parseSequence(text) {
  const trimmed = text.trim();
  if (!trimmed) return [];
  const parts = trimmed.split(/[\s,]+/).filter(Boolean);
  const values = [];
  for (const part of parts) {
    if (!/^-?\d+$/.test(part)) {
      throw new Error(`Valor inválido: ${part}`);
    }
    values.push(Number(part));
  }
  if (values.length > 10000) {
    throw new Error("A sequência excede 10.000 elementos.");
  }
  return values;
}

function needsLargeNWarning(method, n) {
  if (n < LARGE_N_WARNING_THRESHOLD) return false;
  if (method === "all") return true;
  return QUADRATIC_IDS.has(method);
}

async function loadMethods() {
  const res = await fetch("/methods");
  if (!res.ok) return;
  const data = await res.json();
  for (const item of data.methods) {
    methodsById.set(item.id, item);
    const opt = document.createElement("option");
    opt.value = item.id;
    opt.textContent = item.name;
    methodEl.appendChild(opt);
  }
}

function generateRandom() {
  const n = Number(randomNEl.value);
  const min = Number(randomMinEl.value);
  const max = Number(randomMaxEl.value);
  if (!Number.isInteger(n) || n < 1 || n > 10000) {
    setMessage("N deve ser um inteiro entre 1 e 10.000.");
    return;
  }
  if (!Number.isInteger(min) || !Number.isInteger(max) || min > max) {
    setMessage("Intervalo inválido: informe mínimo e máximo inteiros.");
    return;
  }
  const values = [];
  for (let i = 0; i < n; i += 1) {
    values.push(Math.floor(Math.random() * (max - min + 1)) + min);
  }
  sequenceEl.value = values.join(" ");
  setMessage("Sequência aleatória gerada.", "muted");
}

function setTableHeaders(compareAll) {
  if (compareAll) {
    resultsHeadRow.innerHTML = `
      <th>Método</th>
      <th>Tempo (ms)</th>
      <th>Comparações</th>
      <th>Trocas</th>
      <th>Estável</th>
      <th>Complexidade (médio)</th>
    `;
  } else {
    resultsHeadRow.innerHTML = `
      <th>Método</th>
      <th>Tempo (ms)</th>
      <th>Comparações</th>
      <th>Trocas</th>
    `;
  }
}

function renderResults(results, method) {
  const compareAll = method === "all";
  setTableHeaders(compareAll);
  resultsBody.innerHTML = "";

  for (const row of results) {
    const meta = methodsById.get(row.method);
    const name = meta ? meta.name : row.method;
    const tr = document.createElement("tr");
    if (compareAll) {
      const stableLabel = meta ? (meta.stable ? "sim" : "não") : "-";
      const complexity = meta ? meta.complexity_average : "-";
      tr.innerHTML = `
        <td>${name}</td>
        <td>${row.time_ms.toFixed(3)}</td>
        <td>${row.comparisons}</td>
        <td>${row.swaps === null ? "-" : row.swaps}</td>
        <td>${stableLabel}</td>
        <td>${complexity}</td>
      `;
    } else {
      tr.innerHTML = `
        <td>${name}</td>
        <td>${row.time_ms.toFixed(3)}</td>
        <td>${row.comparisons}</td>
        <td>${row.swaps === null ? "-" : row.swaps}</td>
      `;
    }
    resultsBody.appendChild(tr);
  }

  sortedOutput.textContent = `Ordenado: [${results[0].sorted.join(", ")}]`;

  if (!compareAll) {
    const meta = methodsById.get(method);
    if (meta && meta.blurb) {
      methodBlurbEl.textContent = meta.blurb;
      methodBlurbEl.hidden = false;
    } else {
      methodBlurbEl.hidden = true;
      methodBlurbEl.textContent = "";
    }
  } else {
    methodBlurbEl.hidden = true;
    methodBlurbEl.textContent = "";
  }

  resultsPanel.hidden = false;
}

async function sortSequence() {
  setMessage("");
  let sequence;
  try {
    sequence = parseSequence(sequenceEl.value);
  } catch (err) {
    setMessage(err.message);
    return;
  }

  const method = methodEl.value;
  const warn = needsLargeNWarning(method, sequence.length);

  const res = await fetch("/sort", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sequence, method }),
  });

  if (!res.ok) {
    let detail = "Erro ao ordenar.";
    try {
      const body = await res.json();
      if (body.detail) {
        detail = typeof body.detail === "string" ? body.detail : JSON.stringify(body.detail);
      }
    } catch {
      /* ignore */
    }
    setMessage(detail);
    return;
  }

  const data = await res.json();
  renderResults(data.results, method);

  if (warn) {
    setMessage(
      "Aviso: com N ≥ 1.000, bubble/selection/insertion (e o modo todos) podem demorar — complexidade típica O(n²).",
      "warn"
    );
  } else {
    setMessage("Ordenação concluída.", "muted");
  }
}

document.getElementById("btn-generate").addEventListener("click", generateRandom);
document.getElementById("btn-sort").addEventListener("click", sortSequence);

loadMethods().catch(() => {
  setMessage("Não foi possível carregar os métodos da API.");
});
