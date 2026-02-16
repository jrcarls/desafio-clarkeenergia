import { Label, NumberField, Description } from "@heroui/react";

export function EnergyInput({ value, onChange }) {
  return (
    <NumberField
      className="w-full max-w-64"
      value={value}
      onChange={onChange}
      minValue={0}
      step={0.1}
      formatOptions={{
        minimumFractionDigits: 1,
        maximumFractionDigits: 2,
      }}
      name="consumo"
    >
      <Label>Consumo Mensal (kWh)</Label>
      <NumberField.Group>
        <NumberField.DecrementButton />
        <NumberField.Input className="w-30" />
        <NumberField.IncrementButton />
      </NumberField.Group>
      <Description>Informe o consumo mensal de energia</Description>
    </NumberField>
  );
}
