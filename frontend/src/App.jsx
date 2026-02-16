import { StateSelect } from "./components/common/SelectField";
import { EnergyInput } from "./components/common/NumberInput";
import { WithAvatar } from "./components/common/Card";
import { ButtonSearch } from "./components/common/Button";
import { Surface, ScrollShadow } from "@heroui/react";
import { Separator } from "@heroui/react";
import { useState } from "react";

function App() {
  const [estadoId, setEstadoId] = useState(null);
  const [consumoKwh, setConsumoKwh] = useState(0);
  const [resultado, setResultado] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleBuscar = async () => {
    if (!estadoId || consumoKwh <= 0) {
      setError("Por favor, selecione um estado e informe o consumo");
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/simulador", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          estado_id: estadoId,
          consumo_kwh: consumoKwh,
        }),
      });

      if (!response.ok) {
        throw new Error("Erro ao buscar dados");
      }

      const data = await response.json();
      setResultado(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Função para marcar os melhores de cada solução
  const processarResultados = (dados) => {
    if (!dados || dados.length === 0) return [];

    // Agrupa por tipo de solução
    const mercadoLivre = dados.filter(
      (f) => f.tipo_solucao === "Mercado Livre",
    );
    const geracaoDistribuida = dados.filter(
      (f) => f.tipo_solucao === "Geração Distribuída",
    );

    // Encontra o ID do melhor de cada grupo (maior economia)
    const melhorML =
      mercadoLivre.length > 0
        ? mercadoLivre.reduce((a, b) => (a.economia > b.economia ? a : b))
        : null;
    const melhorGD =
      geracaoDistribuida.length > 0
        ? geracaoDistribuida.reduce((a, b) => (a.economia > b.economia ? a : b))
        : null;

    // Marca os melhores
    return dados.map((f) => ({
      ...f,
      melhorEconomia:
        (melhorML && f === melhorML) || (melhorGD && f === melhorGD),
    }));
  };

  // Use assim:
  const dadosProcessados = processarResultados(resultado);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <Surface
        className="flex min-w-[320px] flex-col gap-3 rounded-3xl border p-6"
        variant="transparent"
      >
        <div className="flex gap-10 items-start">
          <div className="flex flex-col gap-6">
            <StateSelect value={estadoId} onChange={setEstadoId} />
            <EnergyInput value={consumoKwh} onChange={setConsumoKwh} />
            <ButtonSearch onClick={handleBuscar} loading={loading} />

            {error && <div className="text-red-500 text-sm">{error}</div>}

            <Separator className="my-4" />

            {console.log(resultado) /* Exibir resultado para debug */}
          </div>

          <ScrollShadow className="max-h-125 p-4">
            <div className="flex flex-col gap-4">
              {dadosProcessados &&
                dadosProcessados.map((fornecedor, index) => (
                  <WithAvatar key={index} fornecedor={fornecedor} />
                ))}
            </div>
          </ScrollShadow>
        </div>
      </Surface>
    </div>
  );
}

export default App;
