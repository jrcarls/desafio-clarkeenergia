import { StateSelect } from "./components/common/SelectField";
import { EnergyInput } from "./components/common/NumberInput";
import { ButtonSearch } from "./components/common/Button";
import { Surface } from "@heroui/react";
import { Separator } from "@heroui/react";
import { useState } from "react";
import { Basic } from "./components/common/Tabs";
import { API_URL } from "./config/api";
import { ModalInfo } from "./components/common/Modal";
import AppNavbar from "./components/layout/Navbar";

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
      const response = await fetch(`${API_URL}/api/v1/simulador`, {
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

  const processarResultados = (dados) => {
    if (!dados || dados.length === 0) return [];

    const mercadoLivre = dados.filter(
      (f) => f.tipo_solucao === "Mercado Livre",
    );
    const geracaoDistribuida = dados.filter(
      (f) => f.tipo_solucao === "Geração Distribuída",
    );

    const melhorML =
      mercadoLivre.length > 0
        ? mercadoLivre.reduce((a, b) => (a.economia > b.economia ? a : b))
        : null;
    const melhorGD =
      geracaoDistribuida.length > 0
        ? geracaoDistribuida.reduce((a, b) => (a.economia > b.economia ? a : b))
        : null;

    return dados.map((f) => ({
      ...f,
      melhorEconomia:
        (melhorML && f === melhorML) || (melhorGD && f === melhorGD),
    }));
  };

  const dadosProcessados = processarResultados(resultado);

  return (
    <>
      <ModalInfo />
      <AppNavbar />
      <div className="min-h-screen flex items-center justify-center bg-gray-50 p-4">
        <Surface
          className="flex w-full max-w-6xl h-auto md:h-150 flex-col gap-3 rounded-3xl border p-4 md:p-6"
          variant="transparent"
        >
          <div className="flex flex-col md:flex-row gap-6 md:gap-10 items-stretch md:items-start h-full">
            <div className="flex flex-col gap-4 md:gap-6 w-full md:w-auto md:min-w-70">
              <StateSelect value={estadoId} onChange={setEstadoId} />
              <EnergyInput value={consumoKwh} onChange={setConsumoKwh} />
              <Separator />
              <ButtonSearch onClick={handleBuscar} loading={loading} />

              {error && <div className="text-red-500 text-sm">{error}</div>}

              <Separator className="my-2 md:hidden" />
            </div>

            <div className="flex-1 w-full min-w-0 overflow-hidden">
              <Basic fornecedores={dadosProcessados} />
            </div>
          </div>
        </Surface>
      </div>
    </>
  );
}

export default App;
