import {
  Autocomplete,
  Description,
  EmptyState,
  Label,
  ListBox,
  SearchField,
  useFilter,
} from "@heroui/react";

import { API_URL } from "../../config/api";
import { useAsyncList } from "@react-stately/data";
import { useState } from "react";

export function StateSelect({ value, onChange }) {
  const [selectedKey, setSelectedKey] = useState(null);
  const { contains } = useFilter({ sensitivity: "base" });

  const list = useAsyncList({
    async load({ signal }) {
      const res = await fetch(`${API_URL}/api/v1/estados`, {
        signal,
      });

      const json = await res.json();

      return {
        items: json,
      };
    },
  });

  return (
    <Autocomplete
      className="w-[256px]"
      placeholder="Selecione um estado"
      selectionMode="single"
      selectedKey={selectedKey}
      onSelectionChange={(key) => {
        setSelectedKey(key);
        if (onChange) onChange(key);
      }}
    >
      <Label>Estado (UF)</Label>

      <Autocomplete.Trigger>
        <Autocomplete.Value />
        <Autocomplete.ClearButton />
        <Autocomplete.Indicator />
      </Autocomplete.Trigger>

      <Autocomplete.Popover>
        <Autocomplete.Filter filter={contains}>
          <SearchField autoFocus name="search" variant="secondary">
            <SearchField.Group>
              <SearchField.SearchIcon />
              <SearchField.Input placeholder="Buscar estados..." />
              <SearchField.ClearButton />
            </SearchField.Group>
          </SearchField>

          <ListBox
            items={list.items}
            renderEmptyState={() => (
              <EmptyState>Nenhum estado encontrado</EmptyState>
            )}
          >
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
          </ListBox>
        </Autocomplete.Filter>
      </Autocomplete.Popover>

      <Description>
        Selecione o estado para buscar as soluções disponíveis
      </Description>
    </Autocomplete>
  );
}
