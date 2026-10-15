const sequenceEl = document.getElementById("sequence");
const methodEl = document.getElementById("method");
const randomNEl = document.getElementById("random-n");
const randomMinEl = document.getElementById("random-min");
const randomMaxEl = document.getElementById("random-max");
const messageEl = document.getElementById("message");
const resultsPanel = document.getElementById("results-panel");
const sortedOutput = document.getElementById("sorted-output");
const resultsBody = document.querySelector("#results-table tbody");

const METHOD_LABELS = {
  bubble: "Bubble Sort",
  selection: "Selection Sort",
  insertion: "Insertion Sort",
  merge: "Merge Sort",
  quick: "Quick Sort",
  heap: "Heap Sort",
  tim: "Tim Sort",
};

function setMessage(text, isError = true) {
  messageEl.textContent = text || "";
  messageEl.style.color = isError ? "var(--danger)" : "var(--muted)";
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

async function loadMethods() {
  const res = await fetch("/methods");
  if (!res.ok) return;
  const data = await res.json();
  for (const item of data.methods) {
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
  setMessage("Sequência aleatória gerada.", false);
}

function renderResults(results) {
  resultsBody.innerHTML = "";
  for (const row of results) {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${METHOD_LABELS[row.method] || row.method}</td>
      <td>${row.time_ms.toFixed(3)}</td>
      <td>${row.comparisons}</td>
      <td>${row.swaps === null ? "-" : row.swaps}</td>
    `;
    resultsBody.appendChild(tr);
  }
  sortedOutput.textContent = `Ordenado: [${results[0].sorted.join(", ")}]`;
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

  const res = await fetch("/sort", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sequence, method: methodEl.value }),
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
  renderResults(data.results);
  setMessage("Ordenação concluída.", false);
}

document.getElementById("btn-generate").addEventListener("click", generateRandom);
document.getElementById("btn-sort").addEventListener("click", sortSequence);

loadMethods().catch(() => {
  setMessage("Não foi possível carregar os métodos da API.");
});
