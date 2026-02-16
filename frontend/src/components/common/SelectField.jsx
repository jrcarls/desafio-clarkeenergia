import { Label, ListBox, Select } from "@heroui/react";
import { useAsyncList } from "@react-stately/data";
import { Collection } from "react-aria-components";

export function StateSelect() {
  const list = useAsyncList({
    async load({ signal }) {
      const res = await fetch("http://127.0.0.1:5000/api/v1/estados", {
        signal,
      });

      const json = await res.json();

      return {
        items: json,
      };
    },
  });

  return (
    <Select className="w-[256px]" placeholder="Selecione um estado">
      <Label>Estado (UF)</Label>

      <Select.Trigger>
        <Select.Value />
        <Select.Indicator />
      </Select.Trigger>

      <Select.Popover>
        <ListBox>
          <Collection items={list.items}>
            {(item) => (
              <ListBox.Item
                key={item.id}
                id={String(item.id)}
                textValue={item.nome}
              >
                {item.nome} ({item.sigla})
                <ListBox.ItemIndicator />
              </ListBox.Item>
            )}
          </Collection>
        </ListBox>
      </Select.Popover>
    </Select>
  );
}
