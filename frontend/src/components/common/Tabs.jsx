import { Tabs } from "@heroui/react";
import { ScrollShadow } from "@heroui/react";
import { WithAvatar } from "./Card";

export function Basic({ fornecedores = [] }) {
  const mercadoLivre = fornecedores.filter(
    (f) => f.tipo_solucao === "Mercado Livre",
  );
  const geracaoDistribuida = fornecedores.filter(
    (f) => f.tipo_solucao === "Geração Distribuída",
  );

  return (
    <Tabs defaultSelectedKey="todas" className="w-full">
      <Tabs.ListContainer>
        <Tabs.List aria-label="Tipo de solução">
          <Tabs.Tab id="todas">
            Todas
            <Tabs.Indicator />
          </Tabs.Tab>
          <Tabs.Tab id="mercado-livre">
            Mercado Livre
            <Tabs.Indicator />
          </Tabs.Tab>
          <Tabs.Tab id="geracao-distribuida">
            Geração Distribuída
            <Tabs.Indicator />
          </Tabs.Tab>
        </Tabs.List>
      </Tabs.ListContainer>
      <Tabs.Panel className="pt-4" id="todas">
        <ScrollShadow className="max-h-[60vh] md:max-h-125 p-2 md:p-4">
          <div className="flex flex-col gap-4">
            {fornecedores.map((fornecedor, index) => (
              <WithAvatar key={index} fornecedor={fornecedor} />
            ))}
          </div>
        </ScrollShadow>
      </Tabs.Panel>
      <Tabs.Panel className="pt-4" id="mercado-livre">
        <ScrollShadow className="max-h-[60vh] md:max-h-125 p-2 md:p-4">
          <div className="flex flex-col gap-4">
            {mercadoLivre.map((fornecedor, index) => (
              <WithAvatar key={index} fornecedor={fornecedor} />
            ))}
          </div>
        </ScrollShadow>
      </Tabs.Panel>
      <Tabs.Panel className="pt-4" id="geracao-distribuida">
        <ScrollShadow className="max-h-[60vh] md:max-h-125 p-2 md:p-4">
          <div className="flex flex-col gap-4">
            {geracaoDistribuida.map((fornecedor, index) => (
              <WithAvatar key={index} fornecedor={fornecedor} />
            ))}
          </div>
        </ScrollShadow>
      </Tabs.Panel>
    </Tabs>
  );
}
