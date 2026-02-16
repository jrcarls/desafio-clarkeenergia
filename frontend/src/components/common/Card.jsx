import { Avatar, Card, Chip } from "@heroui/react";

export function WithAvatar() {
  return (
    <div className="flex flex-col gap-6 w-full max-w-4xl">
      {/* CARD GRANDE */}
      <Card className="col-span-12 flex h-auto flex-col sm:flex-row">
        <div className="relative h-40 w-full shrink-0 overflow-hidden rounded-2xl sm:h-40 sm:w-40">
          <img
            alt="Cherries"
            className="pointer-events-none absolute inset-0 h-full w-full object-cover select-none"
            loading="lazy"
            src="https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/docs/cherries.jpeg"
          />
        </div>

        <div className="flex flex-1 flex-col justify-between gap-2 p-3">
          {/* Header */}
          <div className="flex items-start justify-between gap-2">
            <div>
              <Card.Title className="text-base font-semibold leading-tight">
                Nome da Empresa
              </Card.Title>
              <Card.Description className="text-xs">
                Origem: UF
              </Card.Description>
            </div>
            <Chip
              variant="outline"
              className="shrink-0 text-xs bg-blue-50 text-blue-600"
            >
              Mercado Livre
            </Chip>
          </div>

          {/* Conteúdo compacto */}
          <div className="flex items-end justify-between gap-3">
            <div className="flex flex-col gap-2">
              <div>
                <div className="text-xl font-bold leading-none">
                  R$ 123,45/mês
                </div>
                <span className="text-xs text-muted-foreground">
                  de economia estimada
                </span>
              </div>

              <div className="flex gap-4 text-xs">
                <div>
                  <span className="text-muted-foreground">kWh: </span>
                  <span className="font-bold">R$ 1.234,56</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Clientes: </span>
                  <span className="font-bold">123</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Economia: </span>
                  <span className="font-bold text-green-600">90%</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Avaliação: </span>
                  <span className="font-bold text-yellow-600">4.5</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Card>
      <Card className="col-span-12 flex h-auto flex-col sm:flex-row">
        <div className="relative h-40 w-full shrink-0 overflow-hidden rounded-2xl sm:h-40 sm:w-40">
          <img
            alt="Cherries"
            className="pointer-events-none absolute inset-0 h-full w-full object-cover select-none"
            loading="lazy"
            src="https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/docs/cherries.jpeg"
          />
        </div>

        <div className="flex flex-1 flex-col justify-between gap-2 p-3">
          {/* Header */}
          <div className="flex items-start justify-between gap-2">
            <div>
              <Card.Title className="text-base font-semibold leading-tight">
                Nome da Empresa
              </Card.Title>
              <Card.Description className="text-xs">
                Origem: UF
              </Card.Description>
            </div>
            <Chip
              variant="outline"
              className="shrink-0 text-xs bg-orange-50 text-orange-600"
            >
              Geração Distribuída
            </Chip>
          </div>

          {/* Conteúdo compacto */}
          <div className="flex items-end justify-between gap-3">
            <div className="flex flex-col gap-2">
              <div>
                <div className="text-xl font-bold leading-none">
                  R$ 123,45/mês
                </div>
                <span className="text-xs text-muted-foreground">
                  de economia estimada
                </span>
              </div>

              <div className="flex gap-4 text-xs">
                <div>
                  <span className="text-muted-foreground">kWh: </span>
                  <span className="font-bold">R$ 1.234,56</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Clientes: </span>
                  <span className="font-bold">123</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Economia: </span>
                  <span className="font-bold text-green-600">90%</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Avaliação: </span>
                  <span className="font-bold text-yellow-600">4.5</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Card>
      <Card className="col-span-12 flex h-auto flex-col sm:flex-row">
        <div className="relative h-40 w-full shrink-0 overflow-hidden rounded-2xl sm:h-40 sm:w-40">
          <img
            alt="Cherries"
            className="pointer-events-none absolute inset-0 h-full w-full object-cover select-none"
            loading="lazy"
            src="https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/docs/cherries.jpeg"
          />
        </div>

        <div className="flex flex-1 flex-col justify-between gap-2 p-3">
          {/* Header */}
          <div className="flex items-start justify-between gap-2">
            <div>
              <Card.Title className="text-base font-semibold leading-tight">
                Nome da Empresa
              </Card.Title>
              <Card.Description className="text-xs">
                Origem: UF
              </Card.Description>
            </div>
            <Chip
              variant="outline"
              className="shrink-0 text-xs bg-blue-50 text-blue-600"
            >
              Mercado Livre
            </Chip>
          </div>

          {/* Conteúdo compacto */}
          <div className="flex items-end justify-between gap-3">
            <div className="flex flex-col gap-2">
              <div>
                <div className="text-xl font-bold leading-none">
                  R$ 123,45/mês
                </div>
                <span className="text-xs text-muted-foreground">
                  de economia estimada
                </span>
              </div>

              <div className="flex gap-4 text-xs">
                <div>
                  <span className="text-muted-foreground">kWh: </span>
                  <span className="font-bold">R$ 1.234,56</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Clientes: </span>
                  <span className="font-bold">123</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Economia: </span>
                  <span className="font-bold text-green-600">90%</span>
                </div>
                <div>
                  <span className="text-muted-foreground">Avaliação: </span>
                  <span className="font-bold text-yellow-600">4.5</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Card>
    </div>
  );
}
