import { Card, Chip } from "@heroui/react";
import { formatMoeda } from "../../utils/format";
import { BadgeDollarSign } from "lucide-react";
import { getSolucaoStyle } from "../../utils/chipSolution";

export function WithAvatar({ fornecedor }) {
  if (!fornecedor) {
    return null;
  }

  return (
    <div className="flex flex-col gap-6 w-full">
      <Card className="flex h-auto flex-col sm:flex-row">
        {/* Imagem - altura fixa no mobile, quadrada no desktop */}
        <div className="relative h-32 sm:h-40 w-full sm:w-40 shrink-0 overflow-hidden rounded-2xl">
          <img
            alt={fornecedor.nome}
            className="pointer-events-none absolute inset-0 h-full w-full object-cover select-none"
            loading="lazy"
            src={
              fornecedor.logo ||
              "https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/docs/cherries.jpeg"
            }
          />
        </div>

        <div className="flex flex-1 flex-col justify-between gap-2 p-3">
          {/* Header com título e chips */}
          <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-2">
            <div>
              <Card.Title className="text-base font-semibold leading-tight">
                {fornecedor.nome}
              </Card.Title>
              <Card.Description className="text-xs">
                Origem: {fornecedor.estado_origem}
              </Card.Description>
            </div>
            <div className="flex flex-wrap gap-2">
              {fornecedor.melhorEconomia && (
                <Chip
                  variant="solid"
                  className="shrink-0 text-xs bg-green-500 text-white"
                >
                  <BadgeDollarSign className="w-4 h-4" />
                  Melhor Economia
                </Chip>
              )}
              <Chip
                variant="outline"
                className={`shrink-0 text-xs ${getSolucaoStyle(fornecedor.tipo_solucao)}`}
              >
                {fornecedor.tipo_solucao}
              </Chip>
            </div>
          </div>

          {/* Valores e métricas */}
          <div className="flex flex-col gap-2">
            <div>
              <div className="text-lg sm:text-xl font-bold leading-none">
                {formatMoeda(fornecedor.economia)}/mês
              </div>
              <span className="text-xs text-muted-foreground">
                <span className="font-bold text-green-500">
                  {fornecedor.economia_percentual?.toFixed(2)}%
                </span>{" "}
                de economia
              </span>
            </div>

            {/* Grid responsivo para métricas */}
            <div className="grid grid-cols-2 sm:flex sm:flex-wrap gap-2 sm:gap-4 text-xs">
              <div>
                <span className="text-muted-foreground">Custo kWh: </span>
                <span className="font-bold">
                  {formatMoeda(fornecedor.custo_kwh)}
                </span>
              </div>
              <div>
                <span className="text-muted-foreground">Fornecedor: </span>
                <span className="font-bold">
                  {formatMoeda(fornecedor.custo_fornecedor)}
                </span>
              </div>
              <div>
                <span className="text-muted-foreground">Clientes: </span>
                <span className="font-bold text-purple-500">
                  {fornecedor.numero_clientes}
                </span>
              </div>
              <div>
                <span className="text-muted-foreground">Avaliação: </span>
                <span className="font-bold text-yellow-500">
                  {fornecedor.avaliacao_media}
                </span>
              </div>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}
